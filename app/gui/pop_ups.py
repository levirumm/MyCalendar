from PySide6.QtWidgets import (
    QDialog, QGridLayout, QPushButton
)
from math import ceil
from app.gui.layout.ui_event_choice import Ui_EventChoice
from app.gui.layout.ui_color_swatch import Ui_ColorSwatch
from app.model.schema import ItemType
from app.gui.metrics import Typography, Metrics
from app.gui.utils import make_circle, style_window


class EventSelect(QDialog, Ui_EventChoice):
    """
    Dialog which allows user to choose to input a new 
    assignment or a new exam.
    """
    def __init__(self, parent) -> None:
        super().__init__(parent)
        ui = Ui_EventChoice()
        ui.setupUi(self)

        self._selection = None

        self._shadow = style_window(self, ui.frame)
        ui.frame.setProperty("role", "menu")

        for button in [ui.assignment_button, ui.exam_button]:
            button.setFont(Typography.BASE)
            button.setProperty("color", "white")
            button.setProperty("role", "drop_down")
        
        ui.assignment_button.clicked.connect(
            self._on_assignment_clicked
        )
        ui.exam_button.clicked.connect(self._on_exam_clicked)
    
    @property
    def selection(self) -> ItemType | None:
        return self._selection
        
    def _on_assignment_clicked(self) -> None:
        """Sets selection and closes window."""
        self._selection = ItemType.ASSIGNMENT
        self.accept()

    def _on_exam_clicked(self) -> None:
        """Sets selection and closes window."""
        self._selection = ItemType.EXAM
        self.accept()


class ColorSwatch(QDialog, Ui_ColorSwatch):
    """
    Dialog which allows user to choose to select the color 
    of their class, or the class color corresponding to 
    an assessment.
    """
    def __init__(self, parent, colors: list[str]) -> None:
        super().__init__(parent)
        ui = Ui_ColorSwatch()
        ui.setupUi(self)

        self._selection = None

        self._shadow = style_window(self, ui.frame)
        ui.frame.setProperty("role", "menu")

        self._populate_swatch(colors, ui.swatch_layout)
    
    def _populate_swatch(
            self, colors: list[str], layout: QGridLayout
        ) -> None:
        """
        Populates the swatch layout with QPushButtons for 
        selection colors.
        """
        color_amount = len(colors)
        counter = 0

        rows = (color_amount - 1)// 4 + 1
        cols = ceil(color_amount / rows)

        btn_size = Metrics.SMALL_BUTTON
        for row in range(rows): 
            for col in range(cols):
                if counter >= color_amount: break

                color = colors[counter]
                btn = QPushButton()
                btn.setProperty("color", f"{color}")
                btn.setFixedSize(btn_size, btn_size)
                btn.clicked.connect(
                    lambda _, c=color: self._on_click(c)
                )
                make_circle(btn, btn_size)

                layout.addWidget(btn, row, col)

                counter += 1
        
    @property
    def selection(self) -> str | None:
        return self._selection

    def _on_click(self, color: str) -> None:
        self._selection = color
        self.accept()