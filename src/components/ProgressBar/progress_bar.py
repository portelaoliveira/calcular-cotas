from typing import Optional

from PyQt5.QtWidgets import QProgressBar, QWidget

from ...utils.read_file import read_file


class ProgressBar(QProgressBar):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        self.setValue(0)

        style_content = read_file(__file__, "progress_bar.qss", "styles")
        if style_content:
            self.setStyleSheet(style_content)

    def set_value(self, value: int):
        self.setValue(value)

        if self.value() > 50:
            style_content = read_file(
                __file__, "progress_bar_50.qss", "styles"
            )
            if style_content:
                self.setStyleSheet(style_content)
        else:
            style_content = read_file(__file__, "progress_bar.qss", "styles")
            if style_content:
                self.setStyleSheet(style_content)
