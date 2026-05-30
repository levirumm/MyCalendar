from pathlib import Path
from PySide6.QtGui import QColor
from app.gui.palette import PALETTE


BUTTON_COLORS: list[str] = [
    "light_blue", "base_blue", "dark_blue", 
    "darkest_blue", "white", "red", 
    "orange", "yellow",
    "green", "purple", "pink"
]

CLASS_COLORS: list[str] = [
    "red", "orange", "yellow", 
    "green", "dark_blue", "darkest_blue", 
    "purple", "pink"
]

LIST_ITEM_COLORS: list[str] = ["light_blue", "white"]


def load_qss(paths: list[Path]) -> str:
    """
    Returns string joining QSS from all QSS files, inserting 
    palette values, and deriving button and list item colors.
    """
    return "\n".join(
        Path(path).read_text(encoding="utf-8").format(**PALETTE)
        for path in paths
    ) + generate_button_colors() + generate_list_item_colors()


def hover_color(color: QColor) -> str:
    """Returns slightly darker color preserving hue."""
    h, s, v, a = color.getHsv() # type:ignore
    # Boost saturation to prevent graying
    new_s = min(255, int(s * 1.1))
    # Reduce brightness
    new_v = max(0, int(v * 0.95))

    return QColor.fromHsv(h, new_s, new_v, a).name()


def pressed_color(color: QColor) -> str:
    """Returns darker color preserving hue."""
    h, s, v, a = color.getHsv() # type:ignore
    # Boost saturation to prevent graying
    new_s = min(255, int(s * 1.2))
    # Reduce brightness
    new_v = max(0, int(v * 0.9))

    return QColor.fromHsv(h, new_s, new_v, a).name()


def generate_button_colors(button_colors = BUTTON_COLORS) -> str:
    """
    Derives hover and pressed button colors given base color.
    Includes a [pressed=true] identifier for QWidgets 
    without a :pressed specifier.
    """
    qss = ""
    for color_key in button_colors:
        color = PALETTE[color_key]
        qcolor = QColor(color)
        qss += (
            f"QPushButton[color='{color_key}']" + "{\n"
            f"background-color: {color}; " + "}\n"

            f"QPushButton[color='{color_key}']:hover" + "{\n" 
            f"background-color: {hover_color(qcolor)}; " + "}\n"

            f"QPushButton[color='{color_key}']:pressed" + "{\n"
            f"background-color: {pressed_color(qcolor)}; " + "}\n"
        )
    return qss


def generate_list_item_colors(
        list_item_colors = LIST_ITEM_COLORS
    ) -> str:
    """
    Derives hover and pressed lsit item colors given base color.
    Includes a [pressed=true] and [hover=true] for toggling 
    states.
    """
    qss = ""
    for color_key in list_item_colors:
        color = PALETTE[color_key]
        qcolor = QColor(color)
        qss += (
            f"CalendarListItem[color='{color_key}']" + "{\n"
            f"background-color: {color}; " + "}\n"

            f"CalendarListItem[color='{color_key}'][hover='true']" + "{\n" 
            f"background-color: {hover_color(qcolor)}; " + "}\n"

            f"CalendarListItem[color='{color_key}'][pressed='true']" + "{\n"
            f"background-color: {pressed_color(qcolor)}; " + "}\n"
        )
    return qss
