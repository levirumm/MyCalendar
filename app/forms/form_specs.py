from enum import Enum, auto
from dataclasses import dataclass


class FormType(Enum):
    """Enum for type of form."""
    ASSIGNMENT = auto()
    CLASS = auto()
    EXAM = auto()


class FormState(Enum):
    """Enum for state of form."""
    VIEW = auto()
    EDIT = auto()
    ADD = auto()


class EntryType(Enum):
    """Enum for types of entries appearing on forms."""
    TEXT = auto()
    SWATCH = auto()
    PERCENTAGE = auto()
    URL = auto()
    DATE = auto()
    TIME = auto()


@dataclass(frozen=True)
class FormField:
    """
    Specifications for form field of form, including 
    icon and entry specs.
    """
    type: EntryType
    placeholder: str = ""
    label: str = ""
    icon: str = ""
    required: bool = False


FORM_FIELDS: dict[FormType, dict[str, FormField]] = {
    # Specifications of all fields for each form type
    FormType.CLASS: {
        "title": FormField(
            type=EntryType.TEXT, placeholder="Add Class", 
            required=True
        ),
        "color": FormField(
            type=EntryType.SWATCH, label="Select Colour", 
            icon=":/paint_bucket", required=True
        ),
        "lecturer": FormField(
            type=EntryType.TEXT,  placeholder="Add Lecturer", 
            icon=":/person.svg"
        ),
        "email": FormField(
            type=EntryType.URL, placeholder="Add Email",
            icon=":/at.svg"
        ),
        "homepage": FormField(
            type=EntryType.URL, 
            placeholder="Add Homepage URL", icon=":/home.svg"
        )
    },

    FormType.ASSIGNMENT: {
        "title": FormField(
           type=EntryType.TEXT, placeholder="Add Assignment", 
           required=True
        ),
        "color": FormField(
            type=EntryType.SWATCH, 
            label="Select Class", icon=":/graduation_cap", required=True
        ),
        "due_date": FormField(
            type=EntryType.DATE, label="Due", 
            icon=":/alert_calendar.svg", required=True
        ),
        "weight": FormField(
            type=EntryType.PERCENTAGE, placeholder="Add Weight", 
            icon=":/percentage.svg"
        ),
        "open_date": FormField(
            type=EntryType.DATE, label="Available", icon=":/clock.svg"
        ),
        "url": FormField(
            type=EntryType.URL, placeholder="Add URL", icon=":/link.svg"
        )   
    },

    FormType.EXAM: {
        "title": FormField(
            type=EntryType.TEXT, placeholder="Add Exam", required=True
        ),
        "color": FormField(
            type=EntryType.SWATCH, label="Select Class", 
            icon=":/graduation_cap", required=True
        ),
        "due_date": FormField(
            type=EntryType.DATE, label="Due", icon=":/alert_calendar.svg", 
            required=True
        ),
        "weight": FormField(
            type=EntryType.PERCENTAGE,
            placeholder="Add Weight", icon=":/percentage.svg"
        ),
        "time": FormField(
            type=EntryType.TIME, icon=":/clock.svg", 
            label="Starts"
        ),
        "location": FormField(
            type=EntryType.TEXT, placeholder="Add Location", 
            icon=":/location_pin.svg"
        ),
        "url": FormField(
            type=EntryType.URL, placeholder="Add URL", icon=":/link.svg"
        )   
    }
}