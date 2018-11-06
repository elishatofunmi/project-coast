import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton




class login(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Student login'
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 200
        self.setMaximumSize(700,500)
        self.dict_details = {}


        self.display_background()
        self.display_login_details()
    
    

    def display_background(self):
        self.setWindowTitle(self.title)


        self.label = QLabel(self)
        pixmap = QPixmap("army_details.png")
        self.label.setGeometry(0,0,self.width,self.height)
        self.label.setPixmap(pixmap)
        self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.label.setScaledContents(True)
        self.label.show()

        #self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(self.top, self.left,self.width, self.height)
        return


    def display_login_details(self):
        
        layout = QVBoxLayout()

        # display name
        self.label_name = QLabel('Service Number:')
        self.label_name.move(30,40)
        #self.label_name.resize()
        layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit()
        self.lineedit_name.move(30,50)
        self.lineedit_name.resize(20,20)
        self.lineedit_name.setPlaceholderText("Enter your name")
        layout.addWidget(self.lineedit_name)
        

        # display Rank/title
        self.rank_title = QLabel('Rank:')
        self.rank_title.move(40,40)
        layout.addWidget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit()
        self.rank_title_edit.move(40,50)
        self.rank_title_edit.resize(20,20)
        layout.addWidget(self.rank_title_edit)
        self.rank_title_edit.setPlaceholderText("Enter your Title/Rank")


        self.click_to_login = QPushButton('Login', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(60,40)
        self.click_to_login.setToolTip("Login")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.log_in)
        
        self.click_to_cancel = QPushButton('close', self)
        layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(20,20)
        self.click_to_cancel.move(60,50)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.close_win)
    
        self.display_label = QLabel('',self)
        layout.addWidget(self.display_label)
        self.display_label.resize(40,30)
        self.display_label.move(90,80)

        self.setLayout(layout)
        self.show()
        return
    
  
    
    def log_in(self):
        if self.confirm_details() == True:
            # find person
            self.display_label.setText('details taken')
            self.search_person()

        else:
            self.display_label.setText('confirm your details')
        return

    
    def confirm_details(self):
        name = self.lineedit_name.text()
        rank = self.rank_title_edit.text()
        
        
        if (name != '') and (rank != ''):
            solu = True
        else:
            solu = False
        
        return solu
    
    def search_person(self):
        return
    
    
    def close_win(self):
        return sys.exit()




if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = login()
    window.show()
    sys.exit(App.exec())