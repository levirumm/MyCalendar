from datetime import date, timedelta
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QHBoxLayout, QLabel, QFrame
)
from PySide6.QtCore import Qt
from app.model.constants import (
    CALENDAR_ROWS, CALENDAR_COLS, DAYS, MONTHS
)
from app.gui.typography import Typography
from app.gui.palette import PALETTE
from app.gui.layout.ui_calendar_view import Ui_MyCalendar
from app.gui.layout.ui_calendar_cell import Ui_CalendarCell


class CalendarView(QWidget, Ui_MyCalendar):
    """
    View class of Calendar app which handles GUI components
    """
    STYLE_PATHS: list[Path] = [
        Path(__file__).parent / "style" / "central.qss",
    ]

    def __init__(self, today: date, date_of_first: date) -> None:
        super().__init__()
        ui = Ui_MyCalendar()
        ui.setupUi(self)
        self.setWindowTitle("My Calendar")

        # Initiate app wide styling
        self.setStyleSheet(self._load_qss()) 

        self._grid = CalendarGrid(
            date_of_first, ui.day_heading_layout, 
            ui.calendar_grid_layout
        )

        ui.header_bar_container.setProperty("role", "header_bar")
        ui.left_column_container.setProperty("role", "left_column")
        ui.day_heading_container.setProperty("role", "day_bar")
        ui.class_list_label.setText("Classes")
        ui.class_list_label.setFont(Typography.BASE)

        # Header bar shit
        ui.month_year_label.setText(
            f"{MONTHS[today.month]} {today.year}"
        )
        ui.month_year_label.setFont(Typography.HEADING)

        self.show()
    
    def _load_qss(self) -> str:
        """
        Returns string joining QSS from all QSS files, inserting 
        palette values.
        """
        return "\n".join(
            Path(path).read_text(encoding="utf-8").format(**PALETTE)
            for path in self.STYLE_PATHS
        )


class CalendarGrid:
    """
    Manages the 5x7 grid of calendar cells.
    """
    def __init__(
            self, date_of_first: date,
            day_heading_layout: QHBoxLayout, 
            grid_layout: QGridLayout
        ) -> None:
        self._populate_heading_bar(day_heading_layout)
        self._draw_cells(date_of_first, grid_layout)

    def _populate_heading_bar(self, layout: QHBoxLayout) -> None:
        """Draws the labels for the days of the week."""
        for day in DAYS:
            label = QLabel(day, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)
            label.setFont(Typography.BASE) 

    def _draw_cells(self, cell_date: date, layout: QGridLayout) -> None:
        """Draws the calendar cells for the current month."""
        for row in range(CALENDAR_ROWS):
            for col in range(CALENDAR_COLS):
                cell = CalendarCell(cell_date)
                layout.addWidget(cell, row, col)
                cell_date += timedelta(1)
        

class CalendarCell(QFrame, Ui_CalendarCell):
    def __init__(self, cell_date: date) -> None:
        super().__init__()
        ui = Ui_CalendarCell()
        ui.setupUi(self)

        ui.date_label.setText(str(cell_date.day))
        ui.date_label.setFont(Typography.SMALL)
