from PySide6.QtWidgets import QApplication
from app.model.model import CalendarModel
from app.gui.view import CalendarView


class MyCalendar(QApplication):
    """
    Main application class which initiates application 
    model, view, and controller.
    """
    def __init__(self) -> None:
        super().__init__()

        self._model = CalendarModel()
        self._view = CalendarView()
        
        self.exec()