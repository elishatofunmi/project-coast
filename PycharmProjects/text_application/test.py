import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys



class Mainwindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.IMAGEPATH = 'C:/Users/ACER/Desktop/dummy_woman.png'


        self.styleSheet = """
        QPushButton{
            background-color:#4e4e4e;
            color:#ffffff;
        }
        QMainWindow{
            background-color:#ff9900;
            color:#ffffff;
        }
        QTextEdit:#myPsuedo{
            background-color:#ff5522;
        }
       
        
        
        """
        self.app.setStyleSheet(self.styleSheet)

        self.initGUI()

        self.window.setWindowTitle('Create a window')
        #self.window.setStyleSheet('background-color:#6e6e6e')
        self.window.setGeometry(500,100,300,600)
        self.window.show()
        sys.exit(self.app.exec_())


    def initGUI(self):

        #create a label
        self.image = QImage(self.IMAGEPATH)
        self.label = QLabel(self.window)
        self.label.setGeometry(50,20,200,200)
        #self.window.setStyleSheet('background-color:#6e6e6e')
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)

        # create a sudo field
        self.pseudo = QTextEdit(self.window)
        self.pseudo.setGeometry(25,270,250,40)
        self.pseudo.setText('Pseudo')
        self.pseudo.setObjectName('myPseudo')
        #self.pseudo.setStyleSheet('background-color:#f7f7f7; color: #8e8e8e; padding-top: 5px; font-size:15px; padding-left:10px')


        # create an email field
        self.email = QTextEdit(self.window)
        self.email.setGeometry(25, 330, 250, 40)
        self.email.setText('Email')
        #self.email.setStyleSheet('background-color:#f7f7f7; color: #8e8e8e; padding-top: 5px; font-size:15px; padding-left:10px')

        # create password field
        self.password = QTextEdit(self.window)
        self.password.setGeometry(25, 390, 250, 40)
        self.password.setText('Password')
        #self.password.setStyleSheet('background-color:#f7f7f7; color: #8e8e8e; padding-top: 5px; font-size:15px; padding-left:10px')

        # create confirm password field
        self.confirm_password = QTextEdit(self.window)
        self.confirm_password.setGeometry(25, 450, 250, 40)
        self.confirm_password.setText('confirm your password')
        #self.confirm_password.setStyleSheet('background-color:#f7f7f7; color: #8e8e8e; padding-top: 5px; font-size:15px; padding-left:10px')

        # create account button field
        self.createButton = QPushButton(self.window)
        self.createButton.setGeometry(25, 510, 250, 40)
        self.createButton.setText('Create an Account')
        #self.createButton.setStyleSheet('background-color:#f7f7f7; color: #8e8e8e; padding-top: 5px; font-size:15px; padding-left:10px')



main = Mainwindow()