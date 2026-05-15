from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont, QFontMetrics


SCALE_FACTORS = {
    "BASE": 1.0,
    "HEADING": 1.8,
    "SMALL": 0.8,
}


def make_font(base_font: QFont, size: float) -> QFont:
    """Makes a base font derivative of different size."""
    font = QFont(base_font)
    font.setPixelSize(int(size))
    return font


class Typography:
    """
    Central font registry for the app. All fonts are 
    derived from a single base application font.
    """
    # Default to application font for all
    BASE = QApplication.font()
    HEADING = BASE
    SMALL = BASE

    @staticmethod
    def init():
        app_font = QApplication.font()
        fm = QFontMetrics(app_font)
        base_size = fm.height()

        # Generate map of font name to font object
        fonts: dict[str, QFont] = {
            name: make_font(app_font, base_size * scale)
            for name, scale in SCALE_FACTORS.items()
        }

        Typography.BASE = fonts["BASE"]
        Typography.SMALL = fonts["SMALL"]
        Typography.HEADING = fonts["HEADING"]