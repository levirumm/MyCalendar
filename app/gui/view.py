from datetime import date, timedelta
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QHBoxLayout, QLabel, QFrame,
    QPushButton, QDialog
)
from PySide6.QtCore import Qt, QObject, Signal, QSize
from app.forms.form_specs import FormType
from app.model.constants import (
    CALENDAR_ROWS, CALENDAR_COLS, DAYS, MONTHS, UNICODE
)
from app.gui.metrics import Typography, Metrics
from app.gui.palette import PALETTE
from app.gui.layout.ui_calendar_view import Ui_MyCalendar
from app.gui.layout.ui_calendar_cell import Ui_CalendarCell
from app.gui.pop_ups import EventSelect
from app.gui.utils import make_circle, anchor_window
    

class CalendarView(QWidget, Ui_MyCalendar):
    """
    View class of Calendar app which handles GUI components
    """
    STYLE_PATHS: list[Path] = [
        Path(__file__).parent / "style" / "central.qss",
    ]

    def __init__(self, today: date, date_of_first: date) -> None:
        super().__init__()
        self._ui = Ui_MyCalendar()
        self._ui.setupUi(self)
        self.setWindowTitle("My Calendar")

        # Initiate app wide styling
        self.setStyleSheet(self._load_qss()) 

        # Header bar
        self._header_bar = HeaderBar(today, self._ui)

        # Left column
        self._left_column = LeftColumn(self._ui)

        # Calendar grid
        self._grid = CalendarGrid(
            today, date_of_first, self._ui.calendar_grid_layout
        )
        self.show()
    
    def update_display_month(
            self, today: date, display_date:date, date_of_first: date
        ) -> None:
        """Updates month being displayed."""
        self._header_bar.set_month_year_label(display_date)
        self._grid.update(today, date_of_first)
    
    def connect_to_controller(self, controller):
        """Connects view slots to the controller."""
        # Header bar signals
        self._header_bar.previousMonth.connect(controller.on_previous_month)
        self._header_bar.nextMonth.connect(controller.on_next_month)
        self._header_bar.refresh.connect(controller.on_refresh)
        self._header_bar.today.connect(controller.on_today)
        self._header_bar.addItem.connect(controller.on_add_item)

        # Left column signals
        self._left_column.addClass.connect(
            lambda: controller.on_add_item(FormType.CLASS)
        )
                        
    def _load_qss(self) -> str:
        """
        Returns string joining QSS from all QSS files, inserting 
        palette values.
        """
        return "\n".join(
            Path(path).read_text(encoding="utf-8").format(**PALETTE)
            for path in self.STYLE_PATHS
        )
    

class HeaderBar(QObject):
    """
    Manages the calendars header area, including the day-of-week 
    labels, the month + year title, and the header bar icons.
    """
    previousMonth = Signal()
    nextMonth = Signal()
    refresh = Signal()
    today = Signal()
    addItem = Signal(FormType)

    def __init__(
            self, display_date: date, ui: Ui_MyCalendar
        ) -> None:
        super().__init__()
        # Reference to label as it is updated
        self._month_year_label: QLabel = ui.month_year_label

        # Set background styling and title font
        ui.header_bar_container.setProperty("role", "header_bar")
        ui.day_heading_container.setProperty("role", "day_bar")
        self._month_year_label.setFont(Typography.HEADING)

        # Render header bar elements
        self.set_month_year_label(display_date)
        self._render_day_headings(ui.day_heading_layout)
        self._render_buttons(ui)
    
    def set_month_year_label(self, display_date: date) -> None:
        """Updates the month-year label (e.g. May 2026)."""
        self._month_year_label.setText(
            f"{MONTHS[display_date.month]} {display_date.year}"
        )
    
    def _render_day_headings(self, layout: QHBoxLayout) -> None:
        """Draws the headings for the days of the week."""
        for day in DAYS:
            label = QLabel(day, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)
            label.setFont(Typography.BASE) 
            label.setProperty("variant", "white")
    
    def _render_buttons(self, ui: Ui_MyCalendar) -> None:
        """Renders the buttons in the header bar."""
        btn_size = Metrics.HEADER_BUTTON
        self._make_header_icon(ui.previous_month_button, btn_size)
        self._make_header_icon(ui.next_month_button, btn_size)
        self._make_header_icon(ui.refresh_button, btn_size)
        self._make_header_icon(ui.today_button, btn_size)
        self._make_header_icon(
            ui.add_event_button, btn_size, dark=True
        )

        # Set text for text icon buttons
        ui.previous_month_button.setText(UNICODE["left_arrow"])
        ui.next_month_button.setText(UNICODE["right_arrow"])

        # Set size of icons for image icon buttons
        icn_size = Typography.HEADING.pixelSize()
        ui.refresh_button.setIconSize(QSize(icn_size, icn_size))
        ui.today_button.setIconSize(QSize(icn_size, icn_size))
        ui.add_event_button.setIconSize(QSize(icn_size, icn_size))

        # Connect slots to header buttons
        ui.previous_month_button.clicked.connect(
            lambda: self.previousMonth.emit()
        )
        ui.next_month_button.clicked.connect(
            lambda: self.nextMonth.emit()
        )
        ui.refresh_button.clicked.connect(
            lambda: self.refresh.emit()
        )
        ui.today_button.clicked.connect(
            lambda: self.today.emit()
        )
        ui.add_event_button.clicked.connect(
            lambda: self._open_add_event_menu(ui)
        )
    
    def _make_header_icon(
            self, button: QPushButton, size: int, 
            dark: bool = False
        ) -> None:
        """Applies header icon styling to button widget."""
        button.setFont(Typography.HEADING)
        button.setProperty(
            "variant", "5_blue" if dark else "2_blue"
        )
        make_circle(button, size)
    
    def _open_add_event_menu(self, ui: Ui_MyCalendar) -> None:
        """
        Opens menu allowing user to select to add an assignment 
        or an exam.
        """
        menu = EventSelect(parent=ui.header_bar_container)
        anchor_window( # Anchor top right to add event button
            menu, anchor=ui.add_event_button, anchor_side="right"
        )
        result = menu.exec()

        if result == QDialog.DialogCode.Accepted:
            selection = menu.selection
            self.addItem.emit(selection)


class LeftColumn(QObject):
    """
    Manages the left-side column of the calendar, including 
    the list of enrolled classes and the to-do list.
    """
    addClass = Signal()

    def __init__(self, ui: Ui_MyCalendar) -> None:
        super().__init__()
        ui.left_column_container.setProperty("role", "left_column")
        ui.class_list_label.setText("Classes")
        ui.class_list_label.setFont(Typography.SUB_HEADING)
        
        btn_size = Metrics.SMALL_BUTTON
        icn_size = Metrics.DATE_LABEL_HIGHLIGHT
        ui.add_class_button.setProperty("variant", "1_blue")
        ui.add_class_button.setIconSize(QSize(icn_size, icn_size))
        make_circle(ui.add_class_button, btn_size)

        ui.add_class_button.clicked.connect(lambda: self.addClass.emit())
        

class CalendarGrid:
    """
    Manages the 5x7 grid of calendar cells.
    """
    def __init__(
            self, today: date, date_of_first: date, grid_layout: QGridLayout
        ) -> None:
        # Dict mapping dates to corresponding cell widget
        self._cells: dict[date, CalendarCell] = {}

        self._draw_cells(today, date_of_first, grid_layout)
    
    def update(self, today: date, date_of_first: date) -> None:
        """Updates calendar grid to display given date."""
        cell_date = date_of_first
        new_cells: dict[date, CalendarCell] = {}

        for prev_date, cell in self._cells.items():
            cell.update_date(cell_date)
            new_cells[cell_date] = cell

            # Clear highlight of previously highlighted day
            if prev_date == today:
                cell.set_highlight(False)

            # Highlight day label of current day
            if cell_date == today:
                cell.set_highlight(True)

            cell_date += timedelta(1)

        self._cells = new_cells # Switch to new cell map

    def _draw_cells(
            self, today: date, cell_date: date, layout: QGridLayout
        ) -> None:
        """Draws the calendar cells for the current month."""
        for row in range(CALENDAR_ROWS):
            for col in range(CALENDAR_COLS):
                cell = CalendarCell(cell_date)
                layout.addWidget(cell, row, col)

                # Highlight day label of current day
                if cell_date == today:
                    cell.set_highlight(True)

                self._cells[cell_date] = cell

                cell_date += timedelta(1)
        

class CalendarCell(QFrame, Ui_CalendarCell):
    """
    Single cell in calendar grid, including date label, 
    events, and 'see more' button.
    """
    def __init__(self, cell_date: date) -> None:
        super().__init__()
        self._ui = Ui_CalendarCell()
        self._ui.setupUi(self)

        self._render_top_elements(cell_date.day)
    
    def update_date(self, new_date: date) -> None:
        """Updates cell's date labels to match new date."""
        self._ui.date_label.setText(str(new_date.day))
        
    def set_highlight(self, highlight: bool) -> None:
        """Adds or removes highlight on date label."""
        label = self._ui.date_label
        label.setProperty("variant", "highlight" if highlight else None)
        self.style().polish(label)
    
    def _render_top_elements(self, day: int) -> None:
        """
        Renders label displaying date at top of cell and see more 
        events button. Hides see more events button.
        """
        size = Metrics.DATE_LABEL_HIGHLIGHT
        date_label = self._ui.date_label
        button = self._ui.see_more_events_button

        # Set size and shape of buttons
        for btn in [date_label, button]:
            btn.setFixedSize(size, size)
            make_circle(btn, size)

        date_label.setText(str(day))
        date_label.setFont(Typography.SMALL)

        button.setText("+")
        button.setFont(Typography.BASE)
        button.hide() # Default to hidden