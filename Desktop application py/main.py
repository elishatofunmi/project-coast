import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from login import login
from sign_in import sign_in
from welcome import welcome






if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    
    well = welcome()
    well.show()
    
    
    
    
    window = sign_in()
        
    log = login()
        
    sys.exit(App.exec())
        