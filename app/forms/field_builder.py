from PySide6.QtWidgets import (
    QFrame, QTimeEdit, QLabel, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QWidget, QDateEdit, QAbstractSpinBox
)
from PySide6.QtCore import QDate
from PySide6.QtGui import QPixmap, QDoubleValidator
from typing import Callable
from app.gui.metrics import Metrics, Typography
from app.forms.form_specs import FormField, EntryType


class FieldBuilder:
    """
    Renderer for form fields composed of and icon and 
    an entry.
    """
    def __init__(self, form_layout: QVBoxLayout) -> None:
        self._form_layout = form_layout

        self._dispatcher: dict[EntryType, Callable] = {
            EntryType.TEXT: self._make_text_edit,
            EntryType.DATE: self._make_date_edit,
            EntryType.TIME: self._make_time_edit,
            EntryType.PERCENTAGE: self._make_percentage_edit,
            EntryType.URL: self._make_URL_edit
        }

    def add(self, field: FormField) -> QWidget:
        """Renders a row in a form given specifications."""
        # Container for row
        row_container = QFrame()
        padding = Metrics.COLOR_IDENTIFIER
        layout = QHBoxLayout()
        layout.setContentsMargins(0, padding, 0, 0)
        layout.setSpacing(padding)
        
        if field.icon:
            self._render_icon(field.icon, layout)

        edit = self._dispatcher[field.type](field, layout)
        edit.setFont(Typography.BASE) 

        row_container.setLayout(layout)
        self._form_layout.addWidget(row_container)

        return edit
    
    def _render_icon(
            self, icon_path: str, layout: QHBoxLayout
        ) -> None:
        """Renders icon to the left of entry."""
        icon = QLabel()
        icon_size = Metrics.COLOR_IDENTIFIER
        icon.setFixedSize(icon_size, icon_size)
        icon.setPixmap(QPixmap(icon_path))
        icon.setScaledContents(True)
        layout.addWidget(icon)

    def _make_text_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> QLineEdit:
        """Renders a QLineEdit."""
        edit = QLineEdit()
        self._configure_text_edit(edit, field, layout)
        return edit

    def _make_date_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> QDateEdit:
        """Renders a QDateEdit."""
        container, edit_layout = self._configure_labeled_edit_container()
    
        # Label and date edit (default to today)
        edit = QDateEdit()
        edit.setDate(QDate.currentDate())
        label = self._configure_labeled_spin_box(field, edit)
        
        self._configure_labeled_edit(
            edit, label, container, edit_layout, layout
        )
        return edit

    def _make_time_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> QTimeEdit:
        """Renders a QTimeEdit."""
        container, edit_layout = self._configure_labeled_edit_container()

        # Label and time edit (default to 12:00 AM)
        edit = QTimeEdit()
        label = self._configure_labeled_spin_box(field, edit)

        self._configure_labeled_edit(
            edit, label, container, edit_layout, layout
        )
        return edit
    
    def _make_percentage_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> QLineEdit:
        """
        Renders a QLineEdit with a QDoubleValidator restricting 
        the input to 0-100 and with 2dp of precision.
        """
        edit = QLineEdit()
        validator = QDoubleValidator(bottom=0, top=100, decimals=2)
        validator.setNotation( # Disallow scientific notation
            QDoubleValidator.Notation.StandardNotation
        )
        edit.setValidator(validator)
        self._configure_text_edit(edit, field, layout)
        return edit

    def _make_URL_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> "URLEdit":
        """Renders a URLEdit."""
        edit = URLEdit()
        self._configure_text_edit(edit, field, layout)
        return edit
    
    def _configure_text_edit(
            self, edit, field: FormField, layout: QHBoxLayout
        ) -> None:
        """Configure attributes common to text edits."""
        edit.setPlaceholderText(field.placeholder)
        layout.addWidget(edit)
    
    def _configure_labeled_edit_container(self) -> tuple[QFrame, QHBoxLayout]:
        """Makes QFrame to hold label and edit."""
        container = QFrame()
        edit_layout = QHBoxLayout()
        edit_layout.setSpacing(0)
        edit_layout.setContentsMargins(0, 0, 0, 0)
        return (container, edit_layout)

    def _configure_labeled_spin_box(self, field, edit) -> QLabel:
        """
        Configures attributes common to spin boxes 
        (date and time edits).
        """
        label = QLabel(field.label)
        label.setFont(Typography.BASE)
        edit.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.NoButtons
        )
        edit.setFrame(False)
        return label

    def _configure_labeled_edit(
            self, edit, label, container, edit_layout, layout
        ) -> None:
        """
        Adds label + edit widgets to edit layout, edit layout 
        to container, and container to layout.
        """
        edit_layout.addWidget(label)
        edit_layout.addWidget(edit)
        edit_layout.addStretch()
        container.setLayout(edit_layout)
        layout.addWidget(container)

    
class URLEdit(QLineEdit):
    """
    QLineEdt which, when disabled, is a clickable link.
    """
    def __init__(self) -> None:
        super().__init__()
    
    def setDisabled(self, disabled: bool) -> None:
        super().setDisabled(disabled)

        if disabled:
            self.setProperty("variant", "URL")