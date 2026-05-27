from typing import Protocol
import webbrowser
from PySide6.QtWidgets import (
    QFrame, QTimeEdit, QLabel, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QWidget, QDateEdit, QAbstractSpinBox,
    QPushButton, QDialog
)
from PySide6.QtCore import Qt, QDate, Signal, QObject, QTime
from PySide6.QtGui import QMouseEvent, QPixmap, QDoubleValidator
from typing import Callable
from app.gui.metrics import Metrics, Typography
from app.forms.form_specs import FormField, EntryType
from app.gui.pop_ups import ColorSwatch
from app.gui.utils import make_bean, anchor_window


class FormEntry(Protocol):
    """Protocol for all entries appearing on form."""
    def get(self) -> str:
        ...
    
    def set(self, data) -> None:
        ...
    
    def set_hidden(self, hidden: bool) -> None:
        ...
    
    def set_disabled(self, disabled: bool) -> None:
        ...


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
            EntryType.URL: self._make_URL_edit,
            EntryType.SWATCH: self._make_swatch
        }

    def add(self, field: FormField) -> FormEntry:
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

    def add_title(
            self, field: FormField, title_layout: QHBoxLayout
        ) -> "TextEntry":
        """Renders title entry and adds to existing title layout."""
        title_entry = TextEntry()
        title_entry.setFont(Typography.SUB_HEADING)
        title_entry.setPlaceholderText(field.placeholder)
        title_entry.setProperty("role", "title_entry")
        title_layout.addWidget(title_entry)

        return title_entry

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
        ) -> "TextEntry":
        """Renders a TextEntry."""
        edit = TextEntry()
        self._configure_text_edit(edit, field, layout)
        return edit

    def _make_date_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> "DateEntry":
        """Renders a DateEntry."""
        container, edit_layout = self._configure_labeled_edit_container()
    
        # Label and date edit (default to today)
        edit = DateEntry()
        edit.setDate(QDate.currentDate())
        label = self._configure_labeled_spin_box(field, edit)
        
        self._configure_labeled_edit(
            edit, label, container, edit_layout, layout
        )
        return edit

    def _make_time_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> "TimeEntry":
        """Renders a QTimeEdit."""
        container, edit_layout = self._configure_labeled_edit_container()

        # Label and time edit (default to 12:00 AM)
        edit = TimeEntry()
        label = self._configure_labeled_spin_box(field, edit)

        self._configure_labeled_edit(
            edit, label, container, edit_layout, layout
        )
        return edit
    
    def _make_percentage_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> "PercentageEntry":
        """
        Renders a PercentageEntry with a QDoubleValidator restricting 
        the input to 0-100 and with 2dp of precision.
        """
        edit = PercentageEntry()
        self._configure_text_edit(edit, field, layout)
        return edit

    def _make_URL_edit(
            self, field: FormField, layout: QHBoxLayout
        ) -> "URLEdit":
        """Renders a URLEdit."""
        edit = URLEdit()
        self._configure_text_edit(edit, field, layout)
        return edit
    
    def _make_swatch(
            self, field: FormField, layout: QHBoxLayout
        ) -> "SwatchButton":
        """Makes a button for selecting class/class color."""
        font_size = Typography.BASE.pixelSize()
        swatch_button = SwatchButton(field.label, layout, font_size)

        # Set spacing so button text lines up with other fields
        layout.setSpacing(Metrics.COLOR_IDENTIFIER - (font_size // 2))

        return swatch_button

    def _configure_text_edit(
            self, edit, field: FormField, layout: QHBoxLayout
        ) -> None:
        """Configure attributes common to text edits."""
        edit.setPlaceholderText(field.placeholder)
        layout.addWidget(edit)
    
    def _configure_labeled_edit_container(
            self
        ) -> tuple[QFrame, QHBoxLayout]:
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


class TextEntry(QLineEdit):
    def get(self) -> str:
        """Returns contents of entry."""
        return self.text()

    def set(self, data: str) -> None:
        """Sets the text of the entry."""
        self.setText(data)
    
    def set_hidden(self, hidden: bool) -> None:
        """Hides or shows the container of widget."""
        frame = self.parentWidget()
        if not frame: return

        frame.hide() if hidden else frame.show()

    def set_disabled(self, disabled: bool) -> None:
        """Sets the readonly state of the entry."""
        self.setReadOnly(disabled)
        self.setCursorPosition(0) # Scroll to text start


class PercentageEntry(TextEntry):
    def __init__(self) -> None:
        """Initiates TextEntry with validator."""
        super().__init__()
        validator = QDoubleValidator(
            bottom=0, top=100, decimals=2
        )
        # Disallow scientific notation
        validator.setNotation(
            QDoubleValidator.Notation.StandardNotation
        )
        self.setValidator(validator)


class DateEntry(QDateEdit):
    def get(self) -> str:
        """Return data in iso format."""
        return self.date().toString("yyyy-MM-dd")

    def set(self, date_str: str) -> None:
        """Converts iso string to QDate and sets entry."""
        date = QDate.fromString(date_str, "yyyy-MM-dd")
        self.setDate(date)
    
    def set_hidden(self, hidden: bool) -> None:
        """Hides or shows the container of widget."""
        frame = self.parentWidget()
        if not frame: return
        
        frame.hide() if hidden else frame.show()
    
    def set_disabled(self, disabled: bool) -> None:
        """Sets the readonly state of the entry."""
        self.setReadOnly(disabled)


class TimeEntry(QTimeEdit):
    def get(self) -> str:
        """Returns time string is iso format."""
        return self.time().toString("HH:mm:ss")

    def set(self, time_str: str) -> None:
        """Converts iso string to QTime and sets entry."""
        time = QTime.fromString(time_str, "HH:mm:ss")
        self.setTime(time)
    
    def set_hidden(self, hidden: bool) -> None:
        """Hides or shows the container of widget."""
        frame = self.parentWidget()
        if not frame: return
        
        frame.hide() if hidden else frame.show()
    
    def set_disabled(self, disabled: bool) -> None:
        """Sets the readonly state of the entry."""
        self.setReadOnly(disabled)


class URLEdit(TextEntry):
    """
    QLineEdt which, when disabled, is a clickable link.
    """
    def __init__(self) -> None:
        super().__init__()
        self._readonly = False
    
    def set_disabled(self, disabled: bool) -> None:
        """Sets the readonly state of the entry."""
        super().set_disabled(disabled)
        self._readonly = disabled

    def enterEvent(self, _) -> None:
        if self._readonly:
            self._set_link(True)

    def leaveEvent(self, _) -> None:
        if self._readonly:
            self._set_link(False)
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Opens link if readonly and left button press."""
        if (
            self._readonly and 
            event.button() == Qt.MouseButton.LeftButton
        ):
            webbrowser.open(self.get())   

    def _set_link(self, link: bool) -> None:
        """Sets the underline and cursor of entry."""
        # Set underline
        font = self.font()
        font.setUnderline(link)
        self.setFont(font)

        # Set cursor
        cursor = (
            Qt.CursorShape.PointingHandCursor if link 
            else Qt.CursorShape.ArrowCursor
        )
        self.setCursor(cursor)
        

class SwatchButton(QObject):
    """
    Button which opens opens color swatch when pressed. 
    Sends colorPicked signal on selection.
    """
    colorPicked = Signal(str)

    def __init__(
            self, label: str, layout: QHBoxLayout, 
            font_size: int
        ) -> None:
        super().__init__()
        self._color = ""

        # Offset by half text height
        offset = font_size // 2

        # Render button and add to layout
        self._button = QPushButton(label)
        self._button.setProperty("color", "lightest_blue")
        self._button.setStyleSheet(
            "text-align: left;"
            f"padding-left: {offset}px;"
            f"padding-right: {offset}px;"
        )
        self._button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        make_bean(self._button, Metrics.COLOR_IDENTIFIER)
        layout.addWidget(self._button)

    @property
    def button(self) -> QPushButton:
        return self._button
    
    def get(self) -> str:
        """Returns the selected color."""
        return self._color

    def set(self, color: str) -> None:
        """Sets the color attribute of the swatch."""
        self._color = color
    
    def set_text(self, label: str) -> None:
        """Sets the text of the swatch button."""
        self._button.setText(label)
    
    def set_hidden(self, hidden: bool) -> None:
        """Hides the parent frame of the swatch."""
        frame = self._button.parentWidget()
        if not frame: return
        
        frame.hide() if hidden else frame.show()
    
    def set_disabled(self, disabled: bool) -> None:
        """Sets the disabled state of the button."""
        self._button.setDisabled(disabled)
    
    def setFont(self, font) -> None:
        """Sets font of the button."""
        self._button.setFont(font)
    
    def open_swatch(
            self, parent, anchor: QWidget, colors: list[str]
        ) -> None:
        """
        Opens color swatch anchor to anchor point and emits 
        signal if color selected.
        """
        swatch = ColorSwatch(parent, colors)
        anchor_window(swatch, anchor)
        result = swatch.exec()

        # Re-evaluate hover status
        self._button.style().polish(self._button)

        if (
            result == QDialog.DialogCode.Accepted 
            and swatch.selection
        ):
            self.colorPicked.emit(swatch.selection) 