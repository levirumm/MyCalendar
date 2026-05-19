from app.gui.view import CalendarView
from app.model.model import CalendarModel
from app.forms.form import Form
from app.forms.form_specs import FormType


class CalendarController:
    """
    Controller of application which handles events and 
    coordinates updates of model and view.
    """
    def __init__(
            self, model: CalendarModel, view: CalendarView
        ) -> None:
        self._view: CalendarView = view
        self._model: CalendarModel = model

        # Display date defaults to current date
        self._display_date = self._model.today

        self._view.connect_to_controller(self)
    
    def on_previous_month(self) -> None:
        """Update calendar view to display previous month."""
        self._display_date = self._model.previous_month(self._display_date)
        self._show_display_date()
    
    def on_next_month(self) -> None:
        """Update calendar view to display next month."""
        self._display_date = self._model.next_month(self._display_date)
        self._show_display_date()
    
    def on_refresh(self) -> None:
        """Prompts model to update todays date and updates view."""
        self._model.refresh()
        self._show_display_date()

    def on_today(self) -> None:
        """Updates calendar to display current month."""
        self._display_date = self._model.today
        self._show_display_date()
    
    def on_add_item(self, form_type: FormType) -> None:
        """Opens the form allowing used to add corresponding item."""
        form = Form(parent=self._view, form_type=form_type)
    
    def _show_display_date(self) -> None:
        """Updates view to show display date."""
        first_cell = self._model.date_of_first_cell(self._display_date)
        self._view.update_display_month(
            self._model.today, self._display_date, first_cell
        )