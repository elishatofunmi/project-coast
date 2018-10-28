import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton




class welcome(QWidgets):
    def __init__(self):
        self.title = 'Database mill'
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500



        self.display_background()
        self.display()

    def display_background(self):
        self.setWindowTitle(self.title)


        #self.label = QLabel(self)
        #pixmap = QPixmap("data_scientist.png")
        #self.label.setGeometry(0,0,700,500)
        #self.label.setPixmap(pixmap)
        #self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        #self.label.setScaledContents(True)
        #self.label.show()

        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(self.top, self.left,self.width, self.height)


    def display(self):
        self.label_display = QLabel('Welcome to our database')
        self.label_display.setGeometry(300,200, 700, 200)



        self.click_to_continue = QPushButton('Login', self)
        self.click_to_continue.move(300, 400)
        self.click_to_continue.resize(100,50)
        self.click_to_continue.setToolTip("Login as an Administrator")
        self.click_to_continue.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_continue.connect(self.click_to_log_in)



        button = QPushButton('Sign in', self)
        button.move(500, 400)
        button.resize(100,50)
        button.setToolTip("Sign in as an administrator")
        button.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button.connect(self.click_to_sign_in)


        button1 = QPushButton('Exit', self)
        button1.setToolTip("Exit this Database Application")
        button1.move(700,400)
        button1.resize(100,50)
        button1.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button1.connect(self.exit_app)



    def click_to_log_in(self):
        # move to login window
        return


    def click_to_sign_in(self):
        # move to administrative sign in
        return

    def exit_app(self):
        # close down the application
        #sys.exit(App.exec())
        return


        







App = QApplication(sys.argv)
window = welcome()
window.show()
sys.exit(App.exec())