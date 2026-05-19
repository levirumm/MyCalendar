from app.forms.form_view import FormView
from app.forms.form_specs import (
    CLASS_FORM, ASSIGNMENT_FORM, EXAM_FORM
)


class Form:
    """
    Form which allow users to enter, edit, and delete 
    class, assignment, and exam information.
    """
    def __init__(self, parent) -> None:
        self._view = FormView(parent, EXAM_FORM)

        self._view.exec()