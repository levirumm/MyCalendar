from enum import Enum, auto
from dataclasses import dataclass


class FormType(Enum):
    """Enum for type of form."""
    ASSIGNMENT = auto()
    CLASS = auto()
    EXAM = auto()


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
    key: str
    type: EntryType
    placeholder: str = ""
    label: str = ""
    icon: str = ""
    required: bool = False


FORM_SPECS: dict[FormType, list[FormField]] = {
    # Specifications of all fields for each form type
    FormType.CLASS: [
        FormField(
            key="title", type=EntryType.TEXT, placeholder="Add Class", 
            required=True
        ),
        FormField(
            key="color", type=EntryType.SWATCH, label="Select Colour", 
            icon=":/paint_bucket", required=True
        ),
        FormField(
            key="lecturer", type=EntryType.TEXT, 
            placeholder="Add Lecturer", icon=":/person.svg"
        ),
        FormField(
            key="email", type=EntryType.URL, placeholder="Add Email",
            icon=":/at.svg"
        ),
        FormField(
            key="homepage", type=EntryType.URL, 
            placeholder="Add Homepage URL", icon=":/home.svg"
        )
    ],

    FormType.ASSIGNMENT: [
        FormField(
            key="title", type=EntryType.TEXT, 
            placeholder="Add Assignment", required=True
        ),
        FormField(
            key="color", type=EntryType.SWATCH, 
            label="Select Class", icon=":/graduation_cap", required=True
        ),
        FormField(
            key="due_date", type=EntryType.DATE, label="Due", 
            icon=":/alert_calendar.svg", required=True
        ),
        FormField(
            key="weight", type=EntryType.PERCENTAGE,
            placeholder="Add Weight", icon=":/percentage.svg"
        ),
        FormField(
            key="open_date", type=EntryType.DATE,
            label="Available", icon=":/clock.svg"
        ),
        FormField(
            key="url", type=EntryType.URL, placeholder="Add URL",
            icon=":/link.svg"
        )   
    ],

    FormType.EXAM: [
        FormField(
            key="title", type=EntryType.TEXT, 
            placeholder="Add Exam", required=True
        ),
        FormField(
            key="color", type=EntryType.SWATCH, label="Select Class", 
            icon=":/graduation_cap", required=True
        ),
        FormField(
            key="due_date", type=EntryType.DATE, label="Due", 
            icon=":/alert_calendar.svg", required=True
        ),
        FormField(
            key="weight", type=EntryType.PERCENTAGE,
            placeholder="Add Weight", icon=":/percentage.svg"
        ),
        FormField(
            key="time", type=EntryType.TIME, icon=":/clock.svg", 
            label="Starts"
        ),
        FormField(
            key="location", type=EntryType.TEXT, 
            placeholder="Add Location", icon=":/location_pin.svg"
        ),
        FormField(
            key="url", type=EntryType.URL, placeholder="Add URL",
            icon=":/link.svg"
        )   
    ]
}