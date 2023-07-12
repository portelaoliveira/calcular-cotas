from PyQt5.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from ...utils.read_file import read_file


class DropDown(QWidget):
    def __init__(self, text_label: str, items: list, parent=None):
        super().__init__(parent=parent)

        # Components of file input
        self.label: QLabel
        self.dropdown: QComboBox

        self.text_label = text_label
        self._parent = parent
        self._items = items

        self.create_layout()

        style_content = read_file(__file__, "dropdown_style.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def create_layout(self):
        # Create components
        self.label = QLabel()
        self.label.setText(self.text_label)

        self.dropdown = QComboBox()
        self.dropdown.resize(98, 55)
        self.dropdown.addItems(self._items)

        # Create layout
        self.vertical_layout = QVBoxLayout()

        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.dropdown)

        self.setLayout(self.vertical_layout)

    def get_value(self) -> str:
        return self.dropdown.currentText()
