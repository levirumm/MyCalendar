from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from app.model.model import CalendarModel
from app.gui.typography import Typography
from app.gui.view import CalendarView


class MyCalendar(QApplication):
    """
    Main application class which initiates application 
    model, view, and controller.
    """
    def __init__(self) -> None:
        super().__init__()

        # Set dpi scale policy to fix dpi scaling issues
        self.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )

        # Determine font sizes (dpi aware)
        Typography.init()

        # Initialise calendar model
        self._model = CalendarModel()

        # Initialise calendar view displaying current month
        today = self._model.today
        first = self._model.date_of_first_cell(today)
        self._view = CalendarView(today, first)
        
        self.exec()