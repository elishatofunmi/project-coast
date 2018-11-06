import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton



class admin_log(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Admin login'
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 200
        self.setMaximumSize(700,500)
        self.dict_details = {}
        self.state = False


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
        self.admin_name = QLabel('User name:')
        self.admin_name.move(30,40)
        #self.label_name.resize()
        layout.addWidget(self.admin_name)


        # display entry box for name
        self.lineedit_admin_name = QLineEdit()
        self.lineedit_admin_name.move(30,50)
        self.lineedit_admin_name.resize(20,20)
        self.lineedit_admin_name.setPlaceholderText("Enter your name")
        layout.addWidget(self.lineedit_admin_name)
        

        # display Rank/title
        self.rank_admin = QLabel('password:')
        self.rank_admin.move(40,40)
        layout.addWidget(self.rank_admin)

        # display entry box for rank or title
        self.rank_admin_edit = QLineEdit()
        self.rank_admin_edit.move(40,50)
        self.rank_admin_edit.resize(20,20)
        layout.addWidget(self.rank_admin_edit)
        self.rank_admin_edit.setPlaceholderText("Enter your password")


        self.click_to_login = QPushButton('Login', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(60,40)
        self.click_to_login.setToolTip("Login")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.log_in_admin)
        
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
    
  
    
    def log_in_admin(self):
        if self.confirm_details_admin() == True:
            # find person
            self.display_label.setText('Admin Confirmed')
            self.close_win()
            self.state = True
            
        else:
            self.display_label.setText('confirm your details')
        return 

    
    def confirm_details_admin(self):
        name = self.lineedit_admin_name.text()
        rank = self.rank_admin_edit.text()
        
        
        user_name, password = self.get_admin_details_admin()
        
        
        if (name == user_name) and (rank == password):
            solu = True
        else:
            solu = False
        
        return solu
    
    
    def get_admin_details_admin(self):
        flie_open = open('admin_details.txt', 'r')
        read_data = flie_open.readlines()[0]
        data = read_data.split(',')
        flie_open.close()
        
        return data[0],data[1]
    
    
    
    def search_person(self):
        return
    
    
    def close_win(self):
        return sys.exit()




if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = admin_log()
    window.show()
    sys.exit(App.exec())