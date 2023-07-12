import os
from typing import Optional

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QStackedWidget, QWidget

from ..components.SideBar.side_bar import SideBar
from ..utils.get_file import get_file
from ..utils.read_file import read_file
from .intermediate_quotas_viewer import IntermediateQuotasViewer

RESOURCES_PATH = os.path.join(os.getcwd(), "resources")
LOGO_PATH = get_file(RESOURCES_PATH, "logo.svg", "icons", path_is_file=False)


class HomeViewer(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        self.setWindowTitle("Cotas de pontos intermediários")
        self.setFixedSize(920, 600)

        self.setWindowIcon(QIcon(LOGO_PATH))

        style_content = read_file(__file__, "style.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

        self.create_layout()

    def create_layout(self):
        self.reduced_viewer = IntermediateQuotasViewer(parent=self)

        self.main_window = QStackedWidget(parent=self)
        self.main_window.addWidget(self.reduced_viewer)

        self.side_menu = SideBar(
            "Cotas de pontos intermediários",
            self.main_window.setCurrentIndex,
            parent=self,
        )

        self.side_menu.add_menu_item(
            "Calcular cotas intermediárias", "topography.svg"
        )

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.side_menu, stretch=0)
        self.layout.addWidget(self.main_window, stretch=1)

        self.setLayout(self.layout)
