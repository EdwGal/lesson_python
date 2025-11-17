import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mi aplicativo de layouts")
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("orange"))
        
        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(1)
        layout1.addLayout(layout2)
        
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))
               
        layout1.addLayout(layout3)
        layout1.addWidget(Color("green"))
        layout1.addWidget(Color("black"))
        
       
        
        widget = QWidget()
        widget.setLayout(layout1)
        
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
windows = MainWindow()
windows.show()
app.exec()