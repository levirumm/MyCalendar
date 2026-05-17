from PySide6.QtWidgets import QDialog, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from app.gui.layout.ui_form import Ui_Form


class FormView(QDialog, Ui_Form):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        ui = Ui_Form()
        ui.setupUi(self)

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
        ui.frame.setProperty("role", "form")

        # Apply drop shadow
        self._shadow = QGraphicsDropShadowEffect()
        self._shadow.setBlurRadius(15)
        self._shadow.setXOffset(0)
        self._shadow.setYOffset(1)
        ui.frame.setGraphicsEffect(self._shadow)