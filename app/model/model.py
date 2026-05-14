from app.db.database_manager import DatabaseManager


class CalendarModel:
    """
    Calendar model containing information about dates 
    and controlling access to database.
    """
    def __init__(self) -> None:
        self._db_manager = DatabaseManager()