from PySide6.QtWidgets import QDialog, QPushButton, QLayout, QSizePolicy
from PySide6.QtCore import QSize, Signal
from app.model.schema import ItemType, FieldName
from app.gui.utils import make_circle, make_bean, style_window
from app.gui.palette import PALETTE
from app.gui.metrics import Metrics, Typography
from app.forms.form_specs import FormField, FormState
from app.forms.field_builder import (
    FieldBuilder, SwatchButton, FormEntry
)
from app.gui.layout.ui_form import Ui_Form


class FormView(QDialog, Ui_Form):
    """
    View class of form which controls UI elements.
    """
    FORM_FACTOR: int = 25
    HEIGHT_OFFSET_RATIO: int = 5

    save = Signal()
    delete = Signal()
    completeToggled = Signal(bool)
    colorPicked = Signal(str)

    def __init__(
            self, parent, fields: dict[FieldName, FormField], 
            item_type: ItemType, colors: list[str]
        ) -> None:
        super().__init__(parent)
        self._ui = Ui_Form()
        self._ui.setupUi(self)

        self._colors = colors

        # Initialise view of form
        self._contextual_buttons = self._render_buttons(item_type)
        self._configure_form()
        self._shadow = style_window(self, self._ui.frame)

        # Dict mapping field keys to their entries
        self._field_entries: dict[FieldName, FormEntry] = {}

        # Build fields and add to map
        field_builder = FieldBuilder(self._ui.row_layout)
        for field_name, field in fields.items():
            entry = self._draw_form_field(
                field_name, field, field_builder
            )
            self._field_entries[field_name] = entry
    
    def set_complete(self, is_complete: bool) -> None:
        """Updates the check box."""
        self._ui.complete_button.setChecked(is_complete)
    
    def is_complete(self) -> bool:
        """Returns the status of the complete check box."""
        return self._ui.complete_button.isChecked()
    
    def read_entries(self) -> dict:
        """Returns dict mapping entry key to its datum."""
        return {
            key: entry.get()
            for key, entry in self._field_entries.items()
        }

    def set_fields(self, data: dict[FieldName, str]) -> None:
        """
        Inputs the field datum into the corresponding entry.
        """
        for field_name, datum in data.items():
            entry = self._field_entries.get(field_name, None)
            if entry:
                entry.set(datum)

    def set_state(self, state: FormState) -> None:
        """
        Disables/enables entries and hides/shows buttons 
        depending on state.
        """
        if state is FormState.VIEW:
            # Hide save, show contextual buttons
            self._ui.save_button.hide()
            for button in self._contextual_buttons:
                button.show()
        else:
            # Show save, hide contextual buttons
            self._ui.save_button.show()
            for button in self._contextual_buttons:
                button.hide()

        for entry in self._field_entries.values():
            if state is not FormState.VIEW:
                # All fields shown and enabled
                entry.set_hidden(False)
                entry.set_disabled(False)
                continue

            entry.set_disabled(True)

            # In view state, only show filled entries
            if not entry.get():
                entry.set_hidden(True)
      
    def set_selection(self, color: str) -> None:
        """Sets the swatch to given color."""
        swatch = self._field_entries[FieldName.COLOR]
        swatch.set(color)
    
    def hide_swatch(self) -> None:
        """Removes the swatch from the form."""
        swatch = self._field_entries[FieldName.COLOR]
        swatch.set_hidden(True)
    
    def disable_swatch(self) -> None:
        """Disables the swatch button."""
        swatch = self._field_entries[FieldName.COLOR]
        swatch.set_disabled(True)
        
    def display_class_title(self, title: str) -> None:
        """Updates label on color swatch to be class title."""
        swatch = self._field_entries[FieldName.COLOR]
        swatch.set_text(title) # type: ignore
    
    def set_indicator(self, color: str) -> None:
        """Sets the color of the color indicator."""
        btn_size = Metrics.COLOR_IDENTIFIER
        self._ui.color_indicator.setStyleSheet(
            f"background-color: {color};"
        )
        make_circle(self._ui.color_indicator, btn_size)
        self._ui.color_indicator.style().polish(
            self._ui.color_indicator
        )

    def connect_to_form(self, form) -> None:
        """Connects form view signals to form slots."""
        self.save.connect(form.on_save)
        self.delete.connect(form.on_delete)
        self.colorPicked.connect(form.on_color_picked)
        self.completeToggled.connect(form.on_complete_toggled)

    def _toggle_check_box(self, check_box: QPushButton) -> None:
        """Updates the styling of the button based on status."""
        checked = check_box.isChecked() 
        check_box.setProperty(
            "role", "checked" if checked else "unchecked"
        )
        check_box.style().polish(check_box)
        self.completeToggled.emit(checked)

    def _render_buttons(self, item_type: ItemType) -> list[QPushButton]:
        """
        Renders the close, save, edit, and mark complete 
        buttons at the top of the form. Returns the buttons 
        which are hidden and shown based on state.
        """
        # Close, edit, delete, and complete buttons
        btn_size = Metrics.COLOR_IDENTIFIER

        # Get list of buttons which appear on form
        buttons = [
            self._ui.edit_button, self._ui.delete_button
        ]

        if item_type is ItemType.CLASS:
            # Class forms do not have a complete button
            self._ui.complete_button.hide()
        else:
            buttons.append(self._ui.complete_button)
        
        for button in buttons + [ self._ui.close_button,]:
            button.setProperty("color", "lightest_blue")
            button.setIconSize(QSize(btn_size, btn_size))
            make_circle(button, btn_size)

        self._toggle_check_box(self._ui.complete_button)

        # Render save button
        self._ui.save_button.setProperty("color", "darkest_blue")
        self._ui.save_button.setProperty("text_color", "white")
        self._ui.save_button.setProperty("role", "save")
        self._ui.save_button.setFont(Typography.BASE)
        make_bean(self._ui.save_button, btn_size)

        # Connect to buttons
        self._ui.close_button.clicked.connect(self.accept)
        self._ui.edit_button.clicked.connect(
            lambda: self.set_state(FormState.EDIT)
        )
        self._ui.delete_button.clicked.connect(self._on_delete)
        self._ui.complete_button.toggled.connect(
            lambda: self._toggle_check_box(self._ui.complete_button)
        )
        self._ui.save_button.clicked.connect(self.save.emit)

        return buttons

    def _on_delete(self) -> None:
        """Emits delete signal and restyles button."""
        self.delete.emit()
        self._ui.delete_button.style().polish(self._ui.delete_button)
    
    def _configure_form(self) -> None:
        """
        Applies styling to form elements, including window attributes, 
        qss properties, margins + spacing, and drop shadow.
        """
        # Apply styling to frame
        self._ui.frame.setProperty("role", "form")
        self.set_indicator(PALETTE["light_blue"])
        width = Typography.BASE.pixelSize() * self.FORM_FACTOR

        self._center()

        # Set fixed width, size constraint, and ignored 
        # horizontal size policy.This way, the form 
        # expands and shrink vertically but not horizontally
        self._ui.frame.setFixedWidth(width)
        self._ui.verticalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize
        )
        self._ui.frame.setSizePolicy(
            QSizePolicy.Policy.Ignored, 
            QSizePolicy.Policy.Preferred
        )
    
        # Apply margins to form
        self._ui.title_layout.setSpacing(Metrics.COLOR_IDENTIFIER)
        side_padding = Metrics.COLOR_IDENTIFIER
        end_padding = Typography.SMALL.pixelSize()
        self._ui.frame_layout.setContentsMargins(
            side_padding, end_padding, side_padding, end_padding
        )
        self._ui.save_button_layout.setContentsMargins(
            0, end_padding, 0, 0
        )
    
    def _center(self):
        """
        Centers in the screen horizontally. Sets the y position 
        to a fifth of the total screen height.
        """
        screen = self.screen().geometry()
        geo = self.frameGeometry()

        # Center horizontally
        x = screen.center().x() - geo.width() // 2

        # Fixed vertical position at 1/5 screen height
        y = screen.top() + screen.height() // self.HEIGHT_OFFSET_RATIO

        # Clamp x so it cannot go off screen
        x = max(screen.left(), min(x, screen.right() - geo.width()))

        self.move(x, y)
    
    def _draw_form_field(
            self, field_name: FieldName, field: FormField, 
            field_builder: FieldBuilder
        ) -> FormEntry:
        """Renders and returns form field given specs."""
        match field_name:
            case FieldName.TITLE:
                entry = field_builder.add_title(
                    field, self._ui.title_layout
                )
            case FieldName.COLOR:
                entry = field_builder.add(field)

                if isinstance(entry, SwatchButton):
                    entry.button.clicked.connect(
                        lambda: self._open_swatch(entry)
                    )
                    entry.colorPicked.connect(self._on_color_picked)
            case _:
                entry = field_builder.add(field)
        return entry
        
    def _open_swatch(self, swatch: SwatchButton) -> None:
        """Opens swatch anchored to color indicator."""
        swatch.open_swatch(
            parent=self._ui.frame, anchor=self._ui.color_indicator, 
            colors=self._colors
        )
    
    def _on_color_picked(self, color: str) -> None:
        """Sets color indicator and emits signal."""
        self.colorPicked.emit(color)