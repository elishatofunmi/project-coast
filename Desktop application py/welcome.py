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
        self.title = 'NIGERIAN ARMY SCHOOL OF SIGNALS STUDENT RECORD DATABASE'
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
        
        
        self.label_display = QLabel('WELCOME TO THE NIGERIAN ARMY SCHOOL OF SIGNALS STUDENT RECORD DATABASE')
        
        #self.label_display.SetReadOnly(True)
        #self.label_display.textCursor().insertHtml('<b>WELCOME TO OUR DATABASE</b>')
        layout.addWidget(self.label_display, 1,1, 3,3)
        self.label_display.setAlignment(Qt.AlignHCenter)
        self.label_display.setWordWrap(True)
        self.label_display.show()

        
        

        self.click_to_continue = QPushButton('Login', self)
        layout.addWidget(self.click_to_continue, 3, 1, 2, 1)
        self.click_to_continue.setToolTip("Login as an Administrator")
        self.click_to_continue.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_continue.clicked.connect(self.click_to_log_in)



        button = QPushButton('Sign up', self)
        layout.addWidget(button, 3, 4,2,1)
        button.setToolTip("Sign in as an administrator")
        button.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button.clicked.connect(self.click_to_sign_in)



    def click_to_log_in(self): # displays the name of the officer or soldier and his or her rank being searched for
        # move to the login window
        # display Username
        layout = QVBoxLayout()
        self.label_name = QLabel('Name:')
        self.label_name.move(30,40)
        layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit()
        self.lineedit_name.move(30,50)
        self.lineedit_name.resize(20,20)
        self.lineedit_name.setPlaceholderText("Enter name")
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
        self.rank_title_edit.setPlaceholderText("Enter rank")
        
        
        self.click_to_login = QPushButton('continue', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(50,40)
        self.click_to_login.setToolTip("get details of name and rank")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.get_details)
        
        self.click_to_cancel = QPushButton('close', self)
        layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(20,20)
        self.click_to_cancel.move(50,50)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.close_details)
        
        
        
        self.display_label = QLabel('',self)
        layout.addWidget(self.display_label)
        self.display_label.resize(40,30)
        self.display_label.move(90,80)

        self.setLayout(layout)
        self.show()
        return
    
    def get_details(self): # get details of soldier or officier being searched from file
        
        
        return
    
    def close_details(self):# closes the window for searching for soldier or officier
        return sys.exit()
    

    def click_to_sign_in(self):
        # move to administrative sign in
        
        return







    


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
            file_open.write(self.lineedit_name.text())
            file_open.write(',')
            file_open.write(self.rank_title_edit.text())
            file_open.write(',')
            file_open.write(self.password_conf.text())
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



def read_from_file():
    solu = True
    flie_open = open('admin_details.txt', 'r')
    read_data = flie_open.readlines()                          # readfrom file
    if read_data[0]
    data = read_data.split(',')
    flie_open.close()
    if '' in data:
        solu = False
    else:
        solu = True
    return solu



def run_file():
    if read_from_file() == True:
        window = welcome()
        window.show()
        sys.exit(App.exec())
    else:
        auth_admin = Authenticate_admin()
        auth_admin.show()
        auth_admin.close()
        run_file()
    return


if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    
    
    run_file()
    
    