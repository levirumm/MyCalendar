from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from app.model.model import CalendarModel
from app.gui.metrics import Typography, Metrics
from app.gui.view import CalendarView
from app.controller.controller import CalendarController


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

        # Determine app metrics (dpi aware)
        Typography.init()
        Metrics.init()

        # Initialise calendar model
        self._model = CalendarModel()

        # Initialise calendar view displaying current month
        today = self._model.today
        first = self._model.date_of_first_cell(today)
        self._view = CalendarView(today, first)

        # Initialise calendar controller
        self._controller = CalendarController(self._model, self._view)
        
        self.exec()