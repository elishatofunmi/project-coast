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
        self.status = False
        self.setGeometry(0, 0, 680, 600)
        self.setMaximumSize(700,600)
        self.trigger_welcome()
        
    def trigger_welcome(self):
        self.display_background()
        self.display()
        return
        
        #self.mai = main()
        #self.mai.stacked.setCurrentWidget(self)
    


    def display_background(self):

        self.width = 700
        self.height = 600
        self.label = QLabel(self)
        self.label.resize(self.width, self.height)
        pixmap = QPixmap("final_png.PNG")
        self.pixmat = pixmap.scaled(self.width, self.height)
        self.label.setPixmap(self.pixmat)
        self.label.setGeometry(0,0,self.width,self.height)
        self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.label.setScaledContents(True)
        self.label.show()
        return


    def display(self):
        #layout.addStretch(1)
        
        #titleLabel = QLabel('WELCOME TO THE NIGERIAN ARMY SCHOOL OF SIGNALS STUDENT RECORD DATABASE')


        #layout.addWidget(titleLabel)
        #titleLabel.setAlignment(Qt.AlignHCenter)
        #titleLabel.setWordWrap(True)


        loginButton =  QPushButton('Login', self)
        loginButton.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7; padding: 16px')
        loginButton.clicked.connect(self.click_to_log_in)
        loginButton.resize(200,50)
        loginButton.move(70,290)
        #layout.addWidget(loginButton)

        self.signUpButton = QPushButton('Sign up', self)
        self.signUpButton.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7; padding: 16px')
        self.signUpButton.clicked.connect(self.click_to_sign_in)
        self.signUpButton.move(450,290)
        self.signUpButton.resize(200,50)
        #layout.addWidget(self.signUpButton)
        
   
        
        
        
        #self.setLayout(layout)
        self.show()
    
    
    
    
    def click_to_log_in(self):    #displays the name of the officer or soldier and his or her rank being searched for
        # move to the login window
        self.status = 'login'
        self.log = login()
        self.log.show()
        return
        
   
    def close_details(self):    
        #closes the window for searching for soldier or officier
        return sys.exit()
    

    def click_to_sign_in(self):
        # move to administrative sign in
        self.status = 'sign'
        self.sign = sign_in()
        self.sign.show()
        
        return
  
    
    
   
    
    
#if __name__ == '__main__':
    
#    App = QApplication(sys.argv)
#    App.setStyle('Fusion')
    
#    mai = welcome()
#    mai.show()
#    p = mai.palette()
#    p.setColor(mai.backgroundRole(), Qt.gray)
#    mai.setPalette(p)
    
#    sys.exit(App.exec())