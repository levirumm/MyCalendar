from PySide6.QtWidgets import QWidget
from app.gui.layout.ui_calendar_view import Ui_MyCalendar


class CalendarView(QWidget, Ui_MyCalendar):
    """
    View class of Calendar app which handles GUI components
    """
    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_MyCalendar()
        self._ui.setupUi(self)
        self.setWindowTitle("My Calendar")

        self.show()