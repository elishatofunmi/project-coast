from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.QtWidgets import (QApplication, QLabel, QWidget,QVBoxLayout, QPushButton)


        
class display(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle('My Database')
        
        self.resize(500,300)
        self.setMinimumWidth(200)
        self.setMaximumWidth(500)
        self.setMinimumHeight(300)
        self.setMaximumHeight(600)
        menu = QMenuBar()
        status = QStatusBar()
        
    def load_backgroud_picture():
        return
    
    def login_with_text():
        return
   
    
    




    
class admin_dialog(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.resize(300,200)
        self.setMinimumWidth(300)
        self.setMaximumWidth(300)
        self.setMinimumHeight(200)
        self.setMaximumHeight(200)

        self.initWindow()

        # Create label and button
        label = QLabel('Name: ')
        label.resize(40,20)
        label.move(50,50)
        edit1 = QLineEdit('')
        edit1.resize(60,20)
        edit1.move(60, 50)
        

        label1 = QLabel('Rank:')
        edit2 = QLineEdit('')

        label2 = QLabel('Password: ')
        edit3 = QLineEdit('')
        button = QPushButton('done')
        button1 = QPushButton('cancel')
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(button)
        layout.addWidget(button1)

        # Apply layout to widget
        widget = QWidget()
        widget.setLayout(layout)

    def initWindow(self):
        self.label = QLabel()
        self.label.setPixmap(QPixmap('index.jpeg'))
        self.label.setGeometry(60,50,1000,400)
        self.show()


        #self.setWindowIcon(QtGui.QIcon("index.png"))
        

        
#if "__name__" == "__main__":        
app = QApplication(sys.argv)
admin = admin_dialog()
admin.show()
#screen = display()
#screen.show()
sys.exit(app.exec_())
