import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout

from intermediate_two import mediate




class welcome(QWidget):
   def __init__(self):
      super().__init__()
      self.med = mediate()
      #self.med.show()
    
    
   
    
    
#if __name__ == '__main__':
#    
#    App = QApplication(sys.argv)
#    App.setStyle('Fusion')
#    
#    mai = welcome()
#    mai.show()
#    p = mai.palette()
#    p.setColor(mai.backgroundRole(), Qt.gray)
#    mai.setPalette(p)
#    
#    sys.exit(App.exec())