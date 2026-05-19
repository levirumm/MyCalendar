from app.forms.form_view import FormView
from app.forms.form_specs import FormType, FORM_SPECS


class Form:
    """
    Form which allow users to enter, edit, and delete 
    class, assignment, and exam information.
    """
    def __init__(self, parent, form_type: FormType) -> None:
        self._view = FormView(parent, FORM_SPECS[form_type])

        self._view.exec()