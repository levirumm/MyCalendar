from enum import Enum
from dataclasses import dataclass


class ItemType(Enum):
    """Enum for types of items."""
    ASSIGNMENT = "assignment"
    CLASS = "class"
    EXAM = "exam"


class FieldName(Enum):
    """
    Enum for names of fields, used by db initialiser and 
    in form specs.
    """
    ITEM_ID = "item_id"
    CLASS_ID = "class_id"
    ASSIGNMENT_ID = "assignment_id"
    EXAM_ID = "exam_id"
    TITLE = "title"
    COLOR = "color"
    LECTURER = "lecturer"
    EMAIL = "email"
    HOMEPAGE = "homepage"
    DUE_DATE = "due_date"
    OPEN_DATE = "open_date"
    WEIGHT = "weight"
    URL = "url"
    COMPLETE = "complete"
    LOCATION = "location"
    TIME = "time"
    INSERTION_TIME = "insertion_time"
    ASSESSMENT_TYPE = "assessment_type"


@dataclass
class ItemDescription:
    """Data describing an item."""
    item_type: ItemType
    item_id: int
    title: str
    color: str