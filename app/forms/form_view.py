from PySide6.QtWidgets import QDialog, QPushButton
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
    colorPicked = Signal(str)
    save = Signal()

    def __init__(
            self, parent, fields: dict[FieldName, FormField], 
            item_type: ItemType, state: FormState, colors: list[str]
        ) -> None:
        super().__init__(parent)
        self._ui = Ui_Form()
        self._ui.setupUi(self)

        # Configure form
        self._colors = colors
        self._render_buttons()
        self._configure_form()
        self._toggle_state(state)
        self._shadow = style_window(self, self._ui.frame)

        # Dict mapping field keys to their entries
        self._field_entries: dict[FieldName, FormEntry] = {}

        # Build fields and add to map
        field_builder = FieldBuilder(self._ui.row_layout)
        for field_name, field in fields.items():
            entry = self._draw_form_field(field_name, field, field_builder)
            self._field_entries[field_name] = entry
    
    def read_entries(self) -> dict:
        """Returns dict mapping entry key to its datum."""
        return {
            key: entry.get()
            for key, entry in self._field_entries.items()
        }

    def display_class_title(self, title: str) -> None:
        """Updates label on color swatch to be class title."""
        swatch = self._field_entries[FieldName.COLOR]
        swatch.set(title)
    
    def set_indicator(self, color: str) -> None:
        """Sets the color of the color indicator."""
        btn_size = Metrics.COLOR_IDENTIFIER
        self._ui.color_indicator.setStyleSheet(
            f"background-color: {color};"
        )
        make_circle(self._ui.color_indicator, btn_size)
        self._ui.color_indicator.style().polish(self._ui.color_indicator)

    def connect_to_form(self, form) -> None:
        """Connects form view signals to form slots."""
        self.save.connect(form.on_save)
        self.colorPicked.connect(form.on_color_picked)

    def _toggle_check_box(self, check_box: QPushButton) -> None:
        """Updates the styling of the button based on status."""
        check_box.setProperty(
            "role", "checked" if check_box.isChecked() 
            else "unchecked"
        )
        check_box.style().polish(check_box)

    def _render_buttons(self) -> None:
        """
        Renders the close, save, edit, and mark complete 
        buttons at the top of the form.
        """
        # Close, edit, delete, and complete buttons
        btn_size = Metrics.COLOR_IDENTIFIER
        for button in [
            self._ui.close_button, self._ui.edit_button, 
            self._ui.delete_button, self._ui.complete_button
        ]:
            button.setProperty("color", "lightest_blue")
            button.setIconSize(QSize(btn_size, btn_size))
            make_circle(button, btn_size)

        self._toggle_check_box(self._ui.complete_button)

        # Render save button
        self._ui.save_button.setProperty("color", "darkest_blue")
        self._ui.save_button.setProperty("text_color", "white")
        self._ui.save_button.setFont(Typography.BASE)
        make_bean(self._ui.save_button, btn_size)

        # Connect to buttons
        self._ui.close_button.clicked.connect(lambda: self.accept())
        self._ui.complete_button.toggled.connect(
            lambda: self._toggle_check_box(self._ui.complete_button)
        )
        self._ui.save_button.clicked.connect(lambda: self.save.emit())
    
    def _configure_form(self) -> None:
        """
        Applies styling to form elements, including window attributes, 
        qss properties, margins + spacing, and drop shadow.
        """
        # Apply styling to frame
        self._ui.frame.setProperty("role", "form")

        self.set_indicator(PALETTE["blue"]["light"])

        # Apply margins to form
        self._ui.title_layout.setSpacing(Metrics.COLOR_IDENTIFIER)
        side_padding = Metrics.COLOR_IDENTIFIER
        end_padding = Typography.SMALL.pixelSize()
        self._ui.frame_layout.setContentsMargins(
            side_padding, end_padding, side_padding, end_padding
        )
    
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
    
    def _toggle_state(self, state: FormState) -> None:
        """Configures the view based on the state of the form."""
        if state is FormState.ADD:
            self._ui.edit_button.hide()
            self._ui.complete_button.hide()
            self._ui.delete_button.hide()
        
    def _open_swatch(self, swatch: SwatchButton) -> None:
        """Opens swatch anchored to color indicator."""
        swatch.open_swatch(
            parent=self._ui.frame, anchor=self._ui.color_indicator, 
            colors=self._colors
        )
    
    def _on_color_picked(self, color: str) -> None:
        """Sets color indicator and emits signal."""
        self.colorPicked.emit(color)