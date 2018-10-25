from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("My Database")
        
        # show the minimized and maximized icon
        self.showMinimized()
        self.showMaximized()
        
        #show full screen
        #self.showfullScreen()
        
        self.setNormal()
        
        self.setMinimumWidth(200)
        self.setMaximumWidth(500)
        self.setMinimumHeight(300)
        self.setMaximumHeight(600)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        label = QLabel("Hello, world!")
        layout.addWidget(label, 0,0)
        
app = QApplication(sys.argv)
screen = Window()
screen.show()


sys.exit(app.exec_())
