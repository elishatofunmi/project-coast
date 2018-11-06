import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton



class Authenticate_admin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title = 'Administrative details'
        self.dict_details = {'username': None, 'password': None, 'confirm_password': None}
        self.display_login_details()
        
        
        
    def display_login_details(self):
        
        layout = QVBoxLayout()

        # display Username
        self.label_name = QLabel('Username:')
        self.label_name.move(30,40)
        layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit()
        self.lineedit_name.move(30,50)
        self.lineedit_name.resize(20,20)
        self.lineedit_name.setPlaceholderText("Enter your username")
        layout.addWidget(self.lineedit_name)
        
        # display Rank/title
        self.rank_title = QLabel('Password:')
        self.rank_title.move(40,40)
        layout.addWidget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit()
        self.rank_title_edit.move(40,50)
        self.rank_title_edit.resize(20,20)
        layout.addWidget(self.rank_title_edit)
        self.rank_title_edit.setPlaceholderText("Enter your password")
        
        
        # confirm password
        self.password_confirm = QLabel(' Confirm password:')
        self.password_confirm.move(50,40)
        layout.addWidget(self.password_confirm)


        #dispaly entrybox for confirming password
        self.password_conf = QLineEdit()
        self.password_conf.move(50,50)
        self.password_conf.resize(20,20)
        layout.addWidget(self.password_conf)
        self.password_conf.setPlaceholderText("Enter to confirm password")
        
        
        self.click_to_login = QPushButton('Save', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(60,40)
        self.click_to_login.setToolTip("save details")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.save_details)
        
        self.click_to_cancel = QPushButton('close', self)
        layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(20,20)
        self.click_to_cancel.move(60,50)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.cancel_details)
        
        
        
        self.display_label = QLabel('',self)
        layout.addWidget(self.display_label)
        self.display_label.resize(40,30)
        self.display_label.move(100,80)

        self.setLayout(layout)
        self.show()
        return
    
    
    def save_details(self):
        self.dict_details['username'] = self.lineedit_name.text()
        self.dict_details['password'] = self.rank_title_edit.text()
        self.dict_details['confirm_password'] = self.password_conf.text()
        if self.confirm_details() == True:
            self.display_label.setText('your details have been saved successfully')
            
            file_open = open('admin_details.txt', 'w')
            list_both = [self.lineedit_name.text(),',', self.rank_title_edit.text(),
                         ',',self.password_conf.text()]
            file_open.writelines(list_both)
            file_open.close()
            
        return
        
    def confirm_details(self):
        solution = False
        if self.verify_details() == False:
            if self.dict_details['password'] != self.dict_details['confirm_password']:
                self.display_label.setText('your password does not match')
                solution = False
                
            else:
                solution = True
        else:
            self.display_label.setText('Invalid entry, please enter your details')
        return solution
    
    
    
    def verify_details(self):
        return ('' in self.dict_details.values())
    
    
    
    
    def cancel_details(self):
        return sys.exit()
    
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    
    window = Authenticate_admin()
    window.show()
    p = window.palette()
    p.setColor(window.backgroundRole(), Qt.gray)
    window.setPalette(p)
 
        
    sys.exit(App.exec())