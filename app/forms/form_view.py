from PySide6.QtWidgets import (
    QDialog, QGraphicsDropShadowEffect, QFrame
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap
from resources import resources_rc
from app.gui.utils import make_circle
from app.gui.palette import PALETTE
from app.gui.metrics import Metrics, Typography
from app.gui.layout.ui_form import Ui_Form
from app.forms.form_specs import FormRow


class FormView(QDialog, Ui_Form):
    def __init__(
            self, parent, form_specs: dict[str, FormRow]
        ) -> None:
        super().__init__(parent)
        ui = Ui_Form()
        ui.setupUi(self)
        self._complete_button = ui.complete_button

        self._style_window(ui.frame)
        self._render_buttons(ui)
        self._render_title_row(ui, form_specs["title"])

        self._complete_button.toggled.connect(self._toggle_check_box)

        self._toggle_check_box()
    
    def _toggle_check_box(self) -> None:
        if self._complete_button.isChecked():
            self._complete_button.setIcon(QIcon(":/box_checked.svg"))
        else:
            self._complete_button.setIcon(QIcon(":/box_unchecked.svg"))

    def _render_buttons(self, ui: Ui_Form) -> None:
        """
        Renders the close, save, edit, and mark complete 
        buttons at the top of the form.
        """
        btn_size = Metrics.COLOR_IDENTIFIER
        ui.complete_button.setFixedSize(btn_size, btn_size)

        for button in [
            ui.close_button, ui.edit_button, 
            ui.delete_button, ui.complete_button
        ]:
            button.setProperty("variant", "0_blue")
            make_circle(button, btn_size)
            button.setIconSize(QSize(btn_size, btn_size))
    
    def _render_title_row(
            self, ui: Ui_Form, row_specs: FormRow
        ) -> None:
        """Renders the title entry row, including color indicator."""
        # Title entry
        ui.name_entry.setFont(Typography.SUB_HEADING)
        ui.name_entry.setPlaceholderText(row_specs.placeholder)

        # Color identifier
        ui.color_indicator.setStyleSheet(
            f"background-color: {PALETTE["2_blue"]};"
        )
        make_circle(ui.color_indicator, Metrics.COLOR_IDENTIFIER)
    
    def _style_window(self, frame: QFrame) -> None:
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