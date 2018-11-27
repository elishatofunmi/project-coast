import sys


from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QWidget,QListWidget,QHBoxLayout, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout, QStackedWidget

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
        self.welcome_page()
      
      
    
       
       
    def welcome_page(self):
       self.auth_admin = Authenticate_admin()
       self.auth_admin.show()
     
       return True

    
        
        
    
        

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    
    window = main()
#    p = window.palette()
#    p.setColor(window.backgroundRole(), Qt.gray)
#    window.setPalette(p)
 
        
    sys.exit(App.exec_())