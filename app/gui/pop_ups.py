from math import ceil
from enum import Enum
from datetime import date

from PySide6.QtWidgets import (
    QDialog, QGridLayout, QPushButton, QFrame, 
    QGraphicsOpacityEffect, QVBoxLayout
)
from PySide6.QtCore import QPropertyAnimation, QTimer
from PySide6.QtGui import QPixmap
from app.gui.layout.ui_event_choice import Ui_EventChoice
from app.gui.layout.ui_color_swatch import Ui_ColorSwatch
from app.gui.layout.ui_assessment_menu import Ui_AssessmentMenu
from app.gui.layout.ui_delete_menu import Ui_DeleteMenu
from app.gui.layout.ui_toast import Ui_Toast
from app.model.schema import ItemType
from app.gui.metrics import Typography, Metrics
from app.gui.utils import make_circle, make_bean, style_window


class ToastType(Enum):
    ERROR = "error"
    INFO = "info"
    WARNING = "warning"


class Toast(QFrame, Ui_Toast):
    """
    Toast which fades away after set duration.
    """
    ICON_PATHS = {
        ToastType.ERROR: ":/stop.svg",
        ToastType.INFO: ":/info.svg",
        ToastType.WARNING: ":/warning.svg"
    }

    def __init__(
            self, parent, message: str, toast_type: ToastType,
            duration
        ) -> None:
        super().__init__(parent)
        self.setupUi(self)

        # Set toast styling
        self.setProperty("variant", toast_type.value)
        self.line.setProperty("role", "line")
        self.line.setProperty("variant", toast_type.value)

        # Set icon styling
        self.icon_label.setFixedSize(
            Metrics.COLOR_IDENTIFIER, 
            Metrics.COLOR_IDENTIFIER
        )
        self.icon_label.setPixmap(
            QPixmap(self.ICON_PATHS[toast_type])
        )
        self.icon_label.setScaledContents(True)

        # Set label styling
        self.label.setText(message)
        self.label.setFont(Typography.BASE)
        self.label.setProperty("variant", toast_type.value)

        # Define fade out effect
        effect = QGraphicsOpacityEffect(self)
        effect.setOpacity(1.0)
        self.setGraphicsEffect(effect)
        self._fade = QPropertyAnimation(
            effect, b"opacity", self
        )
        self._fade.setStartValue(1)
        self._fade.setEndValue(0)
        self._fade.finished.connect(self.deleteLater)

        # Position in center of parent
        self.adjustSize()
        center = parent.rect().center()
        self.move(
            center.x() - self.width() // 2,
            center.y() - self.height() // 2
        )
        self.show()
        
        # Initiate fade after delay
        QTimer.singleShot(duration, self._fade.start)


class EventSelect(QDialog, Ui_EventChoice):
    """
    Dialog which allows user to choose to input a new 
    assignment or a new exam.
    """
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._selection = None

        self._shadow = style_window(self, self.frame)
        self.frame.setProperty("role", "menu")

        for button in [self.assignment_button, self.exam_button]:
            button.setFont(Typography.BASE)
            button.setProperty("color", "white")
            button.setProperty("role", "drop_down")
        
        self.assignment_button.clicked.connect(
            self._on_assignment_clicked
        )
        self.exam_button.clicked.connect(self._on_exam_clicked)
    
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
        self.setupUi(self)

        self._selection = None

        self._shadow = style_window(self, self.frame)
        self.frame.setProperty("role", "menu")

        self._populate_swatch(colors, self.swatch_layout)
    
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


class AssessmentMenu(QDialog, Ui_AssessmentMenu):
    """
    Dialog which presents a list of pressable calendar 
    list items if assessments on given day exceeds 
    maximum.
    """
    def __init__(self, parent, day: date) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._shadow = style_window(self, self.frame)

        # Label showing abbrv. day and date, e.g. Tue, 12
        text = f"{day.strftime("%a")}, {day.day}"
        self.date_label.setText(text)
        self.date_label.setFont(Typography.SUB_HEADING)

        self.frame.setProperty("role", "form")
    
    @property
    def menu_layout(self) -> QVBoxLayout:
        return self.assessment_layout


class DeleteMenu(QDialog, Ui_DeleteMenu):
    """
    Opens a menu warning user that deleting class will 
    delete associated assessments, and allowing user to 
    choose to delete class.
    """
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._shadow = style_window(self, self.frame)
        self.frame.setProperty("role", "menu_2")

        self.are_you_sure_label.setFont(Typography.SUB_HEADING)
        self.warning_text.setFont(Typography.BASE)
        self.warning_text.setProperty("variant", "muted")

        icn_size = Metrics.HEADER_BUTTON
        self.warning_icon.setFixedSize(icn_size, icn_size)

        self.cancel_button.setFont(Typography.BASE)
        self.delete_button.setFont(Typography.BASE)
        self.cancel_button.setProperty("color", "white")
        self.delete_button.setProperty("color", "red")
        self.delete_button.setProperty("text_color", "white")

        self.cancel_button.clicked.connect(self.reject)
        self.delete_button.clicked.connect(self.accept)