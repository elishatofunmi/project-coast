import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "DataBase mill"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        

        self.InitWindow()
        self.init_buttons()
    

    def InitWindow(self):
        self.setWindowTitle(self.title)


        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('index.jpeg'))
        self.label.setGeometry(60,50,1000,400)
        self.label.show()
        

        self.setWindowIcon(QIcon('Icon.jpeg'))
        self.setGeometry(self.top, self.left,self.width, self.height)
        self.label.show()

    def init_buttons(self):
        button = QPushButton('save', self)
        button.move(100, 400)
        button.resize(100,30)
        button.setToolTip("This buttons saves all your entries")
        
        
        button1 = QPushButton('cancel', self)
        button1.setToolTip("This button cancels whatever you might have done initially")
        button1.resize(100,30)
        button1.move(450,400)

        button2 = QPushButton('sign in', self)
        button2.setToolTip("This signs you in immediately after you login your details")
        button2.resize(100,30)
        button2.move(270,400)


#if "__name__" == "__main__":
App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())

