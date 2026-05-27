from itertools import product
from datetime import datetime, date, timedelta
from app.model.schema import ItemType, ItemDescription
from app.model.constants import CALENDAR_ROWS, CALENDAR_COLS
from app.model.db.database_manager import DatabaseManager


class CalendarModel:
    """
    Calendar model containing information about dates 
    and controlling access to database.
    """
    def __init__(self) -> None:
        self._db_manager = DatabaseManager()
        self._today = datetime.today().date()

        self._db_manager.get_class_descriptions()
    
    @property
    def today(self) -> date:
        return self._today

    def refresh(self) -> None:
        """Updates current date."""
        self._today = datetime.today().date()
    
    def get_item_info(self, item_type: ItemType, item_id: int) -> dict:
        """Retrieves and returns item data from database."""
        return self._db_manager.get_item_info(item_type, item_id)
    
    def get_month_assessments(
            self, display_date: date
        ) -> list[tuple[date, list[ItemDescription]]]:
        """
        Returns list of tuples containing date and list of assessments 
        due on each day appearing on the calendar page of the 
        given display month.
        """
        month_assessments = []
        date = self.date_of_first_cell(display_date)

        for _ in product(
            range(CALENDAR_ROWS), range(CALENDAR_COLS)
        ):
            day_assessments = (
                self._db_manager.get_assessments_descriptions(
                    date.isoformat())
            )
            month_assessments.append((date, day_assessments))
            date += timedelta(1)
        return month_assessments
    
    def add_item(self, data: dict, item_type: ItemType) -> bool:
        """Adds item to database. Returns false if error."""
        if item_type == ItemType.CLASS:
            return self._db_manager.add_class(data)
        
        return self._db_manager.add_assessment(
            data, item_type, insertion_time=self._get_date_time()
        )

    def update_item(
            self, item_type: ItemType, item_id: int, data: dict
        ) -> bool:
        """Updates item in database. Returns false if error."""
        return self._db_manager.update_item(item_type, item_id, data)

    def delete_item(self, item_type: ItemType, item_id: int) -> bool:
        """Deletes item from database, returning false if error."""
        return self._db_manager.delete_item(item_type, item_id)

    def toggle_complete(
            self, item_type: ItemType, item_id: int, 
            is_complete: bool
        ) -> None:
        """
        Updates the status of an items complete parameter 
        in database.
        """
        self._db_manager.toggle_complete(item_type, item_id, is_complete)

    def is_complete(self, item_type: ItemType, item_id: int) -> bool:
        """Returns the status of the items complete parameter."""
        return self._db_manager.is_complete(item_type, item_id)

    def get_class_descriptions(self) -> list[ItemDescription]:
        return self._db_manager.get_class_descriptions()
    
    def date_of_first_cell(self, month_date: date) -> date:
        """
        Returns the date of the first cell of the calendar 
        page of month that contains given date.
        """
        first = date(month_date.year, month_date.month, 1)
        idx_first = first.weekday() # Index of weekday of first
        offset = (idx_first + 1) % 7 # Offset from sunday
        return first - timedelta(offset)

    def previous_month(self, current_date: date) -> date:
        """Returns first of previous month."""
        month = current_date.month
        year = current_date.year
        month -= 1
        if month == 0: 
            # Go to December of last year
            month = 12
            year -= 1
        return date(year, month, 1)

    def next_month(self, current_date: date) -> date:
        """Returns first of next month."""
        month = current_date.month
        year = current_date.year
        month += 1
        if month == 13: 
            # Go to January next year
            month = 1
            year += 1
        return date(year, month, 1)

    def _get_date_time(self) -> str:
        """Returns the current date and time."""
        return f"{self._today} {datetime.now().strftime("%H:%M:%S")}"