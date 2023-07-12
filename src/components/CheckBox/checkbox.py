from typing import Optional

from PyQt5.QtWidgets import QCheckBox, QLabel, QVBoxLayout, QWidget

from ...utils.read_file import read_file


class CheckBox(QWidget):
    def __init__(
        self,
        text_label: str,
        checked: bool = True,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent=parent)

        # Components of number input
        self.label: QLabel
        self.checkbox: QCheckBox

        self.text_label = text_label
        self.checked = checked

        self.create_layout()

        style_content = read_file(__file__, "checkbox_style.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def create_layout(self):
        # Create components
        self.label = QLabel(self.text_label)
        self.checkbox = QCheckBox()
        self.checkbox.setChecked(self.checked)

        # Create layout
        self.vertical_layout = QVBoxLayout()

        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.checkbox)

        self.setLayout(self.vertical_layout)

    def get_value(self) -> bool:
        return self.checkbox.isChecked()
