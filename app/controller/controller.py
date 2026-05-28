from app.gui.view import CalendarView
from app.model.model import CalendarModel
from app.model.schema import ItemType
from app.gui.pop_ups import ToastType
from app.model.constants import MAX_CLASSES
from app.forms.form import Form
from app.forms.form_specs import FormState, Result


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

        # Set view elements using model data
        self._update_class_list()
        self._update_to_do_list()
        self._show_display_date()
    
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

    def open_form(
            self, item_type: ItemType, item_id: int,
            list_item: object | None = None
        ) -> None:
        """
        Opens form in view state displaying information 
        of corresponding item.
        """
        data = self._model.get_item_info(item_type, item_id)

        if not data:
            self._view.show_toast(
                f"Failed to open {item_type.value} form", 
                ToastType.WARNING
            )
            return
        
        classes = self._model.get_class_descriptions()

        # Open and connect to form
        form = Form(
            self._view, item_type, classes, item_id
        )
        # Send reference to list item for complete toggling
        form.connect_to_form(self, list_item)
        form.set_fields(data)
        form.set_state(FormState.VIEW)
    
        if item_type is not ItemType.CLASS:
            # Set complete status of assessment
            is_complete = self._model.is_complete(item_type, item_id)
            form.set_complete(is_complete)

        form.open()
    
    def on_add_item(self, item_type: ItemType) -> None:
        """Opens the form allowing user to a class."""
        classes = self._model.get_class_descriptions()

        # Check if item can be added
        result = self._can_add_item(item_type, classes) 
        if not result.valid:
            self._view.show_toast(result.reason, ToastType.INFO)
            return

        # Open and connect to form
        form = Form(self._view, item_type, classes)
        form.connect_to_form(self)
        form.set_state(FormState.ADD)
        form.open()

    def add_item(
            self, data: dict, item_type: ItemType
        ) -> None:
        """
        Prompts model to add item to database and refreshes view.
        """
        if not self._model.add_item(data, item_type):
            self._view.show_toast(
                "Failed to add item to database", 
                ToastType.WARNING
            )
            return
        
        if item_type is ItemType.CLASS:
            self._update_class_list()
        else:
            self._update_calendar_grid()
            self._update_to_do_list()
        
    def delete_item(self, item_type: ItemType, item_id: int) -> None:
        """Deletes item from database and refreshed view."""
        if not self._model.delete_item(item_type, item_id):
            self._view.show_toast(
                "Failed to delete item", ToastType.WARNING
            )
            return
        
        if item_type is ItemType.CLASS:
            self._update_class_list()

        # Update regardless of item type as deleting 
        # class deletes class assessments
        self._update_calendar_grid()
        self._update_to_do_list()
    
    def edit_item(
            self, data: dict, item_type: ItemType, 
            item_id: int, form: Form
        ) -> None:
        """Updates item in database."""
        if not self._model.update_item(item_type, item_id, data):
            self._view.show_toast(
                "Failed to edit item", ToastType.WARNING
            )
            return
        
        if item_type is ItemType.CLASS:
            self._update_class_list()
        
        # Update regardless of item type as editing 
        # class effects class assessments
        self._update_calendar_grid()
        self._update_to_do_list()
        
        form.set_state(FormState.VIEW)

    def on_invalid_form(self, reason: str) -> None:
        """Displays error reason to user with a toast."""
        self._view.show_toast(reason, ToastType.ERROR)
    
    def on_complete_toggled(
            self, item_type: ItemType, item_id: int, 
            is_complete: bool, list_item
        ) -> None:
        """updates items complete status in """
        self._model.toggle_complete(item_type, item_id, is_complete)

        if list_item:
            list_item.set_complete(is_complete)

        self._update_to_do_list()
    
    def _can_add_item(
            self, item_type: ItemType, classes: list
        ) -> Result:
        """
        Returns result based on whether item of given 
        type can be added.
        """
        if item_type is ItemType.CLASS:
            if len(classes) >= MAX_CLASSES:
                return Result(False, "Maximum of four classes")
            return Result(True)
    
        if not classes:
            return Result(False, "Must add classes first")
        return Result(True)         
    
    def _show_display_date(self) -> None:
        """Updates view to show display date."""
        # Update month title and calendar grid
        self._view.update_month_title(self._display_date)
        self._update_calendar_grid()

    def _update_class_list(self) -> None:
        """
        Prompts view to update class list with new data from model.
        """
        descriptions = self._model.get_class_descriptions()
        self._view.update_class_list(descriptions)
    
    def _update_to_do_list(self) -> None:
        """
        Prompts view to update to do list with new data from model.
        """
        due_items = self._model.get_due_items()
        self._view.update_to_do_list(due_items)
    
    def _update_calendar_grid(self) -> None:
        """Prompts view to update calendar grid."""
        # Get list of assessments due on current month
        month_assessments = self._model.get_month_assessments(
            self._display_date
        )

        # Update month title and calendar grid
        self._view.update_calendar_grid(
            self._model.today, month_assessments
        )