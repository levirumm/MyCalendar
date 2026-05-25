from datetime import date, timedelta
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, 
    QLabel, QFrame, QPushButton, QDialog, QSizePolicy
)
from PySide6.QtCore import Qt, QObject, Signal, QSize
from PySide6.QtGui import QFont, QMouseEvent, QFontMetrics

from app.model.constants import (
    CALENDAR_ROWS, CALENDAR_COLS, DAYS, MONTHS, 
    UNICODE
)
from app.model.schema import ItemType, ItemDescription
from app.gui.metrics import Typography, Metrics
from app.gui.palette import PALETTE
from app.gui.layout.ui_calendar_view import Ui_MyCalendar
from app.gui.layout.ui_calendar_cell import Ui_CalendarCell
from app.gui.pop_ups import EventSelect
from app.gui.theme import load_qss
from app.gui.utils import make_circle, make_bean, anchor_window
    

class CalendarView(QWidget, Ui_MyCalendar):
    """
    View class of Calendar app which handles GUI components
    """
    STYLE_PATHS: list[Path] = [
        Path(__file__).parent / "style" / "central.qss",
        Path(__file__).parent / "style" / "forms.qss"
    ]

    def __init__(self, today: date, date_of_first: date) -> None:
        super().__init__()
        self._ui = Ui_MyCalendar()
        self._ui.setupUi(self)
        self.setWindowTitle("My Calendar")

        # Initiate app wide styling
        self.setStyleSheet(load_qss(self.STYLE_PATHS)) 

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
    
    def update_class_list(
            self, class_descriptions: list[ItemDescription]
        ) -> None:
        """Updates the list of classes in the left column."""
        self._left_column.update_class_list(class_descriptions)
    
    def connect_to_controller(self, controller):
        """Connects view slots to the controller."""
        # Header bar signals
        self._header_bar.previousMonth.connect(controller.on_previous_month)
        self._header_bar.nextMonth.connect(controller.on_next_month)
        self._header_bar.refresh.connect(controller.on_refresh)
        self._header_bar.today.connect(controller.on_today)
        self._header_bar.addItem.connect(controller.on_add_item)

        # Left column signals
        self._left_column.class_list.addClass.connect(
            lambda: controller.on_add_item(ItemType.CLASS)
        )
        self._left_column.class_list.classClicked.connect(
            controller.open_form
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
    addItem = Signal(ItemType)

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
            "color", "darkest_blue" if dark else "base_blue"
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
    def __init__(self, ui: Ui_MyCalendar) -> None:
        super().__init__()
        self._class_list = ClassList(ui)
    
    @property
    def class_list(self) -> "ClassList":
        return self._class_list
    
    def update_class_list(
            self, class_descriptions: list[ItemDescription]
        ) -> None:
        """Updates the list of classes in the left column."""
        self._class_list.update(class_descriptions)


class ClassList(QObject):
    """
    Manages the list of enrolled classes composed of 
    CalendarListItems.
    """
    addClass = Signal()
    classClicked = Signal(ItemType, int)

    def __init__(self, ui: Ui_MyCalendar) -> None:
        super().__init__()
        self._layout = self._render_self(ui)
        
    def update(
            self, class_descriptions: list[ItemDescription]
        ) -> None:
        """Renders CalendarListItems for each class."""
        # Clear layout
        while self._layout.count():
            item = self._layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()
        
        # Add class list items
        for description in class_descriptions:
            list_item = CalendarListItem(
                description, font=Typography.BASE, 
                bg_color="light_blue"
            )
            self._layout.addWidget(list_item)

            list_item.clicked.connect(self._on_class_clicked)
    
    def _on_class_clicked(
            self, item_type: ItemType, item_id: int
        ) -> None:
        """Emits class clicked signal with type and id."""
        self.classClicked.emit(item_type, item_id)
    
    def _render_self(self, ui: Ui_MyCalendar) -> QVBoxLayout:
        """Renders the elements of the class list."""
        ui.left_column_container.setProperty("role", "left_column")
        ui.class_list_layout.setSpacing(
            Typography.SMALL.pixelSize() // 2
        )

        # Title label
        ui.class_list_label.setText("Classes")
        ui.class_list_label.setFont(Typography.SUB_HEADING)
        
        # Add class button
        btn_size = Metrics.SMALL_BUTTON
        icn_size = Metrics.DATE_LABEL_HIGHLIGHT
        ui.add_class_button.setProperty("color", "light_blue")
        ui.add_class_button.setIconSize(QSize(icn_size, icn_size))
        make_circle(ui.add_class_button, btn_size)

        ui.add_class_button.clicked.connect(
            lambda: self.addClass.emit()
        )

        return ui.class_list_layout


class CalendarGrid:
    """
    Manages the 5x7 grid of calendar cells.
    """
    def __init__(
            self, today: date, date_of_first: date, 
            grid_layout: QGridLayout
        ) -> None:
        # Dict mapping dates to corresponding cell widget
        self._cells: dict[date, CalendarCell] = {}

        self._draw_cells(today, date_of_first, grid_layout)
    
    def update(self, today: date, date_of_first: date) -> None:
        """Updates calendar grid to display given date."""
        cell_date = date_of_first
        new_cells: dict[date, CalendarCell] = {}

        for cell in self._cells.values():
            cell.update_date(cell_date)
            new_cells[cell_date] = cell

            # Clear highlight of previously highlighted day
            if cell.is_today:
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

        self._is_today = False

        self._render_top_elements(cell_date.day)
    
    @property
    def is_today(self) -> bool:
        return self._is_today
    
    def update_date(self, new_date: date) -> None:
        """Updates cell's date labels to match new date."""
        self._ui.date_label.setText(str(new_date.day))
        
    def set_highlight(self, highlight: bool) -> None:
        """Adds or removes highlight on date label."""
        self._is_today = highlight
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


class CalendarListItem(QFrame):
    """
    Pressable list item which opens form in view state, 
    composed of color indicator and item title label.
    """
    _height_ratio: float = 2
    _indicator_ratio: float = 0.7

    clicked = Signal(ItemType, int)

    def __init__(
            self, description: ItemDescription, font: QFont, 
            bg_color: str
        ) -> None:
        super().__init__()
        self._pressed = False
        self._description = description
        
        # Configure list item
        self.setProperty("color", bg_color)
        self._render_self(font)

        # Set size policy of frame so long labels are elided
        self.setSizePolicy(
            QSizePolicy.Policy.Ignored, 
            QSizePolicy.Policy.Preferred
        )

    def enterEvent(self, _) -> None:
        """Enters hover state."""
        self._set_hover(True)
    
    def leaveEvent(self, _) -> None:
        """Exits hover state."""
        self._set_hover(False)

    def mousePressEvent(self, event: QMouseEvent):
        """Enters pressed state of left button click."""
        if event.button() != Qt.MouseButton.LeftButton:
            return
        self._set_pressed(True)

    def mouseMoveEvent(self, event):
        """
        Cancels press if cursor is dragged outside button.
        """
        if not self._pressed: return
        
        if not self.rect().contains(event.pos()):
            self._set_pressed(False)
            self._set_hover(False)
        
    def mouseReleaseEvent(self, _):
        """Emits clicked signal if pressed flag is True."""
        if self._pressed:
            self._set_pressed(False)
            self.clicked.emit(
                self._description.item_type, 
                self._description.item_id
            )
        self._set_pressed(False)

    def _set_pressed(self, pressed: bool) -> None:
        """Sets pressed flag, styling, and polishes."""
        self._pressed = pressed
        self.setProperty("pressed", pressed)
        self.style().polish(self)
    
    def _set_hover(self, hover: bool) -> None:
        """Sets hover styling and polishes."""
        self.setProperty("hover", hover)
        self.style().polish(self)

    def _render_self(self, font: QFont) -> None:
        """
        Renders the list item, comprising a color indicator 
        and a label.
        """
        font_size = font.pixelSize()
        item_height = int(font_size * self._height_ratio)
        indicator_height = int(font_size * self._indicator_ratio)

        self.setToolTip(self._description.title)

        layout = QHBoxLayout()
        layout.setContentsMargins(
            indicator_height, 0, indicator_height, 0
        )

        # Color indicator (left)
        color_indicator = QLabel()
        color_indicator.setStyleSheet(
            f"background-color: {PALETTE[self._description.color]};"
        )
        make_circle(color_indicator, indicator_height)

        # Title label
        title_label = QLabel(self._description.title)
        title_label.setFont(font)
        make_bean(self, item_height)

        # Add to layout
        layout.addWidget(color_indicator)
        layout.addWidget(title_label)
        layout.addStretch()
        self.setLayout(layout)