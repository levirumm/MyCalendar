import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "calendar_database.db"

CREATE_CLASS_TABLE = """
CREATE TABLE IF NOT EXISTS class (
    classID INTEGER PRIMARY KEY,
    name TEXT,
    lecturer TEXT,
    lecturerEmail TEXT,
    homepage TEXT,
    color TEXT
)
"""

CREATE_ASSIGNMENT_TABLE = """
CREATE TABLE IF NOT EXISTS assignment (
    assignmentID INTEGER PRIMARY KEY,
    classID INTEGER NOT NULL,
    name TEXT,
    dueDate TEXT,
    openDate TEXT,
    weight NUMERIC,
    URL TEXT,
    insertionDateTime TEXT,
    completed INTEGER DEFAULT 0,
    FOREIGN KEY (classID) REFERENCES class(classID) ON DELETE CASCADE
)
"""

CREATE_EXAM_TABLE = """
CREATE TABLE IF NOT EXISTS exam (
    examID INTEGER PRIMARY KEY,
    classID INTEGER NOT NULL,
    name TEXT,
    dueDate TEXT,
    openTime TEXT,
    weight NUMERIC,
    location TEXT,
    URL TEXT,
    insertionDateTime TEXT,
    completed INTEGER DEFAULT 0,
    FOREIGN KEY (classID) REFERENCES class(classID) ON DELETE CASCADE
)
"""


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
    except sqlite3.Error as e:
        return