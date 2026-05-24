import sqlite3
from app.model.schema import ItemType, FieldName, ItemDescription
from app.model.db.database_initialiser import initialise_database


class DatabaseManager:
    """
    Controls database operations including insertion, 
    deletion, and edits of records.
    """
    def __init__(self) -> None:
        conn = initialise_database()

        if not conn: return
        
        self._conn: sqlite3.Connection = conn
        self._conn.row_factory = sqlite3.Row
        self._cur: sqlite3.Cursor = conn.cursor()
    
    def get_item_info(self, item_type: ItemType, item_id: int) -> dict:
        """Fetches and returns item data."""
        sql = self._generate_select_sql(item_type)
        try:
            with self._conn:
                self._cur.execute(sql, (item_id,))
                return dict(self._cur.fetchall()[0])
        except sqlite3.Error:
            return {}
        
    def get_class_descriptions(self) -> list[ItemDescription]:
        """Returns an ItemDescription for each class."""
        descriptions = []
        sql = self._generate_description_sql(ItemType.CLASS)

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
        sql = self._generate_insert_sql(fields, ItemType.CLASS)
    
        return self._add_item(sql, values)
    
    def add_assessment(
            self, data: dict, assessment_type: ItemType, 
            insertion_time: str
        ) -> bool:
        """Adds item to database. Returns false if error occurs."""
        fields, values = self._bundle_fields_and_values(data)

        # Add insertion time field
        fields.append(FieldName.INSERTION_TIME.value)
        values += (insertion_time,)

        sql = self._generate_insert_sql(fields, assessment_type)

        return self._add_item(sql, values)

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

    def _add_item(self, sql: str, values: tuple) -> bool: 
        """
        Tries to add item to database. Returns false if 
        sqlite3 error.
        """
        try:
            with self._conn:
                self._cur.execute(sql, values)
                return True
        except sqlite3.Error:
            return False
    
    def _generate_select_sql(self, item_type: ItemType) -> str:
        return (
            "SELECT *" +
            f"\nFROM {item_type.value}\n"
            f"WHERE {self._get_item_id_key(item_type).value} = ?"
        )
        
    def _generate_insert_sql(
            self, fields: list[str], item_type: ItemType
        ) -> str:
        """Generates the sql required for the given operation."""
        return (
            f"INSERT INTO {item_type.value} (\n{', '.join(fields)}\n)\n"
            f"VALUES ({','.join(['?' for _ in range(len(fields))])})"
        )

    def _generate_description_sql(self, item_type: ItemType) -> str:
        """Returns the sql required for fetching class descriptions."""
        item_id_field = self._get_item_id_key(item_type)
        return (
            "SELECT\n" +
            (
            ",\n".join(
                f"{field.value}" for field in [
                item_id_field, FieldName.TITLE, FieldName.COLOR
                ])
            ) 
            + f"\nFROM {item_type.value}"
            + f"\nORDER BY {item_id_field.value}"
        )

    def _get_item_id_key(self, item_type: ItemType) -> FieldName:
        """Returns the key for the id of the given item type."""
        match item_type:
            case ItemType.CLASS:
                return FieldName.CLASS_ID
            
            case ItemType.ASSIGNMENT:
                return FieldName.ASSIGNMENT_ID
            
            case ItemType.EXAM:
                return FieldName.EXAM_ID   