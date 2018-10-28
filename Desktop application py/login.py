import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton




class login(QWidgets):
    def __init__(self):
        self.title = 'Database mill'
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.display_background()
        self.display_login_details()

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
        return


    def display_login_details(self):
        
        layout = QVBoxLayout()

        # display name
        self.label_name = QLabel('Name:')
        self.label_name.move(30,40)
        layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit()
        self.lineedit_name.setPlaceholderText("Enter your name")
        layout.addWidget(self.lineedit,50 ,40)
        

        # display Rank/title
        self.rank_title = QLabel('Rank/Title:')
        self.rank_title.move(30,60)
        layout.add_widget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit()
        layout.addWidget(self.rank_title_edit,50 ,60)
        self.rank_title_edit.setPlaceholderText("Enter your Title/Rank")


        # display password
        self.password_label = QLabel('Password:')
        self.password_label.move(30,80)
        layout.add_widget(self.password_label)

        #dispaly entrybox for password
        self.password_me = QLineEdit()
        layout.addWidget(self.password_me,50 ,80)
        self.password_me.setPlaceholderText("Enter your password")


       

        widget = QWidget()
        widget.setLayout(layout)
        widget.show()
        return
       
        







App = QApplication(sys.argv)
window = login()
window.show()
sys.exit(App.exec())