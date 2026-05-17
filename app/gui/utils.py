from PySide6.QtWidgets import QWidget


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