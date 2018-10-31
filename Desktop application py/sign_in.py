import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton




class sign_in(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'sign in'
        self.dict_details = {'Name': None, 'Rank/Title': None, 'Password': None, 'confirm_password': None}
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 200
        self.setMaximumSize(700,500)

        self.display_background()
        self.display_login_details()

    def display_background(self):
        self.setWindowTitle(self.title)


        self.label = QLabel(self)
        pixmap = QPixmap("data_scientist.png")
        self.label.setGeometry(0,0,self.width,self.height)
        self.label.setPixmap(pixmap)
        self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.label.setScaledContents(True)
        self.label.show()

        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(self.top, self.left,self.width, self.height)
        return


    def display_login_details(self):
        
        layout = QVBoxLayout()

        # display name
        self.label_name = QLabel('Name:')
        self.label_name.move(30,40)
        #self.label_name.resize()
        layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit()
        self.lineedit_name.move(30,50)
        self.lineedit_name.resize(20,20)
        self.lineedit_name.setPlaceholderText("Enter your name")
        layout.addWidget(self.lineedit_name)
        self.lineedit_name.returnPressed.connect(self.get_name)
        

        # display Rank/title
        self.rank_title = QLabel('Rank/Title:')
        self.rank_title.move(40,40)
        layout.addWidget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit()
        self.rank_title_edit.move(40,50)
        self.rank_title_edit.resize(20,20)
        layout.addWidget(self.rank_title_edit)
        self.rank_title_edit.setPlaceholderText("Enter your Title/Rank")
        self.rank_title_edit.returnPressed.connect(self.get_rank)


        # display password
        self.password_label = QLabel('Password:')
        self.password_label.move(50,40)
        layout.addWidget(self.password_label)

        #dispaly entrybox for passwordo
        self.password_me = QLineEdit()
        self.password_me.move(50,50)
        self.password_me.resize(20,20)
        layout.addWidget(self.password_me)
        self.password_me.setPlaceholderText("Enter your password")
        self.password_me.returnPressed.connect(self.get_password)



        # confirm password
        self.password_confirm = QLabel(' Confirm password:')
        self.password_confirm.move(60,40)
        layout.addWidget(self.password_confirm)
        self.password_me.returnPressed.connect(self.get_confirm_password)

        #dispaly entrybox for confirming password
        self.password_conf = QLineEdit()
        self.password_conf.move(60,50)
        self.password_conf.resize(20,20)
        layout.addWidget(self.password_conf)
        self.password_conf.setPlaceholderText("Enter to confirm password")
        
        
        
        self.click_to_login = QPushButton('Save', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(70,40)
        self.click_to_login.setToolTip("Save entries")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.save)


        self.click_to_login = QPushButton('Login', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(70,70)
        self.click_to_login.setToolTip("Login")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.log_in)
        
        self.click_to_cancel = QPushButton('close', self)
        layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(20,20)
        self.click_to_cancel.move(70,100)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.close_win)
        
        self.display_label = QLabel('',self)
        layout.addWidget(self.display_label)
        self.display_label.resize(40,30)
        self.display_label.move(110,80)
   
    
        self.setLayout(layout)
        self.show()
        return
       
    def log_in(self):
        if self.confirm_details() == True:
            self.display_label.setText('Access Granted')
            
            mb = QMessageBox()
            mb.setText('select Either of the bases')
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle('select detail')
            
            
            self.cancel_but = QPushButton("Cancel")
            self.cancel_but.clicked.connect(self.cancel)
            self.officer_but = QPushButton('Officier')
            self.officer_but.clicked.connect(self.offi_cer)
            self.member_but = QPushButton('Member')
            self.member_but.clicked.connect(self.mem_ber)
            
            
            mb.addButton(self.member_but, mb.YesRole)
            mb.addButton(self.officer_but, mb.NoRole)
            mb.addButton(self.cancel_but, mb.RejectRole)
            ret = mb.exec_()
            mb.show() 
        else:
            self.display_label.setText('Invalid entry, please confirm your details')
        return 
            
        return 
    def cancel(self):
        #back to initial window
        return
    
    def offi_cer(self):
        # go to officers page
        return
    
    def mem_ber(self):
        # go to members page
        return
    
    def close_win(self):
        self.dict_details = {}
        return sys.exit()
    
    
    def save(self):
        self.dict_details['Name'] = self.lineedit_name.text()
        self.dict_details['Rank/Title'] = self.rank_title_edit.text()
        self.dict_details['Password'] = self.password_me.text()
        self.dict_details['confirm_password'] = self.password_conf.text()
        if self.confirm_details() == True:
            self.display_label.setText('your details have been saved successfully')
            
            file_open = open('admin_details.txt', 'w')
            list_both = [self.lineedit_name.text(),',', self.rank_title_edit.text(),',', self.password_me.text(),
                         ',',self.password_conf.text()]
            file_open.writelines(list_both)
            file_open.close()
            
        return self.log_in


    def confirm_details(self):
        solution = False
        if self.verify_details() == False:
            if self.dict_details['Password'] != self.dict_details['confirm_password']:
                self.display_label.setText('your password does not match')
                solution = False
                
            else:
                solution = True
        else:
            self.display_label.setText('Invalid entry, please enter your details')
        return solution
    
    
    
    def verify_details(self):
        return ('' in self.dict_details.values())


    def get_name(self):
        self.dict_details['Name'] = self.lineedit_name.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return
    
    def get_rank(self):
        self.dict_details['Rank/Title'] = self.rank_title_edit.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return
    
    def get_password(self):
        self.dict_details['password'] = self.password_me.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return
    
    def get_confirm_password(self):
        self.dict_details['confirm_password'] = self.password_conf.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return

        
    

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    
    window = sign_in()
    window.show()
 
        
    sys.exit(App.exec())