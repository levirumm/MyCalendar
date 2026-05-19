from PySide6.QtWidgets import (
    QDialog, QGraphicsDropShadowEffect, QFrame, 
    QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt, QSize

from app.gui.utils import make_circle, make_bean
from app.gui.palette import PALETTE
from app.gui.metrics import Metrics, Typography
from app.gui.layout.ui_form import Ui_Form
from app.forms.form_specs import FormField
from app.forms.field_builder import FieldBuilder


class FormView(QDialog, Ui_Form):
    """
    View class of form which controls UI elements.
    """
    def __init__(
            self, parent, form_specs: list[FormField]
        ) -> None:
        super().__init__(parent)
        ui = Ui_Form()
        ui.setupUi(self)

        self._style_window(ui.frame, ui.frame_layout)
        self._render_buttons(ui)

        # Iteratively draw rows in form
        field_builder = FieldBuilder(ui.row_layout)
        for field in form_specs:
            if field.key == "title":
                self._render_title_row(ui, field)
            else:
                field_builder.add(field)

    def _toggle_check_box(self, check_box: QPushButton) -> None:
        """
        Updates the styling of the button based on status.
        """
        check_box.setProperty(
            "role", "checked" if check_box.isChecked() 
            else "unchecked"
        )
        check_box.style().polish(check_box)

    def _render_buttons(self, ui: Ui_Form) -> None:
        """
        Renders the close, save, edit, and mark complete 
        buttons at the top of the form.
        """
        # Close, edit, delete, and complete buttons
        btn_size = Metrics.COLOR_IDENTIFIER
        for button in [
            ui.close_button, ui.edit_button, 
            ui.delete_button, ui.complete_button
        ]:
            button.setProperty("variant", "0_blue")
            button.setIconSize(QSize(btn_size, btn_size))
            make_circle(button, btn_size)

        self._toggle_check_box(ui.complete_button)
        ui.close_button.clicked.connect(lambda: self.accept())
        ui.complete_button.toggled.connect(
            lambda: self._toggle_check_box(ui.complete_button)
        )

        # Save button
        ui.save_button.setProperty("variant", "5_blue")
        ui.save_button.setProperty("style", "white")
        ui.save_button.setFont(Typography.BASE)
        make_bean(ui.save_button, btn_size)
        
    def _render_title_row(
            self, ui: Ui_Form, field: FormField
        ) -> None:
        """
        Renders the title entry row, including color indicator.
        """
        ui.title_layout.setSpacing(Metrics.COLOR_IDENTIFIER)

        # Title entry
        ui.name_entry.setFont(Typography.SUB_HEADING)
        ui.name_entry.setPlaceholderText(field.placeholder)
        ui.name_entry.setProperty("role", "name_entry")

        # Color identifier
        ui.color_indicator.setStyleSheet(
            f"background-color: {PALETTE["2_blue"]};"
        )
        make_circle(ui.color_indicator, Metrics.COLOR_IDENTIFIER)
    
    def _style_window(
            self, frame: QFrame, frame_layout: QVBoxLayout
        ) -> None:
        """
        Applies styling to window, including Qt window 
        attributes, qss properties, and drop shadow.
        """
        # Apply window flags and attributes
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Popup | 
            Qt.WindowType.NoDropShadowWindowHint
        )
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        # Apply styling to frame
        frame.setProperty("role", "form")

        # Apply drop shadow
        self._shadow = QGraphicsDropShadowEffect()
        self._shadow.setBlurRadius(15)
        self._shadow.setXOffset(0)
        self._shadow.setYOffset(1)
        frame.setGraphicsEffect(self._shadow)

        # Apply margins to form
        side_padding = Metrics.COLOR_IDENTIFIER
        end_padding = Typography.SMALL.pixelSize()
        frame_layout.setContentsMargins(
            side_padding, end_padding, side_padding, end_padding
        )