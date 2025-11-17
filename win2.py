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
    QSpinBox
)

class MainWindow(QMainWindow):
    
    # def __init__(self):
    #     super().__init__()
        
    #     self.setWindowTitle("My App")
        
        
    #     widget = QLabel("hello")
    #     font = widget.font()
    #     font.setPointSize(30)
    #     widget.setFont(font)
    #     widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
    #     widget.setPixmap(QPixmap('otje.jpg'))
    #     widget.setScaledContents(True)     
        
    #     self.setCentralWidget(widget)
        
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        # widget = QCheckBox()
        # widget.setCheckState(Qt.CheckState.Checked)
        # widget.stateChanged.connect(self.show_state)
        # self.setCentralWidget(widget)

        combo = QComboBox()
        combo.addItems(["edward","midua","leandro"])
        combo.currentIndexChanged.connect(self.index_changed)
        combo.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(combo)
        # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
        # Or: widget.setTristate(True)
    def index_changed(self, i):
         print(i)
    
    def text_changed(self, s):
         print(s)
           
    def show_state(self, s):
        print(s == Qt.CheckState.Checked.value)
        print(s) 

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()