import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout

from login import login
from sign_in import sign_in




class welcome(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NIGERIAN ARMY SCHOOL OF SIGNALS STUDENT RECORD DATABASE')
        self.setGeometry(0, 0, 680, 500)
        self.setMaximumSize(700,500)
        self.display_background()
        self.display()
    


    def display_background(self):

        self.width = 700
        self.height = 500
        self.label = QLabel(self)
        self.label.resize(self.width, self.height)
        pixmap = QPixmap("army_details.png")
        self.pixmat = pixmap.scaled(self.width, self.height)
        self.label.setPixmap(self.pixmat)
        self.label.setGeometry(0,0,self.width,self.height)
        self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.label.setScaledContents(True)
        self.label.show()
        return


    def display(self):
        layout = QHBoxLayout()
        layout.addStretch(1)
        
        titleLabel = QLabel('WELCOME TO THE NIGERIAN ARMY SCHOOL OF SIGNALS STUDENT RECORD DATABASE')

        layout.addWidget(titleLabel)
        titleLabel.setAlignment(Qt.AlignHCenter)
        titleLabel.setWordWrap(True)


        loginButton =  QPushButton('Login', self)
        loginButton.setToolTip("Login as an Administrator")
        loginButton.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        loginButton.clicked.connect(self.click_to_log_in)
        layout.addWidget(loginButton)

        signUpButton = QPushButton('Sign up', self)
        signUpButton.setToolTip("Sign in as an administrator")
        signUpButton.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        signUpButton.clicked.connect(self.click_to_sign_in)
        layout.addWidget(signUpButton)
        self.setLayout(layout)
        self.show()
    
    
    
    
    def click_to_log_in(self):    #displays the name of the officer or soldier and his or her rank being searched for
        # move to the login window
        self.log = login()
        self.log.show()
        return
        
   
    def close_details(self):    
        #closes the window for searching for soldier or officier
        return sys.exit()
    

    def click_to_sign_in(self):
        # move to administrative sign in
        self.sign = sign_in()
        self.sign.show()
        
        return
  
    
    
   
    
    
if __name__ == '__main__':
    
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    
    mai = welcome()
    mai.show()
    p = mai.palette()
    p.setColor(mai.backgroundRole(), Qt.gray)
    mai.setPalette(p)
    
    sys.exit(App.exec())