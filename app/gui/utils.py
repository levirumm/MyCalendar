from PySide6.QtWidgets import QWidget, QSizePolicy


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
            f"padding-bottom: {height // 8}px;"
    )