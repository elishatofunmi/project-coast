import sys


from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout

from welcome import welcome
from admin_authetication import Authenticate_admin
from sign_in import sign_in



class main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        if self.read_from_file() == True:
            self.welcome_page()
        else:
            self.admin()
            
    
    def welcome_page(self):
        self.wel = welcome()
        self.wel.show()
    
    def admin(self):
        self.auth_admin = Authenticate_admin()
        self.auth_admin.show()
        
        
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
    
    mai = main()
    
    sys.exit(App.exec())