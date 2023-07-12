import os
from typing import Iterable, Optional, Union

from PyQt5.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ...utils.read_file import read_file


class InputFile(QWidget):
    def __init__(
        self,
        text_label: str,
        text_button: str,
        is_folder: bool = True,
        is_single_file: bool = True,
        is_save: bool = False,
        file_types: Union[None, Iterable[str]] = None,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent=parent)

        # Components of file input
        self.label: QLabel
        self.label_path: QLabel
        self.action_button: QPushButton
        self.file_path: Union[str, list[str]] = ""

        self.text_label = text_label
        self.text_button = text_button
        self.is_folder = is_folder
        self.is_single_file = is_single_file
        self.is_save = is_save
        self.file_types = (
            ["*." + f.replace(".", "") for f in file_types]
            if file_types
            else None
        )

        self.create_layout()

        style_content = read_file(__file__, "input_style.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def create_layout(self):
        # Create components
        self.label = QLabel()
        self.label.setText(self.text_label)

        self.label_path = QLabel()
        self.label_path.setWordWrap(True)

        self.label_path.setProperty("class", "label_path")

        self.action_button = QPushButton(self.text_button)
        self.action_button.resize(98, 55)
        if self.is_folder:
            self.action_button.clicked.connect(self.open_folder)
        else:
            self.action_button.clicked.connect(self.open_file)

        # Create layout
        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        self.horizontal_layout.addWidget(self.label_path)
        self.horizontal_layout.addWidget(self.action_button)

        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.setLayout(self.vertical_layout)

    def open_folder(self):
        file_path = QFileDialog.getExistingDirectory(self, "Abrir diretório")

        if file_path:
            self.file_path = file_path
            self.label_path.setText(file_path)

    def open_file(self):
        if self.is_save:
            file_dialog = QFileDialog.getSaveFileName
            title_dialog = "Salvar arquivo"
        elif self.is_single_file:
            file_dialog = QFileDialog.getOpenFileName
            title_dialog = "Abrir arquivos"
        else:
            file_dialog = QFileDialog.getOpenFileNames
            title_dialog = "Abrir arquivo"

        if self.file_types:
            filters = ";;".join(self.file_types)
            file_path = file_dialog(self, title_dialog, filter=filters)[0]
        else:
            file_path = file_dialog(self, title_dialog)[0]

        if file_path:
            self.file_path = file_path
            if isinstance(file_path, str):
                self.label_path.setText(file_path)
            else:
                self.label_path.setText(
                    ", ".join(os.path.basename(f) for f in file_path)
                )

    def set_error(self):
        self.label_path.setStyleSheet("border: 1px solid #ce0606;")

    def remove_error(self):
        self.label_path.setStyleSheet("border: 1px solid #E4E3E9;")
