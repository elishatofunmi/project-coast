import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from login import login
from sign_in import sign_in




class welcome(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Welcome'
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setMaximumSize(700,500)



        self.display_background()
        self.display()

    def display_background(self):
        self.setWindowTitle(self.title)


        self.label = QLabel(self)
        pixmap = QPixmap("data_scientist.png")
        self.label.setGeometry(0,0,700,500)
        self.label.setPixmap(pixmap)
        self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.label.setScaledContents(True)
        self.label.show()


        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(self.top, self.left,self.width, self.height)


    def display(self):
        layout = QGridLayout()
        self.setLayout(layout)
        
        
        self.label_display = QLabel('Welcome to our database')
        
        #self.label_display.SetReadOnly(True)
        #self.label_display.textCursor().insertHtml('<b>WELCOME TO OUR DATABASE</b>')
        layout.addWidget(self.label_display, 3,3, 3,3)
        self.label_display.setAlignment(Qt.AlignHCenter)
        self.label_display.setWordWrap(True)
        self.label_display.show()

        
        

        self.click_to_continue = QPushButton('Login', self)
        layout.addWidget(self.click_to_continue, 4, 1, 2, 1)
        self.click_to_continue.setToolTip("Login as an Administrator")
        self.click_to_continue.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_continue.clicked.connect(self.click_to_log_in)



        button = QPushButton('Sign in', self)
        layout.addWidget(button, 4, 4,2,1)
        button.setToolTip("Sign in as an administrator")
        button.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button.clicked.connect(self.click_to_sign_in)


        button1 = QPushButton('Exit', self)
        button1.setToolTip("Exit this Database Application")
        layout.addWidget(button1, 4,7,2,1)
        button1.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button1.clicked.connect(self.exit_app)



    def click_to_log_in(self):
        # move to the login window
        log = login()
        log.show()
        return


    def click_to_sign_in(self):
        # move to administrative sign in
        sign = sign_in()
        sign.show()
        return

    def exit_app(self):
        # close down the application
        #sys.exit(App.exec())
        return


        






if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = welcome()
    window.show()
    
    
    sys.exit(App.exec())