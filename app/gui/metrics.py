from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont, QFontMetrics


FONT_SCALE_FACTORS = {
    "BASE": 1.0,
    "HEADING": 1.8,
    "SUB_HEADING": 1.15,
    "SMALL": 0.8,
}

ELEMENT_SCALE_FACTORS = {
    "HEADER_BUTTON": 2.8,
    "SMALL_BUTTON": 1.4,
    "DATE_LABEL_HIGHLIGHT": 1.3
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
    SUB_HEADING = BASE
    SMALL = BASE

    @staticmethod
    def init():
        app_font = QApplication.font()
        fm = QFontMetrics(app_font)
        base_size = fm.height()

        # Generate map of font name to font object
        fonts: dict[str, QFont] = {
            name: make_font(app_font, base_size * scale)
            for name, scale in FONT_SCALE_FACTORS.items()
        }

        Typography.BASE = fonts["BASE"]
        Typography.HEADING = fonts["HEADING"]
        Typography.SUB_HEADING = fonts["SUB_HEADING"]
        Typography.SMALL = fonts["SMALL"]


class Metrics:
    """
    Central ui element size registry for the app. Sizes 
    are derived from base font size.
    """
    HEADER_BUTTON = 0
    SMALL_BUTTON = 0
    DATE_LABEL_HIGHLIGHT = 0

    @staticmethod
    def init():
        base_size = Typography.BASE.pixelSize()

        # Generate map of element names to sizes
        sizes: dict[str, int] = {
            name: int(base_size * scale)
            for name, scale in ELEMENT_SCALE_FACTORS.items()
        }

        Metrics.HEADER_BUTTON = sizes["HEADER_BUTTON"]
        Metrics.SMALL_BUTTON = sizes["SMALL_BUTTON"]
        Metrics.DATE_LABEL_HIGHLIGHT = sizes["DATE_LABEL_HIGHLIGHT"]