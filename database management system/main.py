import sys


from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout, QStackedWidget

from welcome import welcome
from admin_authetication import Authenticate_admin
from sign_in import sign_in
from login import login
from display_window import display_window


class main(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.top = 300
        self.left = 200
        self.width = 700
        self.height = 500
        self.setGeometry(self.top, self.left,self.width, self.height)
        self.initUI()
        
            
    def initUI(self):
       self.stacked = QStackedWidget()
       
       
       
       self.leftlist = QListWidget()
       self.leftlist.insertItem(0, 'authenticate_admin')
       self.leftlist.insertItem(1,'welcome')
       self.leftlist.insertItem(2,'sign up')
       self.leftlist.insertItem(3,'login page')
       self.leftlist.insertItem(4,'display_login_details')
       
       self.auth_admin = Authenticate_admin()
       self.stacked.addWidget(self.auth_admin)
       self.wel = welcome()
       self.stacked.addWidget(self.wel)
       self.sign = sign_in()
       self.stacked.addWidget(self.sign)
       self.log = login()
       self.stacked.addWidget(self.log)
       self.display = display_window()
       self.stacked.addWidget(self.display)
       
       hbox = QHBoxLayout(self)
       hbox.addWidget(self.leftlist)
       hbox.addWidget(self.stacked)

       self.setLayout(hbox)
       self.leftlist.currentRowChanged.connect(self.display)
       self.setGeometry(300, 50, 10,10)
#       self.setWindowTitle('StackedWidget demo')
       self.show()
      
      
      
       
    def display(self, i):
       self.stacked.setCurrentIndex(0)
       
       
    def welcome_page(self):
        self.stacked.setCurrentWidget(self.wel)
        if self.wel.status == 'sign':
           self.stacked.setCurrentWidget(self.sign)
           
        elif self.wel.status == 'login':
           self.stacked.setCurrentWidget(self.log)
           
           
        else:
           self.welcome_page()
           
        return True

    
    def admin(self):
       self.stacked.setCurrentWidget(self.auth_admin)
       if self.auth_admin.status == True:
          self.welcome_page()
       else:
          self.admin()
        
       return True
        
        
    def read_from_file(self):
        solu = True
        flie_open = open('admin_details.txt', 'r')
        read_data = flie_open.read()
        data = read_data
        flie_open.close()
        if data == '':
            solu = False
        else:
            solu = True
        return solu
        
        

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    
    window = main()
    window.show()
#    p = window.palette()
#    p.setColor(window.backgroundRole(), Qt.gray)
#    window.setPalette(p)
 
        
    sys.exit(App.exec())