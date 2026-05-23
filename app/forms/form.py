from PySide6.QtCore import QObject, Signal
from app.model.schema import ItemType, FieldName, ItemDescription
from app.forms.form_view import FormView
from app.forms.form_specs import (
    FormState, FormField, ValidationResult, FORM_FIELDS
)
from app.gui.palette import PALETTE
from app.gui.theme import CLASS_COLORS


class Form(QObject):
    """
    Form which allow users to enter, edit, and delete 
    class, assignment, and exam information.
    """
    formSaved = Signal(object, object)
    formInvalidated = Signal(str)

    def __init__(
            self, parent, item_type: ItemType, state: FormState, 
            color_map: dict[str, ItemDescription]
        ) -> None:
        super().__init__()
        self._type = item_type
        self._fields: dict[FieldName, FormField] = FORM_FIELDS[self._type]
        self._color_map = color_map

        # Determine colors allowed by color swatch
        colors = self._determine_allowed_colors()

        # Open and connect to form view
        self._view = FormView(
            parent, self._fields, self._type, state, 
            colors
        )
        self._view.connect_to_form(self)
    
    def open(self) -> None:
        self._view.exec()
    
    def connect_to_form(self, controller) -> None:
        """Connects form signals to controller methods."""
        self.formSaved.connect(controller.add_item)
        self.formInvalidated.connect(controller.on_invalid_form)
    
    def on_color_picked(self, color: str) -> None:
        """
        Sets indicator color. If assessment form, displays 
        title of selected class.
        """
        indicator_color = PALETTE[color]
        self._view.set_indicator(indicator_color)

        if self._type is not ItemType.CLASS:
            title = self._color_map[color].title
            self._view.display_class_title(title)

    def on_save(self) -> None:
        """
        Reads and validates form. If invalid, sends invalidForm 
        signal, else, bundles data and sends save signal.
        """
        field_data = self._view.read_entries()
        result = self._validate_fields(field_data)

        if not result.valid:
            self.formInvalidated.emit(result.reason)
            return
        
        if self._type is not ItemType.CLASS:
            self._bundle_class_id(field_data)
        
        self.formSaved.emit(field_data, self._type)
        self._view.accept()
    
    def _determine_allowed_colors(self) -> list[str]:
        """
        For classes, allows colors not yet selected from class 
        colors palette. Else, allows colors of existing classes.
        """
        if self._type is ItemType.CLASS:
            colors = [
                color for color in CLASS_COLORS 
                if color not in self._color_map.keys()
            ]
        else:
            colors = [c for c in self._color_map.keys()]
        return colors

    def _validate_fields(
            self, field_data: dict[FieldName, str]
        ) -> ValidationResult:
        """Validates data corresponding to each field."""
        for field_name, datum in field_data.items():
            if not datum and self._fields[field_name].required:
                return ValidationResult(
                    valid=False, reason=f"{field_name.value} cannot be null"
                )
        return ValidationResult(True)

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