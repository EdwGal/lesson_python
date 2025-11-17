import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,

)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        widget = QLabel("hola Edward Galvez")
        font = widget.font()
        font.setPointSize(40)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(widget)
        
              

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()