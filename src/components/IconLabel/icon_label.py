from typing import Optional

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget


class IconLabel(QWidget):
    def __init__(
        self,
        icon_path: str,
        text: str,
        icon_height: int = 16,
        final_stretch: bool = True,
        text_align: Qt.AlignmentFlag = Qt.AlignCenter,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent=parent)

        self.icon_path = icon_path
        self.text = text
        self.icon_height = icon_height
        self.final_stretch = final_stretch
        self.text_align = text_align

        self.create_layout()

    def create_layout(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        icon = QIcon(self.icon_path).pixmap(self.icon_height)

        icon_label = QLabel(parent=self)
        icon_label.setPixmap(icon)
        icon_label.setAlignment(Qt.AlignCenter)

        text_label = QLabel(self.text, parent=self)
        text_label.setAlignment(self.text_align)
        text_label.setWordWrap(True)

        layout.addWidget(icon_label, 1)
        layout.addWidget(text_label, 3)

        if self.final_stretch:
            layout.addStretch()
