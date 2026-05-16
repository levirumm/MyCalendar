from datetime import datetime, date, timedelta
from app.model.db.database_manager import DatabaseManager


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