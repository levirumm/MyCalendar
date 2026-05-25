from PySide6.QtWidgets import (
    QWidget, QFrame, QDialog, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt


def make_circle(widget: QWidget, diameter: int) -> None:
    """
    Sets the border radius of the widget in style sheet 
    to be the radius of the widget.
    """
    margin = 1 # 1px margin to avoid clipping
    widget.setFixedSize(diameter + 2 * margin, diameter + 2 * margin)
    widget.setStyleSheet(
        widget.styleSheet() + (
            f"border-radius: {diameter // 2}px;"
            f"margin: {margin}px"
        )
    )
    

def make_bean(widget: QWidget, height: int) -> None:
    """
    Sets the border radius of the widget in style sheet 
    to be the height of the widget.
    """
    margin = 1 # 1px margin to avoid clipping
    widget.setFixedHeight(height)
    widget.setStyleSheet(
        widget.styleSheet() +
            f"border-radius: {height // 2}px;" 
            f"margin-left: {margin}px;"
            f"margin-right: {margin}px;"
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
        dialog: QDialog, anchor: QWidget, anchor_side: str = "left"
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