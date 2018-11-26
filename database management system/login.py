import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

#from database_display import Database
from display_window import display_window
from database import Database




class login(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Student login'
        self.top = 300
        self.left = 200
        self.width = 700
        self.height = 500
        self.setMaximumSize(700,500)
        self.dict_details = {}
        #self.mai = main()
        #self.mai.stacked.setCurrentWidget(self)
        self.trigger_login()
        self.army_type = ''
        

    def trigger_login(self):
        self.display_background()
        self.display_login_details()
        return
    
    

    def display_background(self):
       self.setWindowTitle(self.title)


       self.label = QLabel(self)
       pixmap = QPixmap("all_background.PNG")
       self.label.setGeometry(0,0,self.width,self.height)
       self.label.setPixmap(pixmap)
       self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
       self.label.setScaledContents(True)
       self.label.show()

        #self.setWindowIcon(QIcon('icon.png'))
       self.setGeometry(self.top, self.left,self.width, self.height)
        #return


    def display_login_details(self):
        
        #layout = QVBoxLayout()

        # display name
        self.label_name = QLabel('Army No:', self)
        self.label_name.move(90,150)
        self.label_name.resize(100,30)
        #layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit('', self)
        self.lineedit_name.move(180,150)
        self.lineedit_name.resize(400,30)
        self.lineedit_name.setPlaceholderText("Enter your army number")
        #layout.addWidget(self.lineedit_name)
        

       

        self.click_to_login = QPushButton('Login', self)
        #layout.addWidget(self.click_to_login)
        self.click_to_login.resize(200,30)
        self.click_to_login.move(150,230)
        self.click_to_login.setToolTip("Login")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.log_in)
        
        self.click_to_cancel = QPushButton('close', self)
        #layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(200,30)
        self.click_to_cancel.move(400,230)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.close_win)
    
        self.display_label = QLabel('',self)
        #layout.addWidget(self.display_label)
        self.display_label.resize(400,30)
        self.display_label.move(300,450)

        #self.setLayout(layout)
        self.show()
        #return
    
    def confirm_details(self):
        name = self.lineedit_name.text()
        
        
        if (name != ''):
            solu = True
        else:
            solu = False
        return solu
 
       
    def display_person(self, det):
       self.the_window = display_window()
       self.the_window.set_attr = det
       rank_name = det[1]
       new_path = r'C:\Users\ACER\Desktop\database management system\images\\'
       link = new_path + str(rank_name) + '.png'
       self.the_window.attr_image = link
       self.the_window.show()
       
       return
    
    
    def close_win(self):
        return sys.exit()
     
      
    
    def log_in(self):
       display = Database()
       details = ()
       if self.confirm_details() == True:
           # find person
           name = self.lineedit_name.text()
           try:
              details = display.fetch_record(name, base_type= 'officer')
              if details != 'not found':
                 self.army_type = 'officer'
                 print(self.army_type)
              else:
                 pass
           except TypeError:
              try:
                 details= display.fetch_record(name, base_type = 'soldier')
                 print('second try')
                 if details != 'not found':
                    self.army_type = 'soldier'
                    print(self.army_type)
                 else:
                    pass
              except TypeError:
                 details = 'not found'
           finally:
              if details == 'not found':
                 self.display_label.setText('user not found re enter a valid user')
              else:
                 self.display_label.setText('user has been found')
                 print(details)
                 get_image_directory = r'C:\Users\ACER\Desktop\database management system\images\\' + self.lineedit_name.text()+ '_' + self.army_type + '.png'
                 self.display_data = display_window(ar_list = details, ar_image = get_image_directory, name)
                 self.display_data.show()
                 
                 
                 
                 
       else:
          self.display_label.setText('enter a valid input')
                     
       return
    
    def my_display(self, first):
       
       return 




    



if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = login()
    window.show()
    sys.exit(App.exec())