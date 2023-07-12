import sys

from PyQt5.QtWidgets import QApplication

from src.view.home_viewer import HomeViewer

if __name__ == "__main__":
    app = QApplication([])
    w = HomeViewer()
    w.show()
    sys.exit(app.exec())
