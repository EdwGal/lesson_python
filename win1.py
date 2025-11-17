import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App de Edwadr Galvez G")
        button = QPushButton("hola")
        self.setFixedSize(QSize(1200,650))
        self.setCentralWidget(button)
        

app = QApplication(sys.argv)
#window1 = QWidget()
#window = QPushButton("push me")
window2 = MainWindow()
#window.show()
#window1.show()
window2.show()
app.exec()