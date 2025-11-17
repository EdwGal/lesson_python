import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("diseños en python pqt6")

app = QApplication(sys.argv)
windows = MainWindow()
windows.show()
app.exec()