from app.gui.view import CalendarView
from app.model.model import CalendarModel


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
        previous_month = self._model.previous_month(self._display_date)
        first_cell = self._model.date_of_first_cell(previous_month)

        self._view.update_display_month(
            self._model.today, previous_month, first_cell
        )

        self._display_date = previous_month
    
    def on_next_month(self) -> None:
        """Update calendar view to display next month."""
        next_month = self._model.next_month(self._display_date)
        first_cell = self._model.date_of_first_cell(next_month)
        
        self._view.update_display_month(
            self._model.today, next_month, first_cell
        )

        self._display_date = next_month