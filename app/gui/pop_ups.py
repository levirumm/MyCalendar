from PySide6.QtWidgets import QDialog
from app.gui.layout.ui_event_choice import Ui_EventChoice
from app.forms.form_specs import FormType
from app.gui.metrics import Typography
from app.gui.utils import style_window


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
            button.setProperty("variant", "white")
        
        ui.assignment_button.clicked.connect(
            self._on_assignment_clicked
        )
        ui.exam_button.clicked.connect(self._on_exam_clicked)
    
    @property
    def selection(self) -> FormType | None:
        return self._selection
        
    def _on_assignment_clicked(self) -> None:
        """Sets selection and closes window."""
        self._selection = FormType.ASSIGNMENT
        self.accept()

    def _on_exam_clicked(self) -> None:
        """Sets selection and closes window."""
        self._selection = FormType.EXAM
        self.accept()