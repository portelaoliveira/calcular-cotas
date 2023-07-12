from typing import Callable

from PyQt5.QtWidgets import QApplication, QPushButton

from ...utils.read_file import read_file


class Button(QPushButton):
    def __init__(self, text: str, callback: Callable, parent=None):
        super().__init__(text=text, parent=parent)

        self.clicked.connect(callback)

        style_content = read_file(__file__, "button_style.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def update_text(self, new_text: str):
        self.setText(new_text)
        QApplication.instance().processEvents()
