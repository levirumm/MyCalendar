import sqlite3
from app.model.schema import ItemType, FieldName, ItemDescription
from app.model.db.database_initialiser import initialise_database


class DatabaseManager:
    """
    Controls database operations including insertion, deletion, 
    and edits of records.
    """
    def __init__(self) -> None:
        conn = initialise_database()

        if not conn:
            print("Failed to access / initialise database")
            return
        
        self._conn: sqlite3.Connection = conn
        self._cur: sqlite3.Cursor = conn.cursor()

    def get_class_descriptions(self) -> list[ItemDescription]:
        """Returns an ItemDescription for each class."""
        descriptions = []
        sql = self._generate_class_description_sql()

        with self._conn:
            self._cur.execute(sql)
        
        for data_tuple in self._cur.fetchall():
            descriptions.append(
                ItemDescription(ItemType.CLASS, *data_tuple)
            )
        return descriptions
           
    def add_class(self, data: dict) -> bool:
        """Adds new class to database."""
        fields, values = self._bundle_fields_and_values(data)
        sql = self._generate_sql(fields, ItemType.CLASS)
        
        try:
            with self._conn:
                self._cur.execute(sql, values)
                return True
        except sqlite3.Error:
            return False
    
    def add_assessment(
            self, data: dict, assessment_type: ItemType, 
            insertion_time: str
        ) -> bool:
        """Adds item to database. Returns false if error occurs."""
        fields, values = self._bundle_fields_and_values(data)

        # Add insertion time field
        fields.append(FieldName.INSERTION_TIME.value)
        values += (insertion_time,)

        sql = self._generate_sql(fields, assessment_type)

        try:
            with self._conn:
                self._cur.execute(sql, values)
                return True
        except sqlite3.Error:
            return False
    
    def _bundle_fields_and_values(self, data: dict) -> tuple[list, tuple]:
        """
        Generates and returns list of fields and tuple of values.
        """
        fields = []
        values = ()
        for field, value in data.items():
            fields.append(field.value)
            values += (value,)
        
        return fields, values
        
    def _generate_sql(
            self, fields: list[str], item_type: ItemType
        ) -> str:
        """Generates the sql required for the given operation."""
        sql = ""
    
        # Generate sql using fields and operation
        sql += f"INSERT INTO {item_type.value} (\n{', '.join(fields)}\n)\n"
        sql += f"VALUES ({','.join(['?' for _ in range(len(fields))])})"

        return sql

    def _generate_class_description_sql(self) -> str:
        """Returns the sql required for fetching class descriptions."""
        sql = "SELECT\n"

        sql += (
            ",\n".join(f"{field.value}" for field in [
                FieldName.CLASS_ID, FieldName.TITLE, FieldName.COLOR
                ]
            )
        )
        sql += (
            f"\nFROM {ItemType.CLASS.value}"
            f"\nORDER BY {FieldName.CLASS_ID.value}"
        )
        return sql