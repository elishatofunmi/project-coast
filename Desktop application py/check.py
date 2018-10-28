import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "DataBase mill"
        self.dict_details = {}
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitWindow()

    def get_details(self):
        self.dict_details['Name'] = self.lineedit_name.text()
        self.dict_details['Rank/Title'] = self.rank_title_edit.text()
        self.dict_details['Password'] = self.password_me.text()
        self.dict_details['confirm_password'] = self.password_confirm.text()
        if self.confirm_details() == True:
            self.display_label = QLabel('your details have been saved successfully')
            self.label_name.move(100,430)
            # close this window
        return 


    def clear_details(self):
        self.dict_details = {}
        return

    def sign_in_details(self):
        # if details have been confirmed
        # print that details have been saved
        # login as an admin
        # go to search blah blah blah......
        return

    def confirm_details(self):
        if dict_details['Password'] != dict_details['confirm_password']:
            self.display_label = QLabel('your password does not match')
            self.label_name.move(100,430)
            solution = False

        else:
            solution = True
        return solution

        

    def convert_image(self):
        from PIL import Image
        im = Image.open("index.jpeg")
        bg = Image.new("RBG", im.size, (255,255,255))
        bg.paste(im, (0,0), im)
        bg.save("index.png", quality = 95)
        

        im2 = Image.open("icon.jpeg")
        bg2 = Image.new("RBG", im2.size, (255,255,255))
        bg2.paste(im, (0,0), im2)
        bg2.save("index.png", quality = 95)
    

    def InitWindow(self):
        self.setWindowTitle(self.title)


        #self.label = QLabel(self)
        #pixmap = QPixmap("data_scientist.png")
        #self.label.setGeometry(0,0,700,500)
        #self.label.setPixmap(pixmap)
        #self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        #self.label.setScaledContents(True)
        #self.label.show()

        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(self.top, self.left,self.width, self.height)

        #self.convert_image()
        self.init_buttons()
        self.display_details()


    def display_details(self):
        
        layout = QVBoxLayout()

        # display name
        self.label_name = QLabel('Name:')
        self.label_name.move(30,40)
        layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit()
        self.lineedit_name.setPlaceholderText("Enter your name")
        layout.addWidget(self.lineedit,50 ,40)
        

        # display Rank/title
        self.rank_title = QLabel('Rank/Title:')
        self.rank_title.move(30,60)
        layout.add_widget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit()
        layout.addWidget(self.rank_title_edit,50 ,60)
        self.rank_title_edit.setPlaceholderText("Enter your Title/Rank")


        # display password
        self.password_label = QLabel('Password:')
        self.password_label.move(30,80)
        layout.add_widget(self.password_label)

        #dispaly entrybox for password
        self.password_me = QLineEdit()
        layout.addWidget(self.password_me,50 ,80)
        self.password_me.setPlaceholderText("Enter your password")


        # display confirm password
        self.password_confirm_label = QLabel('Confirm password:')
        self.password__confirm_label.move(30,100)
        layout.add_widget(self.password_confirm_label)
        


        # display entrybox to confirm password
        self.password_confirm = QLineEdit()
        layout.addWidget(self.password_confirm,50 ,100)
        self.password_confirm.setPlaceholderText("confirm your password here")


        widget = QWidget()
        widget.setLayout(layout)
        widget.show()
        return

        

    def init_buttons(self):
        button = QPushButton('save', self)
        button.move(100, 400)
        button.resize(100,30)
        button.setToolTip("This buttons saves all your entries")
        button.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button.connect(self.get_details)
        
        button1 = QPushButton('cancel', self)
        button1.setToolTip("This button cancels whatever you might have done initially")
        button1.resize(100,30)
        button1.move(450,400)
        button1.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button1.connect(self.clear_details)


        button2 = QPushButton('sign in', self)
        button2.setToolTip("This signs you in immediately after you login your details")
        button2.resize(100,30)
        button2.move(270,400)
        button2.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        button2.connect(self.sign_in_details)



#if "__name__" == "__main__":
App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())

