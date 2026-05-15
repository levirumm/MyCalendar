from datetime import datetime, date, timedelta
from app.db.database_manager import DatabaseManager


class CalendarModel:
    """
    Calendar model containing information about dates 
    and controlling access to database.
    """
    def __init__(self) -> None:
        self._db_manager = DatabaseManager()

        self._today = datetime.today().date()
    
    @property
    def today(self) -> date:
        return self._today
    
    def date_of_first_cell(self, month_date: date) -> date:
        """
        Returns the date of the first cell of the calendar 
        page of month that contains given date.
        """
        first = date(month_date.year, month_date.month, 1)
        idx_first = first.weekday() # Index of weekday of first
        offset = (idx_first + 1) % 7 # Offset from sunday
        return first - timedelta(offset)