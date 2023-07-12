import os
from typing import Callable, Optional

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QWidget

from ...utils.get_file import get_file
from ...utils.read_file import read_file
from ..IconLabel.icon_label import IconLabel

RESOURCES_PATH = os.path.join(os.getcwd(), "resources")
LOGO_PATH = get_file(RESOURCES_PATH, "logo.svg", "icons", path_is_file=False)


class SideBar(QWidget):
    def __init__(
        self,
        text_title: str,
        callback: Callable,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent=parent)

        self.text_title = text_title
        self.callback = callback

        self.create_layout()

        style_content = read_file(__file__, "side_bar.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def create_layout(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.header = IconLabel(
            icon_path=LOGO_PATH,
            text=self.text_title,
            icon_height=52,
            final_stretch=False,
            parent=self,
        )
        self.header.setProperty("class", "header")

        self.listWidget = QListWidget(parent=self)
        self.listWidget.currentRowChanged.connect(self.callback)
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.layout.addWidget(self.header, 1)
        self.layout.addWidget(self.listWidget, 5)

        self.setLayout(self.layout)

    def add_menu_item(self, label: str, icon_name: str):
        icon_path = get_file(RESOURCES_PATH, icon_name, "icons", False)
        icon = QIcon(icon_path)
        item = QListWidgetItem(icon, label, self.listWidget)
        item.setSizeHint(QSize(16777215, 60))
        self.listWidget.addItem(item)
        self.listWidget.setCurrentRow(0)
