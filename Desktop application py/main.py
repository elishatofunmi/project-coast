from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


        
class display(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle('My Database')
        
        self.resize(500,300)
        self.setMinimumWidth(200)
        self.setMaximumWidth(500)
        self.setMinimumHeight(300)
        self.setMaximumHeight(600)
        
    def load_backgroud_picture():
        return
    
    def login_with_text():
        return
    
    
        
        
        
app = QApplication(sys.argv)
screen = display()
screen.show()


sys.exit(app.exec_())
