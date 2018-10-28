import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton




class main_window(QWidgets):
    def __init__(self):
        







App = QApplication(sys.argv)
window = main_window()
window.show()
sys.exit(App.exec())