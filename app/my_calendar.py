from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from app.model.model import CalendarModel
from app.gui.metrics import Typography, Metrics
from app.gui.view import CalendarView
from app.controller.controller import CalendarController


class MyCalendar(QApplication):
    """
    Main application class which initiates application 
    model, view, and controller.
    """
    ICON_PATH = ":/calendar_icon.ico"

    def __init__(self) -> None:
        super().__init__()

        # Set window icon
        app_icon = QIcon(str(self.ICON_PATH))
        self.setWindowIcon(app_icon)

        # Set app metrics
        Typography.init()
        Metrics.init()

        # Initialise calendar model
        self._model = CalendarModel()

        today = self._model.today
        first = self._model.date_of_first_cell(today)

        # Initialise calendar view displaying current month
        self._view = CalendarView(today, first)

        # Initialise calendar controller
        self._controller = CalendarController(self._model, self._view)
        
        self.exec()