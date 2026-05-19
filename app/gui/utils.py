from PySide6.QtWidgets import (
    QWidget, QFrame, QDialog, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


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


def generate_button_colors(colors: dict[str, str]) -> str:
    """
    Derives hover and pressed button colors given base color.
    """
    qss = ""

    for name, color in colors.items():
        qcolor = QColor(color)
        qss += (
            f"QPushButton[color='{name}']"  + "{\n"
            f"background-color: {color}; " + "}\n"

            f"QPushButton[color='{name}']:hover"  + "{\n" 
            f"background-color: {hover_color(qcolor)}; " + "}\n"

            f"QPushButton[color='{name}']:pressed"  + "{\n"
            f"background-color: {pressed_color(qcolor)}; " + "}\n"
        )
    return qss


def make_circle(widget: QWidget, diameter: int) -> None:
    """
    Sets the border radius of the widget in style sheet 
    to be the radius of the widget.
    """
    widget.setFixedSize(diameter, diameter)
    widget.setStyleSheet(
        widget.styleSheet() +
            f"border-radius: {diameter // 2}px;"
    )


def make_bean(widget: QWidget, height: int) -> None:
    """
    Sets the border radius of the widget in style sheet 
    to be the height of the widget.
    """
    widget.setFixedHeight(height)
    widget.setStyleSheet(
        widget.styleSheet() +
            f"border-radius: {height // 2}px;" \
            f"padding-bottom: {height // 12}px;"
    )


def style_window(
        dialog: QDialog, frame: QFrame
    ) -> QGraphicsDropShadowEffect:
    """
    Applies styling to window, including Qt window attributes 
    and drop shadow.
    """
    # Apply window flags and attributes
    dialog.setWindowFlags(
        Qt.WindowType.FramelessWindowHint |
        Qt.WindowType.Popup | 
        Qt.WindowType.NoDropShadowWindowHint
    )
    dialog.setAttribute(
        Qt.WidgetAttribute.WA_TranslucentBackground
    )

    # Apply drop shadow
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setXOffset(0)
    shadow.setYOffset(1)
    frame.setGraphicsEffect(shadow)

    return shadow


def anchor_window(
        dialog: QDialog, anchor: QWidget, anchor_side: str
    ) -> None:
    """
    Positions the dialog such that it right/left corner is 
    on anchor widget.
    """
    center = anchor.mapToGlobal(anchor.rect().center())
    x = (
        center.x() - (dialog.width() 
        if anchor_side == "right" else 0)
    )
    y = center.y()
    dialog.move(x, y)