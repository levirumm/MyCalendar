from enum import Enum, auto
from dataclasses import dataclass


class EntryType(Enum):
    """Enum for types of entries appearing on forms."""
    TEXT = auto()
    PERCENTAGE = auto()
    URL = auto()
    DATE = auto()
    TIME = auto()


@dataclass(frozen=True)
class FormRow:
    """
    Specifications for form row, including icon and 
    entry specs.
    """
    type: EntryType
    placeholder: str = ""
    not_none: bool = False


CLASS_FORM: dict[str, FormRow] = {
    "title": FormRow(
        type=EntryType.TEXT, placeholder="Add Class", 
        not_none=True
    ),
    "lecturer": FormRow(
        type=EntryType.TEXT, placeholder="Add Lecturer"
    ),
    "email": FormRow(
        type=EntryType.URL, placeholder="Add Email"
    ),
    "homepage": FormRow(
        type=EntryType.URL, placeholder="Add Homepage URL"
    )
}