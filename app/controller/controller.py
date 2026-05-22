from app.gui.view import CalendarView
from app.model.model import CalendarModel
from app.model.schema import ItemType
from app.model.constants import MAX_CLASSES
from app.forms.form import Form
from app.forms.form_specs import FormState


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
        self._display_date = self._model.previous_month(
            self._display_date
        )
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
    
    def on_add_assessment(self, item_type: ItemType) -> None:
        """
        Opens the form allowing user to add corresponding 
        assessment.
        """
        class_descriptions = self._model.get_class_descriptions()

        if not class_descriptions:
            print("Must add classes first")
            return
        
        self._open_add_item_form(item_type, class_descriptions)
    
    def on_add_class(self) -> None:
        """Opens the form allowing user to a class."""
        class_descriptions = self._model.get_class_descriptions()

        if len(class_descriptions) >= MAX_CLASSES:
            print("Maximum of four classes")
            return 

        self._open_add_item_form(ItemType.CLASS, class_descriptions)

    def add_item(self, data: dict, item_type: ItemType) -> None:
        """Prompts model to add item to database and refreshes view."""
        if not self._model.add_item(data, item_type):
            print("Failed to add item to database")
    
    def on_invalid_form(self, reason: str) -> None:
        """Displays error reason to user with a toast."""
        print(reason)
    
    def _show_display_date(self) -> None:
        """Updates view to show display date."""
        first_cell = self._model.date_of_first_cell(self._display_date)
        self._view.update_display_month(
            self._model.today, self._display_date, first_cell
        )
    
    def _open_add_item_form(
            self, item_type: ItemType, class_descriptions
        ) -> None:
        """
        Generates dict mapping colors to class descriptions and 
        opens form in add state.
        """
        # Dict mapping class color to class description
        color_map = {
            d.color: d for d in class_descriptions
        }

        # Open and connect to form
        form = Form(
            self._view, item_type, FormState.ADD, color_map
        )
        form.connect_to_form(self)
        form.open()