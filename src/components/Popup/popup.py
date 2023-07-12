import os
from typing import Optional

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ...utils.get_file import get_file
from ...utils.read_file import read_file

RESOURCES_PATH = os.path.join(os.getcwd(), "resources")
logo_path = get_file(RESOURCES_PATH, "logo.svg", "icons", path_is_file=False)
success_path = get_file(
    RESOURCES_PATH, "success.svg", "icons", path_is_file=False
)
error_path = get_file(RESOURCES_PATH, "error.svg", "icons", path_is_file=False)


class Popup(QDialog):
    icon_height = 60

    def __init__(
        self,
        title: str,
        text: str,
        error: bool = False,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent=parent)

        self.title = title
        self.text = text
        self.error = error

        self.setWindowTitle("Aviso")
        self.setWindowIcon(QIcon(logo_path))
        self.create_layout()

        style_content = read_file(__file__, "popup.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def create_layout(self):
        self.icon_label = QLabel()
        if self.error:
            self.pixmap = QIcon(error_path).pixmap(self.icon_height)
        else:
            self.pixmap = QIcon(success_path).pixmap(self.icon_height)
        self.icon_label.setPixmap(self.pixmap)
        self.icon_label.setScaledContents(True)
        self.icon_label.setProperty("class", "icon")

        self.title_label = QLabel(self.title)
        self.title_label.setProperty("class", "title")

        self.text_label = QLabel(self.text)

        self.button_ok = QPushButton("Ok!")
        self.button_ok.clicked.connect(self.close)

        # Create layout
        self.header_layout = QHBoxLayout()
        self.header_layout.addWidget(self.icon_label)
        self.header_layout.addWidget(self.title_label)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addWidget(self.text_label)
        self.main_layout.addWidget(self.button_ok, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)
