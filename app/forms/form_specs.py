from enum import Enum, auto
from dataclasses import dataclass
from app.model.schema import ItemType, FieldName


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


@dataclass
class Result:
    """Result of validating a form."""
    valid: bool
    reason: str = ""


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


FORM_FIELDS: dict[ItemType, dict[FieldName, FormField]] = {
    # Specifications of all fields for each form type
    ItemType.CLASS: {
        FieldName.TITLE: FormField(
            type=EntryType.TEXT, placeholder="Add Class", 
            required=True
        ),
        FieldName.COLOR: FormField(
            type=EntryType.SWATCH, label="Select Colour", 
            icon=":/paint_bucket", required=True
        ),
        FieldName.LECTURER: FormField(
            type=EntryType.TEXT,  placeholder="Add Lecturer", 
            icon=":/person.svg"
        ),
        FieldName.EMAIL: FormField(
            type=EntryType.URL, placeholder="Add Email",
            icon=":/at.svg"
        ),
        FieldName.HOMEPAGE: FormField(
            type=EntryType.URL, 
            placeholder="Add Homepage URL", icon=":/home.svg"
        )
    },

    ItemType.ASSIGNMENT: {
        FieldName.TITLE: FormField(
           type=EntryType.TEXT, placeholder="Add Assignment", 
           required=True
        ),
        FieldName.COLOR: FormField(
            type=EntryType.SWATCH, 
            label="Select Class", icon=":/graduation_cap", 
            required=True
        ),
        FieldName.DUE_DATE: FormField(
            type=EntryType.DATE, label="Due", 
            icon=":/alert_calendar.svg", required=True
        ),
        FieldName.WEIGHT: FormField(
            type=EntryType.PERCENTAGE, placeholder="Add Weight", 
            icon=":/percentage.svg"
        ),
        FieldName.OPEN_DATE: FormField(
            type=EntryType.DATE, label="Available", 
            icon=":/clock.svg"
        ),
        FieldName.URL: FormField(
            type=EntryType.URL, placeholder="Add URL", 
            icon=":/link.svg"
        )   
    },

    ItemType.EXAM: {
        FieldName.TITLE: FormField(
            type=EntryType.TEXT, placeholder="Add Exam", 
            required=True
        ),
        FieldName.COLOR: FormField(
            type=EntryType.SWATCH, label="Select Class", 
            icon=":/graduation_cap", required=True
        ),
        FieldName.DUE_DATE: FormField(
            type=EntryType.DATE, label="Scheduled", 
            icon=":/alert_calendar.svg", required=True
        ),
        FieldName.WEIGHT: FormField(
            type=EntryType.PERCENTAGE,
            placeholder="Add Weight", icon=":/percentage.svg"
        ),
        FieldName.TIME: FormField(
            type=EntryType.TIME, icon=":/clock.svg", 
            label="Starts"
        ),
        FieldName.LOCATION: FormField(
            type=EntryType.TEXT, placeholder="Add Location", 
            icon=":/location_pin.svg"
        ),
        FieldName.URL: FormField(
            type=EntryType.URL, placeholder="Add URL", 
            icon=":/link.svg"
        )   
    }
}