from app.db.database_initialiser import initialise_database


class DatabaseManager:
    """
    Controls database operations including insertion, deletion, 
    and edits of records.
    """
    def __init__(self) -> None:
        self._conn = initialise_database()

        if not self._conn:
            print("Failed to access / initialise database")
            return
        
        self._cur = self._conn.cursor()