import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout
from admin_authetication import Authenticate_admin



class display_window(QWidget):
   def __init__(self):
      
      QWidget.__init__(self)
      self.attr_list = []
      self.attr_image = ''
      
      self.display_background()
            
            
            
   def display_background(self):
      layout = QGridLayout()
      
      background_label = QLabel(self)
      background_label.resize(100, 100)
      pixmap = QPixmap(self.attr_image)
      self.pixmat = pixmap.scaled(100, 100)
      background_label.setPixmap(self.pixmat)
      background_label.setGeometry(300,200,100,100)
      background_label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      background_label.setScaledContents(True)
      layout.addWidget(background_label,2,3,4,4)
      
      last_row = 0
      for pre,row in zip(self.attr_list, list(range(7,len(self.attr_list)+7))):
         label = QLabel(pre, 'self')
         layout.addWidget(label,row,3,1,1)
         last_row = row
         
         
      login_row = last_row + 2
      loginButton =  QPushButton('Edit', self)
      loginButton.setToolTip("Edit as an Administrator")
      loginButton.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      loginButton.clicked.connect(self.click_to_edit)
      layout.addWidget(loginButton, login_row, 4,2,3)
         
         
      self.setLayout(layout)
      self.show()
         
      return
   
   def click_to_edit(self):
      self.auth = Authenticate_admin()
      self.auth.show()
      if self.auth.compare_details() == True:
         self.auth.destroy()
         # edit officer or soldier page
         
         
      else:
         pass
      
      return 
         
         
         
         
         
         
class edit_officer():
   def __init__(self):
      dis = display_window()
      self.attr = dis.attr_list
      self.image = dis.attr_image
      
      
   def display_officer_page(self):
      return
   
   
   def save_details(self):
      return
   
   
   def close_details(self):
      return
   
   
   
   
class edit_soldier():
   def __init__(self):
      dis = display_window()
      self.attr = dis.attr_list
      self.image = dis.attr_image
      
      
   def display_soldier_page(self):
      return
   
   
   def save_details(self):
      return
   
   
   def close_details(self):
      return
