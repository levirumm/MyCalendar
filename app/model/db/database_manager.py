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
    
    def get_item_info(
            self, item_type: ItemType, item_id: int
        ) -> dict[FieldName, str]:
        """Fetches and returns item data."""
        selector = self._get_item_id_key(item_type)
        sql = self._generate_select_sql(item_type, selector)

        if not self._execute_sql(sql, (item_id,)):
            return {}
        
        return self._fieldname_dict(self._cur.fetchall()[0])
        
    def get_assessments_descriptions(self, date_str: str) -> list:
        """
        Returns a list of ItemDescriptions of assessments due
        on given date.
        """
        assessments = []
        sql = self._generate_assessment_description_sql()

        if not self._execute_sql(sql, (date_str, date_str)):
            return []
        
        for assessment in self._cur.fetchall():
            # Bundle data into a dict
            a_dict = self._fieldname_dict(assessment)
            
            # Get type of assessments
            item_type = self._get_item_type(
                a_dict[FieldName.ASSESSMENT_TYPE]
            )

            # Create item description object
            item = ItemDescription(
                item_type, int(a_dict[FieldName.ITEM_ID]), 
                a_dict[FieldName.TITLE], a_dict[FieldName.COLOR]
            )
            assessments.append(item)

        return assessments
            
    def get_class_descriptions(self) -> list[ItemDescription]:
        """Returns an ItemDescription for each class."""
        descriptions = []
        sql = self._generate_class_description_sql(ItemType.CLASS)

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
    
        return self._execute_sql(sql, values)

    def update_item(
            self, item_type: ItemType, item_id: int, data: dict
        ) -> bool:
        """Updates item in database."""
        fields, values = self._bundle_fields_and_values(data)
        sql = self._generate_update_sql(item_type, fields)
        values += (item_id,)
        
        return self._execute_sql(sql, values)
    
    def delete_item(
            self, item_type: ItemType, item_id: int
        ) -> bool:
        """Deletes item from database."""
        sql = self._generate_delete_sql(item_type)

        return self._execute_sql(sql, (item_id,))
        
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

        return self._execute_sql(sql, values)

    def _execute_sql(self, sql: str, values: tuple) -> bool: 
        """
        Tries to execute sql. Returns false if 
        sqlite3 error.
        """
        try:
            with self._conn:
                self._cur.execute(sql, values)
                return True
        except sqlite3.Error as e:
            print(e)
            return False
    
    def _generate_select_sql(
            self, item_type: ItemType, selector: FieldName
        ) -> str:
        """
        Returns the SQL for selecting item information form 
        database.
        """
        return (
            "SELECT *" + f"\nFROM {item_type.value}\n"
            f"WHERE {selector.value} = ?"
        )

    def _generate_insert_sql(
            self, fields: list[str], item_type: ItemType
        ) -> str:
        """Generates the sql required to insert item into database."""
        return (
            f"INSERT INTO {item_type.value} (\n{', '.join(fields)}\n)\n"
            f"VALUES ({','.join(['?' for _ in range(len(fields))])})"
        )
    
    def _generate_update_sql(
            self, item_type: ItemType, fields: list[FieldName]
        ) -> str:
        """
        Generates the sql required for updating an item in the 
        database.
        """
        return (
            f"UPDATE {item_type.value}\nSET\n" +
            ", ".join([f"{field} = ?" for field in fields]) +
            f"\nWHERE {self._get_item_id_key(item_type).value} = ?"
        )

    def _generate_delete_sql(self, item_type: ItemType) -> str:
        """
        Returns the sql for deleting an item from the database.
        """
        return (
            f"DELETE FROM {item_type.value}\n"
            f"WHERE {self._get_item_id_key(item_type).value} = ?"
        )

    def _generate_class_description_sql(
            self, item_type: ItemType
        ) -> str:
        """
        Returns the sql required for fetching descriptions 
        (item id, title, color).
        """
        return (
            "SELECT\n" +
            (",\n".join(
                f"{field.value}" for field in [
                self._get_item_id_key(item_type), FieldName.TITLE, 
                FieldName.COLOR
                ])) +
            f"\nFROM {item_type.value}"
            f"\nORDER BY {FieldName.CLASS_ID.value}"
        )
    
    def _generate_assessment_description_sql(self) -> str:
        """
        Returns the sql required for fetching descriptions 
        (item id, title, color).
        """
        return (
            self._generate_assessment_select(ItemType.ASSIGNMENT, "A")
            + "\nUNION ALL\n" +
            self._generate_assessment_select(ItemType.EXAM, "E")
            + f"\nORDER BY {FieldName.INSERTION_TIME.value}"
        )
        
    def _generate_assessment_select(
            self, item_type: ItemType, key: str
        ) -> str:
        """
        Generates the sql for selecting description of assessments 
        of given item from database.
        """
        return (
            "SELECT\n"
            f"'{item_type.value}' as {FieldName.ASSESSMENT_TYPE.value},\n"
            f"{key}.{self._get_item_id_key(item_type).value} "
            f"as {FieldName.ITEM_ID.value},\n"
            f"{key}.{FieldName.TITLE.value} as {FieldName.TITLE.value},\n"
            f"{key}.{FieldName.INSERTION_TIME.value} "
            f"as {FieldName.INSERTION_TIME.value},\n"
            f"C.{FieldName.COLOR.value} as {FieldName.COLOR.value}\n"
            f"FROM {item_type.value} {key}\n"
            f"JOIN {ItemType.CLASS.value} C ON "
            f"{key}.{FieldName.CLASS_ID.value} = C.{FieldName.CLASS_ID.value}\n"
            f"WHERE {key}.{FieldName.DUE_DATE.value} = ?"
        )
            
    def _fieldname_dict(self, data: list[tuple]) -> dict[FieldName, str]:
        """Returns a dict mapping FieldNames to item data."""
        return {
            FieldName(key): datum 
            for key, datum in dict(data).items()
        }

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
    
    def _get_item_id_key(self, item_type: ItemType) -> FieldName:
        """Returns the key for the id of the given item type."""
        match item_type:
            case ItemType.CLASS:
                return FieldName.CLASS_ID
            
            case ItemType.ASSIGNMENT:
                return FieldName.ASSIGNMENT_ID
            
            case ItemType.EXAM:
                return FieldName.EXAM_ID   
    
    def _get_item_type(self, assessment_type: str) -> ItemType:
        """
        Helper function which returns type of assessment from 
        assessment type key.
        """
        return (
            ItemType.ASSIGNMENT if 
            assessment_type == ItemType.ASSIGNMENT.value 
            else ItemType.EXAM
        )