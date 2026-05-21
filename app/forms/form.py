from app.forms.form_view import FormView
from app.forms.form_specs import (
    FormType, FormState, FormField, FORM_FIELDS
)


class Form:
    """
    Form which allow users to enter, edit, and delete 
    class, assignment, and exam information.
    """
    def __init__(
            self, parent, form_type: FormType, state: FormState
        ) -> None:
        self._fields: dict[str, FormField] = FORM_FIELDS[form_type]

        self._view = FormView(
            parent, self._fields, form_type, state
        )
        self._view.connect_to_form(self)
        self._view.exec()
    
    def on_save(self) -> None:
        """
        Reads and validates form. If invalid, sends invalidForm 
        signal, else, bundles data and sends save signal.
        """
        field_data = self._view.read_entries()

        result = self._validate_fields(field_data)

    def on_color_picked(self, color: str) -> None:
        pass

    def _validate_fields(self, field_data: dict) -> bool:
        """Validates data corresponding to each field."""
        for key, datum in field_data.items():
            if not datum and self._fields[key].required:
                return False
        return True