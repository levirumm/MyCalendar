from datetime import date
from itertools import product
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, 
    QLabel, QFrame, QPushButton, QDialog, QSizePolicy
)
from PySide6.QtCore import Qt, QObject, Signal, QSize
from PySide6.QtGui import QFont, QMouseEvent

from app.model.constants import (
    CALENDAR_ROWS, CALENDAR_COLS, DAYS, MONTHS, 
    UNICODE
)
from app.model.schema import ItemType, ItemDescription
from app.gui.metrics import Typography, Metrics
from app.gui.palette import PALETTE
from app.gui.layout.ui_calendar_view import Ui_MyCalendar
from app.gui.layout.ui_calendar_cell import Ui_CalendarCell
from app.gui.pop_ups import EventSelect, Toast, ToastType
from app.gui.theme import load_qss
from app.gui.utils import make_circle, make_bean, anchor_window


def clear_layout(layout) -> None:
    """Deletes all items in a layout."""
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()

        if widget is not None:
            widget.deleteLater()
    

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
            self._ui.calendar_grid_layout
        )
        self.show()
    
    def update_month_title(self, display_date: date) -> None:
        """Updates month name title in header bar."""
        self._header_bar.set_month_year_label(display_date)

    def update_class_list(
            self, class_descriptions: list[ItemDescription]
        ) -> None:
        """Updates the list of classes in the left column."""
        self._left_column.update_class_list(class_descriptions)
    
    def update_to_do_list(
            self, due_items: list[ItemDescription]
        ) -> None:
        """Updates to do list in left column."""
        self._left_column.update_to_do_list(due_items)
    
    def update_calendar_grid(
            self, today: date, 
            month_assessments: list[
                tuple[date, list[ItemDescription]]
            ]
        ) -> None:
        """Updates the grid of calendar cells."""
        self._grid.update(today, month_assessments)
    
    def show_toast(
            self, message: str, toast_type: ToastType, 
            duration: int = 1200
        ) -> None:
        """Opens a toast to display message."""
        Toast(
            self._ui.header_bar_container, message, toast_type, 
            duration
        )
    
    def connect_to_controller(self, controller):
        """Connects view slots to the controller."""
        # Header bar signals
        self._header_bar.previousMonth.connect(controller.on_previous_month)
        self._header_bar.nextMonth.connect(controller.on_next_month)
        self._header_bar.refresh.connect(controller.on_refresh)
        self._header_bar.toToday.connect(controller.on_today)
        self._header_bar.addItem.connect(controller.on_add_item)

        # Left column signals
        self._left_column.class_list.addClass.connect(
            lambda: controller.on_add_item(ItemType.CLASS)
        )
        self._left_column.class_list.classClicked.connect(
            controller.open_form
        )
        self._left_column.to_do_list.assessmentClicked.connect(
            controller.open_form
        )

        # Calendar grid signals
        self._grid.assessmentClicked.connect(controller.open_form)
                          

class HeaderBar(QObject):
    """
    Manages the calendars header area, including the day-of-week 
    labels, the month + year title, and the header bar icons.
    """
    previousMonth = Signal()
    nextMonth = Signal()
    refresh = Signal()
    toToday = Signal()
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
        ui.previous_month_button.clicked.connect(self.previousMonth.emit)
        ui.next_month_button.clicked.connect(self.nextMonth.emit)
        ui.refresh_button.clicked.connect(self.refresh.emit)
        ui.today_button.clicked.connect(self.toToday.emit)
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
        self._to_do_list = ToDoList(ui)

        # Configure left column
        padding = Typography.SUB_HEADING.pixelSize()
        ui.left_column_container.setProperty(
            "role", "left_column"
        )
        ui.left_column_container.setContentsMargins(
            padding, 0, padding, 0
        )
    
    @property
    def class_list(self) -> "ClassList":
        return self._class_list

    @property
    def to_do_list(self) -> "ToDoList":
        return self._to_do_list
    
    def update_class_list(
            self, class_descriptions: list[ItemDescription]
        ) -> None:
        """Updates the list of classes in the left column."""
        self._class_list.update(class_descriptions)
    
    def update_to_do_list(
            self, due_items: list[ItemDescription]
        ) -> None:
        """Updates to do list in left column."""
        self._to_do_list.update(due_items)


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
        clear_layout(self._layout)
        
        # Add class list items
        for description in class_descriptions:
            list_item = CalendarListItem(
                description, font=Typography.BASE, 
                bg_color="light_blue"
            )
            self._layout.addWidget(list_item)

            list_item.clicked.connect(self._on_class_clicked)

        self._layout.addStretch()
    
    def _on_class_clicked(
            self, item_type: ItemType, item_id: int
        ) -> None:
        """Emits class clicked signal with type and id."""
        self.classClicked.emit(item_type, item_id)
    
    def _render_self(self, ui: Ui_MyCalendar) -> QVBoxLayout:
        """Renders the elements of the class list."""
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


class ToDoList(QObject):
    """
    Draws and manages the list of upcoming assignments 
    and exams.
    """
    assessmentClicked = Signal(ItemType, int)

    def __init__(self, ui: Ui_MyCalendar) -> None:
        super().__init__()
        self._layout = self._render_self(ui)
    
    def update(
            self, due_items: list[ItemDescription]
        ) -> None:
        """Renders CalendarListItems for each due item."""
        clear_layout(self._layout)
        
        # Add due items to to do list.
        # Use hollow color indicator
        for description in due_items:
            list_item = CalendarListItem(
                description, font=Typography.BASE, 
                bg_color="light_blue", filled=False
            )
            self._layout.addWidget(list_item)

            list_item.clicked.connect(self._on_item_clicked)

        self._layout.addStretch()
    
    def _on_item_clicked(
            self, item_type: ItemType, item_id: int
        ) -> None:
        """Emits assessment clicked signal with type and id."""
        self.assessmentClicked.emit(item_type, item_id)

    def _render_self(self, ui: Ui_MyCalendar) -> QVBoxLayout:
        """Renders elements of to do list."""
        ui.to_do_list_layout.setSpacing(
            Typography.SMALL.pixelSize() // 2
        )

        # Title label
        ui.to_do_list_label.setText("To-Do")
        ui.to_do_list_label.setFont(Typography.SUB_HEADING)

        return ui.to_do_list_layout


class CalendarGrid(QObject):
    """
    Manages the 5x7 grid of calendar cells.
    """
    assessmentClicked = Signal(ItemType, int)

    def __init__(self, grid_layout: QGridLayout) -> None:
        super().__init__()
        # Dict mapping dates to corresponding cell widget
        self._cells: dict[date | int, CalendarCell] = {}

        self._draw_cells(grid_layout)
    
    def update(
            self, today: date, month_assessments: list[
                tuple[date, list[ItemDescription]]
            ]
        ) -> None:
        """Updates calendar grid to display given month."""
        new_cells: dict[date, CalendarCell] = {}

        for i, cell in enumerate(self._cells.values()):
            new_date, assessments = month_assessments[i]
            
            cell.update_cell(new_date, assessments)
            new_cells[new_date] = cell

            # Clear highlight of previously highlighted day
            if cell.is_today:
                cell.set_today(False)

            # Highlight day label of current day
            if new_date == today:
                cell.set_today(True)

        # Switch to new cell map
        self._cells = new_cells # type: ignore
    
    def _on_assessment_clicked(
            self, item_type: ItemType, item_id: int
        ) -> None:
        """Emits class clicked signal with type and id."""
        self.assessmentClicked.emit(item_type, item_id)
    
    def _draw_cells(self, layout: QGridLayout) -> None:
        """
        Draws the calendar cells for the current month. Uses default 
        integer keys before dates have been set during update.
        """
        counter = 0
        for row, col in product(
            range(CALENDAR_ROWS), range(CALENDAR_COLS)
        ):
            cell = CalendarCell()
            layout.addWidget(cell, row, col)
            self._cells[counter] = cell
            cell.clicked.connect(self._on_assessment_clicked)

            counter += 1
        

class CalendarCell(QFrame, Ui_CalendarCell):
    """
    Single cell in calendar grid, including date label, 
    events, and 'see more' button.
    """
    MAX_ITEMS = 3
    min_height_factor = 7

    clicked = Signal(ItemType, int)

    def __init__(self) -> None:
        super().__init__()
        ui = Ui_CalendarCell()
        ui.setupUi(self)

        # Set minimum size of cells
        self.setMinimumHeight(
            self.min_height_factor 
            * (Typography.SMALL.pixelSize())
        )

        self._date_label = ui.date_label
        self._layout = ui.event_layout

        self._is_today = False

        self._render_date_label(ui.date_label)
    
    @property
    def is_today(self) -> bool:
        return self._is_today
    
    def update_cell(
            self, new_date: date, 
            assessments: list[ItemDescription]
        ) -> None:
        """
        Updates cell's date labels and assessments to match 
        new date.
        """
        # Update date label
        self._date_label.setText(str(new_date.day))
        
        clear_layout(self._layout)
        
        # Add assessment items
        for i, description in enumerate(assessments):
            if i == self.MAX_ITEMS:
                remaining = len(assessments) - self.MAX_ITEMS
                button = self._render_see_more_button(remaining)
                self._layout.addWidget(button)
                break

            list_item = CalendarListItem(
                description, font=Typography.SMALL, 
                bg_color="white", bg_dark="light_gray"
            )

            self._layout.addWidget(list_item)
            list_item.set_complete(description.complete)
            list_item.clicked.connect(self._on_clicked)
        self._layout.addStretch()
        
    def set_today(self, today: bool) -> None:
        """Adds or removes highlight on date label."""
        self._is_today = today
        label = self._date_label
        label.setProperty(
            "variant", "highlight" if today else None
        )
        self.style().polish(label)
    
    def _on_clicked(
            self, item_type: ItemType, item_id: int
        ) -> None:
        """Emits class clicked signal with type and id."""
        self.clicked.emit(item_type, item_id)
    
    def _render_date_label(self, date_label: QLabel) -> None:
        """
        Renders label displaying date at top of cell
        """
        size = Metrics.DATE_LABEL_HIGHLIGHT
        date_label.setFont(Typography.SMALL)
        make_circle(date_label, size)
    
    def _render_see_more_button(self, remaining: int) -> QPushButton:
        """
        Renders the button to see more events below last event.
        """
        button = QPushButton(f"{remaining} more")
        button.setProperty("color", "white")
        make_bean( # Bit of a doggy bit
            button, int(Typography.SMALL.pixelSize() * 1.8)
        )

        # Copy font to not alter other widgets with font
        font = QFont(Typography.SMALL)

        # Use demibold font to stand out
        font.setWeight(QFont.Weight.DemiBold)
        button.setFont(font)

        return button

       
class CalendarListItem(QFrame):
    """
    Pressable list item which opens form in view state, 
    composed of color indicator and item title label.
    """
    _height_ratio: float = 1.8
    _indicator_ratio: float = 0.8

    clicked = Signal(ItemType, int)

    def __init__(
            self, description: ItemDescription, font: QFont, 
            bg_color: str, bg_dark: str = "",
            filled: bool = True
        ) -> None:
        super().__init__()
        self._pressed = False
        self._description = description

        self._bg_color = bg_color
        self._bg_dark = bg_dark
        
        # Configure list item
        self.setProperty("color", bg_color)
        self._label = self._render_self(font, filled)

        # Set size policy of frame so long labels are elided
        self.setSizePolicy(
            QSizePolicy.Policy.Ignored, 
            QSizePolicy.Policy.Preferred
        )

        # Set cursor to be pointing hand
        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )
    
    def set_complete(self, is_complete: bool) -> None:
        """Sets a darker background color to list item."""
        if is_complete:
            self.setProperty("color", self._bg_dark)
        else:
            self.setProperty("color", self._bg_color)
        self.style().polish(self)

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
        # Set pressed to false before emitting signal. Required 
        # because any instructions after emit will be executed 
        # after form closes, and calendar list item may have been 
        # deleted
        was_pressed = self._pressed
        self._set_pressed(False)

        if was_pressed:
            self._set_pressed(False)
            self.clicked.emit(
                self._description.item_type, 
                self._description.item_id
            )

    def _set_pressed(self, pressed: bool) -> None:
        """Sets pressed flag, styling, and polishes."""
        self._pressed = pressed
        self.setProperty("pressed", pressed)
        self.style().polish(self)
    
    def _set_hover(self, hover: bool) -> None:
        """Sets hover styling and polishes."""
        self.setProperty("hover", hover)
        self.style().polish(self)

    def _render_self(
            self, font: QFont, filled: bool
        ) -> QLabel:
        """
        Renders the list item, comprising a color indicator 
        and a label.
        """
        font_size = font.pixelSize()
        item_height = int(font_size * self._height_ratio)
        indicator_height = int(font_size * self._indicator_ratio)

        self.setToolTip(self._description.title)

        # Configure list item layout
        layout = QHBoxLayout()
        padding = (item_height - indicator_height) // 2
        layout.setContentsMargins(padding, 0, padding, 0)
        layout.setSpacing(padding // 2)

        # Color indicator (left)
        color_indicator = self._render_color_indicator(
            indicator_height, filled
        )

        # Title label
        title_label = QLabel(self._description.title)
        title_label.setFont(font)
        make_bean(self, item_height)

        # Add to layout
        layout.addWidget(color_indicator)
        layout.addWidget(title_label)
        layout.addStretch()
        self.setLayout(layout)

        return title_label

    def _render_color_indicator(
            self, height: int, filled: bool
        ) -> QLabel:
        """Renders the color indicator, filled or hollow."""
        color_indicator = QLabel()

        if filled:
            color_indicator.setStyleSheet(
                f"background-color: {
                    PALETTE[self._description.color]
                };"
            )
        else:
            color_indicator.setStyleSheet(
                # Uses muted color to avoid color overload
                f"border: 2px solid {
                    PALETTE[
                        self._description.color + "_muted"
                    ]
                };"
            )
        make_circle(color_indicator, height)

        return color_indicator