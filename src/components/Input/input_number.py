from typing import Optional, Union

from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget

from ...utils.read_file import read_file


class InputNumber(QWidget):
    def __init__(
        self,
        text_label: str,
        number_type: type = float,
        default_value: Union[int, float] = 0,
        min: Union[int, float] = 0,
        max: Union[int, float] = 1000,
        decimals: int = 2,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent=parent)

        # Components of number input
        self.label: QLabel
        self.number_input: QLineEdit

        self.text_label = text_label
        self.number_type = number_type
        self.default_value = default_value
        self.min = min
        self.max = max
        self.decimals = decimals

        self.create_layout()

        style_content = read_file(__file__, "input_style.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def create_layout(self):
        # Create components
        self.label = QLabel(self.text_label)
        self.number_input = QLineEdit(str(self.default_value))

        if self.number_type is float:
            self.number_input.setValidator(
                QDoubleValidator(
                    self.min,
                    self.max,
                    self.decimals,
                    notation=QDoubleValidator.StandardNotation,
                )
            )
        else:
            self.number_input.setValidator(QIntValidator(self.min, self.max))

        # Create layout
        self.vertical_layout = QVBoxLayout()

        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.number_input)

        self.setLayout(self.vertical_layout)

    def get_value(self) -> Union[int, float, None]:
        num = self.number_input.text()
        try:
            return (
                float(num.replace(",", "."))
                if self.number_type is float
                else int(num)
            )
        except ValueError:
            return None

    def set_error(self):
        self.number_input.setStyleSheet("border: 1px solid #ce0606;")

    def remove_error(self):
        self.number_input.setStyleSheet("border: 1px solid #E4E3E9;")
