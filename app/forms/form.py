from PySide6.QtCore import QObject, Signal
from app.model.schema import ItemType, FieldName, ItemDescription
from app.forms.form_view import FormView
from app.forms.form_specs import (
    FormState, FormField, Result, FORM_FIELDS
)
from app.gui.palette import PALETTE
from app.gui.theme import CLASS_COLORS



ERROR_MESSAGES: dict[FieldName, str] = {
    # Maps fields to their error messages. Some, 
    # like due date, should never be triggered, 
    # but are included as a precaution
    FieldName.TITLE: "Must Include a title",
    FieldName.COLOR: "Must select a class color",
    FieldName.CLASS_ID: "Must select a class",
    FieldName.DUE_DATE: "Enter a valid due date",
    FieldName.OPEN_DATE: "Enter a valid open date",
    FieldName.WEIGHT: "Enter a valid weight (0-100)",
    FieldName.TIME: "Enter a valid time"
}



class Form(QObject):
    """
    Form which allow users to enter, edit, and delete 
    class, assignment, and exam information.
    """
    formSaved = Signal(object, object)
    formInvalidated = Signal(str)
    formEdited = Signal(object, object, int, object)
    deleteItem = Signal()
    completeToggled = Signal(object, int, bool)

    def __init__(
            self, parent, item_type: ItemType, 
            classes: list[ItemDescription],
            item_id: int | None = None
        ) -> None:
        super().__init__()
        self._type = item_type
        self._fields: dict[FieldName, FormField] = (
            FORM_FIELDS[self._type]
        )
        self._item_id = item_id

        # Dict mapping class color to class description
        self._color_map = {d.color: d for d in classes}

        colors = self._determine_allowed_colors()

        # Open and connect to form view
        self._view = FormView(
            parent, self._fields, self._type, colors
        )
        self._view.connect_to_form(self)
    
    def open(self) -> None:
        self._view.exec()
    
    def close(self) -> None:
        self._view.accept()
    
    def connect_to_form(self, controller) -> None:
        """Connects form signals to controller methods."""
        self.formSaved.connect(controller.add_item)
        self.formInvalidated.connect(controller.on_invalid_form)

        if not self._item_id: return

        # Connect to delete button which required id
        self.deleteItem.connect(
            lambda: controller.delete_item(
                self._type, self._item_id, self
            )
        )
        self.formEdited.connect(controller.edit_item)

        if self._type is ItemType.CLASS: return

        # Connect to complete toggled signal
        self.completeToggled.connect(
            controller.on_complete_toggled
        )
    
    def set_state(self, form_state: FormState) -> None:
        """Sets the state of the form."""
        self._view.set_state(form_state)
        self._state = form_state

        # Class form hides color swatch in view state
        if (
            form_state is FormState.VIEW 
            and self._type is ItemType.CLASS
        ):
            self._view.hide_swatch()
            return
    
    def set_fields(self, data: dict[FieldName, str]) -> None:
        """Inputs the data into corresponding field entries."""
        # Remove and get class id field
        class_id = data.get(FieldName.CLASS_ID, None)

        if self._type is not ItemType.CLASS:
            color = next(
                c.color for c in self._color_map.values() 
                if c.item_id == class_id
            )
            data[FieldName.COLOR] = color
            self._view.display_class_title(
                self._color_map[color].title
            )
        else:
            color = data[FieldName.COLOR]

        self._view.set_fields(data)
        self._view.set_indicator(PALETTE[color])
    
    def set_class(self, cls: ItemDescription) -> None:
        """
        Manually sets class selection. Used if there is 
        only one class available.
        """
        self.on_color_picked(cls.color)
        self._view.disable_swatch()

    def on_save(self) -> None:
        """
        Reads and validates form. If invalid, sends invalidForm 
        signal, else, bundles data and sends save/edit signal 
        depending on state.
        """
        field_data = self._view.read_entries()
        result = self._validate_fields(field_data)

        if not result.valid:
            self.formInvalidated.emit(result.reason)
            return
        
        if self._type is not ItemType.CLASS:
            self._bundle_class_id(field_data)
        
        # If in add state, add new item to database
        if self._state is FormState.ADD:
            self.formSaved.emit(field_data, self._type)
            self._view.accept()
        
        # If in edit state, update in database
        else:
            self.formEdited.emit(
                field_data, self._type, self._item_id,
                self
            )
    
    def on_delete(self) -> None:
        """Emits signal to delete item and closes form."""
        self.deleteItem.emit()
    
    def set_complete(self, is_complete: bool) -> None:
        """Updates the check box to match complete status."""
        self._view.set_complete(is_complete)
    
    def on_color_picked(self, color: str) -> None:
        """
        Sets indicator color. If assessment form, displays 
        title of selected class.
        """
        indicator_color = PALETTE[color]
        self._view.set_indicator(indicator_color)
        self._view.set_selection(color)

        if self._type is not ItemType.CLASS:
            title = self._color_map[color].title
            self._view.display_class_title(title)
    
    def on_complete_toggled(self, complete: bool) -> None:
        """Emits completeToggled signal."""
        self.completeToggled.emit(
            self._type, self._item_id, complete
        )
    
    def _determine_allowed_colors(self) -> list[str]:
        """
        For classes, allows colors not yet selected from class 
        colors palette. Else, allows colors of existing classes.
        """
        if self._type is not ItemType.CLASS:
            return [c for c in self._color_map.keys()]
        
        # Do not allow multiple classes to share color
        colors = [
            color for color in CLASS_COLORS 
            if color not in self._color_map.keys()
        ]

        if self._item_id:
            # Classes own color appears in swatch, so user can 
            # reset to original choice.
            colors.append(
                next(c.color for c in self._color_map.values() 
                if c.item_id == self._item_id)
            )
        return colors

    def _validate_fields(
            self, field_data: dict[FieldName, str]
        ) -> Result:
        """Validates data corresponding to each field."""
        for field_name, datum in field_data.items():
            if not datum and field_name is FieldName.COLOR:
                return Result(
                    valid=False, reason=ERROR_MESSAGES[
                        FieldName.COLOR if self._type 
                        is ItemType.CLASS else FieldName.CLASS_ID
                    ]
                )
            if not datum and self._fields[field_name].required:
                return Result(
                    valid=False, reason=ERROR_MESSAGES[field_name]
                )
            if (
                field_name is FieldName.WEIGHT 
                and datum and float(datum) > 100
            ):
                return Result(
                    valid=False, reason=ERROR_MESSAGES[field_name]
                )
        return Result(True)

    def _bundle_class_id(
            self, field_data: dict[FieldName, str]
        ) -> None:
        """Replaces color field with class id field."""
        color = field_data[FieldName.COLOR]

        # Remove color field
        field_data.pop(FieldName.COLOR)

        # Add field 'class_id' matching selection
        field_data[FieldName.CLASS_ID] = (
            str(self._color_map[color].item_id)
        )