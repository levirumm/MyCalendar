from app.forms.form_view import FormView


class Form:
    def __init__(self, parent) -> None:
        self._view = FormView(parent)

        self._view.exec()