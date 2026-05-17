from enum import Enum, auto


DAYS = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

MONTHS: dict[int, str] = {
    1: "January", 2: "February",
    3: "March", 4: "April",
    5: "May", 6: "June",
    7: "July", 8: "August",
    9: "September", 10: "October",
    11: "November", 12: "December",
}

CALENDAR_ROWS = 5

CALENDAR_COLS = 7

UNICODE: dict[str, str] = {
    "left_arrow" : "\U0001F804",
    "right_arrow": "\U0001F806",
    "refresh": "\u21BB"
}


class FormType(Enum):
    unit = auto()
    assignment = auto()
    exam = auto()