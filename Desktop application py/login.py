import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton




class login(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'login'
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 200
        self.setMaximumSize(700,500)
        self.dict_details = {}


        self.display_background()
        self.display_login_details()
        self.read_admin_details()
        
        
    def read_admin_details(self):
        flie_open = open('admin_details.txt', 'r')
        read_data = flie_open.readlines()[0]
        data = read_data.split(',')
        flie_open.close()
   
        self.dict_details['Name'] = data[0]
        self.dict_details['Rank/Title'] = data[1]
        self.dict_details['password'] = data[2]
        self.dict_details['confirm_password'] = data[3]
        return 
    

    def display_background(self):
        self.setWindowTitle(self.title)


        self.label = QLabel(self)
        pixmap = QPixmap("data_scientist.png")
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
    
    
    def cancel(self):
        # go to initial page
        return
    
    def offi_cer(self):
        # go to officer page
        return
    
    def mem_ber(self):
        # go to mem_ber page
        return
    
    
    def confirm_details(self):
        name = self.lineedit_name.text()
        rank = self.rank_title_edit.text()
        password = self.password_me.text()
        
        
        my_name = self.dict_details['Name']
        my_rank = self.dict_details['Rank/Title'] 
        my_password = self.dict_details['password'] 
        
        if (name == my_name) & (rank == my_rank) & (password == my_password):
            solu = True
        else:
            solu = False
        return solu
    
    def close_win(self):
        return sys.exit()




if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = login()
    window.show()
    sys.exit(App.exec())