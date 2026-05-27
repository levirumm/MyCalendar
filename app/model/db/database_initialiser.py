import sqlite3
from pathlib import Path
from app.model.schema import FieldName as f
from app.model.schema import ItemType


DB_PATH = Path(__file__).parent / "calendar_database.db"

CREATE_CLASS_TABLE = (
    f"CREATE TABLE IF NOT EXISTS {ItemType.CLASS.value} (\n"
    f"{f.CLASS_ID.value} INTEGER PRIMARY KEY,\n"
    f"{f.TITLE.value} TEXT,\n"
    f"{f.LECTURER.value} TEXT,\n"
    f"{f.EMAIL.value} TEXT,\n"
    f"{f.HOMEPAGE.value} TEXT,\n"
    f"{f.COLOR.value} TEXT\n"
    ")"
)

CREATE_ASSIGNMENT_TABLE = (
    f"CREATE TABLE IF NOT EXISTS {ItemType.ASSIGNMENT.value} (\n"
    f"{f.ASSIGNMENT_ID.value} INTEGER PRIMARY KEY,\n"
    f"{f.CLASS_ID.value} INTEGER NOT NULL,\n"
    f"{f.TITLE.value} TEXT,\n"
    f"{f.DUE_DATE.value} TEXT,\n"
    f"{f.OPEN_DATE.value} TEXT,\n"
    f"{f.WEIGHT.value} TEXT,\n"
    f"{f.URL.value} TEXT,\n"
    f"{f.INSERTION_TIME.value} TEXT,\n"
    f"{f.COMPLETE.value} INTEGER DEFAULT 0,\n"
    f"FOREIGN KEY ({f.CLASS_ID.value}) "
    f"REFERENCES {ItemType.CLASS.value}({f.CLASS_ID.value}) "
    f"ON DELETE CASCADE\n"
    f")"
)

CREATE_EXAM_TABLE = (
    f"CREATE TABLE IF NOT EXISTS {ItemType.EXAM.value} (\n"
    f"{f.EXAM_ID.value} INTEGER PRIMARY KEY,\n"
    f"{f.CLASS_ID.value} INTEGER NOT NULL,\n"
    f"{f.TITLE.value} TEXT,\n"
    f"{f.DUE_DATE.value} TEXT,\n"
    f"{f.TIME.value} TEXT,\n"
    f"{f.WEIGHT.value} TEXT,\n"
    f"{f.LOCATION.value} TEXT,\n"
    f"{f.URL.value} TEXT,\n"
    f"{f.INSERTION_TIME.value} TEXT,\n"
    f"{f.COMPLETE.value} INTEGER DEFAULT 0,\n"
    f"FOREIGN KEY ({f.CLASS_ID.value}) "
    f"REFERENCES {ItemType.CLASS.value}({f.CLASS_ID.value}) "
    f"ON DELETE CASCADE\n"
    f")"
)

def initialise_database() -> sqlite3.Connection | None:
    """
    Creates database file if does not exist. Returns 
    false if an error occurs.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("PRAGMA foreign_keys = ON;")
        cur.execute(CREATE_CLASS_TABLE)
        cur.execute(CREATE_ASSIGNMENT_TABLE)
        cur.execute(CREATE_EXAM_TABLE)

        conn.commit()
        return conn
    except sqlite3.Error:
        return