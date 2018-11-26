import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout



class display_window(QWidget):
   def __init__(self, ar_list, ar_image,name):
      
      super().__init__()
      self.attr_list = ar_list
      self.attr_image = ar_image
      self.army_number = name
      self.setWindowTitle('student information')
      
      self.display_background()
      self.display_image()
      self.show()
            
   def display_background(self):
      self.width = 300
      self.height = 600
      self.setMaximumSize(300,600)
      self.label = QLabel(self)
      pixmap = QPixmap("all_background.PNG")
      self.label.setGeometry(0,0,self.width,self.height)
      self.label.setPixmap(pixmap)
      self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      self.label.setScaledContents(True)
      self.label.show()   
       
            
   def display_image(self):
      layout = QGridLayout()
      
      background_label = QLabel(self)
      pixmap = QPixmap(self.attr_image)
      self.pixmat = pixmap.scaled(100, 100)
      background_label.setPixmap(self.pixmat)
      background_label.setGeometry(300,200,100,100)
      background_label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      background_label.setScaledContents(True)
      layout.addWidget(background_label,2,2,5,3)
      
      name_label = QLabel('Name:',self)
      layout.addWidget(name_label,8,1,1,1)
      
      show_name = QLabel(str(self.attr_list[1]), self)
      layout.addWidget(show_name, 8,3,1,1)
      
      army_label = QLabel('Army No: ', self)
      layout.addWidget(army_label, 9, 1, 1,1)
      
      show_army = QLabel(str(self.attr_list[0]), self)
      layout.addWidget(show_army, 9,3, 1,1)
      
      rank_label = QLabel('Rank: ', self)
      layout.addWidget(rank_label, 10, 1,1,1)
      
      show_rank = QLabel(str(self.attr_list[2]), self)
      layout.addWidget(show_rank, 10, 3,1,1)
      
      unit_label = QLabel('Unit: ', self)
      layout.addWidget(unit_label, 11,1,1,1)
      
      show_unit = QLabel(str(self.attr_list[3]), self)
      layout.addWidget(show_unit, 11,3, 1,1)
      
      show_courses = QLabel('courses:', self)
      layout.addWidget(show_courses, 12,1,1,1)
      
      last_row = 12
      for pre,row in zip(self.attr_list[4].split(' '), list(range(12,len(self.attr_list[4])+10))):
         label = QLabel(str(pre), self)
         layout.addWidget(label,row,3,1,1)
         last_row = row
         
         
      login_row = last_row + 2
      close_button = QPushButton('close', self)
      close_button.setToolTip('Close')
      close_button.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      close_button.clicked.connect(self.click_to_close)
      layout.addWidget(close_button, login_row, 1,2,2)
         
      
      
      loginButton =  QPushButton('Edit', self)
      loginButton.setToolTip("Edit as an Administrator")
      loginButton.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      loginButton.clicked.connect(self.click_to_edit)
      layout.addWidget(loginButton, login_row, 4,2,2)
         
         
      self.setLayout(layout)
      self.show()
         
   
   def click_to_edit(self):
      self.admin = Auth_admin(self.attr_list,self.attr_image)
      self.admin.show()
   
 
   
   def click_to_close(self):
      sys.exit()
      return
   
   
   
   
class Auth_admin(QWidget):
    def __init__(self, ar_list, ar_image):
        QWidget.__init__(self)
        self.title = 'Admin login'
        self.setMaximumSize(700,500)
        self.dict_details = {'username': None, 'password': None}
        self.attr_list = ar_list
        self.attr_image = ar_image
        self.display_background()
        self.display_login_details()
        
       
    def display_background(self):
       self.setWindowTitle(self.title)
       self.width = 700
       self.height = 500
       self.top = 300
       self.left = 200

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
        
    def get_admin_details(self):
       
       flie_open = open('admin_details.txt', 'r')
       read_data = flie_open.readlines()[0]
       data = read_data.split(',')
       flie_open.close()
       if data == '':
          sol = False
       else:
          sol = True
        
       return sol
    
   
    def get_my_admin_details(self):
       
       flie_open = open('admin_details.txt', 'r')
       read_data = flie_open.read()
       data = read_data
       flie_open.close()
       if data == '':
          sol = False
       else:
          sol = True
        
       return sol
        
        
        
    def display_login_details(self):
        self.setWindowTitle(self.title)
        
        #layout = QVBoxLayout()

        # display Username
        self.label_name = QLabel('Username:',self)
        self.label_name.move(90,150)
        self.label_name.resize(100,30)
       # layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit('', self)
        self.lineedit_name.move(180,150)
        self.lineedit_name.resize(400,30)
        self.lineedit_name.setPlaceholderText("Enter your username")
        #layout.addWidget(self.lineedit_name)
        
        # display Rank/title
        self.rank_title = QLabel('Password:',self)
        self.rank_title.move(90,250)
        self.rank_title.resize(100,30)
       # layout.addWidget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit('', self)
        self.rank_title_edit.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
        self.rank_title_edit.move(180,250)
        self.rank_title_edit.resize(400,30)
       # layout.addWidget(self.rank_title_edit)
        self.rank_title_edit.setPlaceholderText("Enter your password")
        #self.setLayout(layout)
        
        self.click_to_login = QPushButton('login', self)
       # layout.addWidget(self.click_to_login)
        self.click_to_login.resize(200,30)
        self.click_to_login.move(150,300)
        self.click_to_login.setToolTip("save details")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.log_details)
        
        self.click_to_cancel = QPushButton('close', self)
       # layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(200,30)
        self.click_to_cancel.move(400,300)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.cancel_details)
        
        
        
        self.display_label = QLabel('',self)
       # layout.addWidget(self.display_label)
        self.display_label.resize(200,30)
        self.display_label.move(100,400)
        self.show()
        return
     
       
     
    def log_details(self):
       if self.compare_details() == True:
          if 'officer' in self.attr_image:
             self.offi= edit_officer(self.attr_list, self.attr_image, self.army_number)
             self.offi.show()
             
          elif 'soldier' in self.attr_image:
             self.sold = edit_sold(self.attr_list, self.attr_image, self.army_number)
             self.sold.show()
             
          else:
             pass
 
       return 
       
       
       
   
    def read_admin_details(self):
        flie_open = open('admin_details.txt', 'r')
        read_data = flie_open.readlines()[0]
        data = read_data.split(',')
        flie_open.close()
        
        return data[0],data[1]
          
          
    def compare_details(self):
        name = self.lineedit_name.text()
        rank = self.rank_title_edit.text()
        
        
        user_name, password = self.read_admin_details()
        
        
        if (name == user_name) and (rank == password):
            solu = True
            self.display_label.setText('your details is confirmed')
        else:
            solu = False
            self.display_label.setText('confirm your details')
        
        return solu
    
    def cancel_details(self):
        return sys.exit(self)
         
         
     
      
      
         
class edit_officer(QWidget):
   def __init__(self,my_list, my_image, name):
      super().__init__()
      self.attr = my_list
      self.image = my_image
      self.army_number = name
      self.background()
      self.display_officer_page()
      
      
   def background(self):
      self.width = 300
      self.height = 600
      self.setMaximumSize(300,600)
      self.label = QLabel(self)
      pixmap = QPixmap("all_background.PNG")
      self.label.setGeometry(0,0,self.width,self.height)
      self.label.setPixmap(pixmap)
      self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      self.label.setScaledContents(True)
      self.label.show() 
      return
      
   def display_officer_page(self):
       layout = QGridLayout()

        # display name
       self.name = QLabel('Name:', self)
       self.name.move(30,30)
       self.name.resize(40,20)
       layout.addWidget(self.name, 1,2,1,1)


        # display entry box for name
       self.edit_name = QLineEdit('', self)
       self.edit_name.move(100,30)
       self.edit_name.resize(400, 30)
       self.edit_name.setPlaceholderText("Enter officer name")
       layout.addWidget(self.edit_name,1,4,1,5)
       

        # display Rank/title
#       self.rank_title = QLabel('Army Number:', self)
#       self.rank_title.move(30,70)
#       self.rank_title.resize(80,20)
#       layout.addWidget(self.rank_title,2,2,1,1)
#
#        # display entry box for rank or title
#       self.rank_title_edit = QLineEdit('',self)
#       self.rank_title_edit.move(100,70)
#       self.rank_title_edit.resize(400,30)
#       layout.addWidget(self.rank_title_edit,2,4,1,5)
#       self.rank_title_edit.setPlaceholderText("Enter Army number")
       
       
        # display RANK
       self.rank = QLabel('Rank:', self)
       layout.addWidget(self.rank,3,2,1,1)

        # display entry box for rank or title
       self.rank_box = QLineEdit('',self)
       self.rank_box.move(100,70)
       self.rank_box.resize(400,30)
       layout.addWidget(self.rank_box,3,4,1,5)
       self.rank_box.setPlaceholderText("Enter your rank")
       
       


        # display unit
       self.officer_unit = QLabel('Unit:', self)
       self.officer_unit.move(30,110)
       self.officer_unit.resize(40,20)
       layout.addWidget(self.officer_unit,4,2,1,1)

        #dispaly entrybox for unit
       self.enter_unit = QLineEdit('', self)
       self.enter_unit.move(100,110)
       self.enter_unit.resize(400,30)
       layout.addWidget(self.enter_unit,4,4,1,5)
       self.enter_unit.setPlaceholderText("Enter Unit")



        # course_attended
       self.srcc = QCheckBox('SRCC', self)
       layout.addWidget(self.srcc,6,1,1,2)
       self.srcc.move(30,150)
       self.srcc.setChecked(False)
       self.srcc.resize(50,50)
        #self.srcc.stateChanged.connect(self.accept)
        
       self.sscc = QCheckBox('SSCC', self)
       layout.addWidget(self.sscc,6,4,1,2)
       self.sscc.move(180,150)
       self.sscc.setChecked(False)
       self.sscc.resize(50,50)
        #self.sscc.stateChanged.connect(self.accept)
        
       self.ec = QCheckBox('EC', self)
       layout.addWidget(self.ec,6,7,1,2)
       self.ec.move(330,150)
       self.ec.setChecked(False)
       self.ec.resize(50,50)
        #self.ec.stateChanged.connect(self.accept)
        
       self.yoc = QCheckBox('YOC', self)
       layout.addWidget(self.yoc,6,10,1,2)
       self.yoc.move(480,150)
       self.yoc.setChecked(False)
       self.yoc.resize(50,50)
       #self.yoc.stateChanged.connect(self.accept)
        
       self.bcc = QCheckBox('BCC', self)
       layout.addWidget(self.bcc,7,1,1,2)
       self.bcc.move(30,200)
       self.bcc.setChecked(False)
       self.bcc.resize(50,50)
        #self.bcc.stateChanged.connect(self.accept)
        
        
       self.csc = QCheckBox('CSC', self)
       layout.addWidget(self.csc,7,4,1,2)
       self.csc.move(180,200)
       self.csc.setChecked(False)
       self.csc.resize(50,50)
        #self.csc.stateChanged.connect(self.accept)
        
       self.nhc = QCheckBox('NHC', self)
       layout.addWidget(self.nhc,7,7,1,2)
       self.nhc.move(330,200)
       self.nhc.setChecked(False)
       self.nhc.resize(50,50)
        #self.nhc.stateChanged.connect(self.accept)
        
       self.ewc = QCheckBox('EWC', self)
       layout.addWidget(self.ewc,7,10,1,2)
       self.ewc.move(480,200)
       self.ewc.setChecked(False)
       self.ewc.resize(50,50)
        #self.ewc.stateChanged.connect(self.accept)
        
       self.ict = QCheckBox('ICT management', self)
       layout.addWidget(self.ict,8,1,1,2)
       self.ict.move(30,250)
       self.ict.setChecked(False)
       self.ict.resize(80,50)
        #self.ict.stateChanged.connect(self.accept)


        
        
       self.click_to_login = QPushButton('Save', self)
       layout.addWidget(self.click_to_login,9,2,2,2)
       self.click_to_login.resize(150,40)
       self.click_to_login.move(30, 350)
       self.click_to_login.setToolTip("Save entries")
       self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
       self.click_to_login.clicked.connect(self.save_officer)

        
       self.open_file = QPushButton('Change image', self)
       layout.addWidget(self.open_file,9,5,2,2)
       self.open_file.resize(150,40)
       self.open_file.move(240,350)
       self.open_file.setToolTip("Save entries")
       self.open_file.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
       self.open_file.clicked.connect(self.add_image)
        

       self.click_to_cancel = QPushButton('close', self)
       layout.addWidget(self.click_to_cancel,9,8,2,2)
       self.click_to_cancel.resize(150,40)
       self.click_to_cancel.move(440,350)
       self.click_to_cancel.setToolTip("close window")
       self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
       self.click_to_cancel.clicked.connect(self.close_details)
        
       self.display_label = QLabel('',self)
       layout.addWidget(self.display_label,12,2,2,7)
       self.display_label.resize(300, 30)
       self.display_label.move(30,400)
   
    
       self.setLayout(layout)
       self.show()
       #return
    
    
   def accept(self):
       
       try:
          selected_list = ''
          
          if hasattr(self, 'srcc') and self.srcc.isChecked():
             selected_list +=  'srcc ' 
          else:
             pass
         
          if hasattr(self, 'sscc') and self.sscc.isChecked():
             selected_list+= 'sscc '
          else:
             pass
                                    
                   
          if hasattr(self, 'ec') and self.ec.isChecked():
              selected_list+= 'ec '
          else:
             pass
               
          if hasattr(self, 'yoc') and self.yoc.isChecked():
              selected_list+= 'yoc '
          else:
             pass
           
           
          if hasattr(self, 'bcc') and self.bcc.isChecked():
              selected_list+= 'bcc '
          else:
             pass
               
          if hasattr(self, 'csc') and self.csc.isChecked():
              selected_list+= 'csc '
          else:
             pass
               
          if hasattr(self, 'nhc') and self.nhc.isChecked():
              selected_list+= 'nhc '
          else:
             pass
               
          if hasattr(self, 'ict') and self.ict.isChecked():
              selected_list+= 'ict '
               
          if hasattr(self, 'fos') and self.fos.isChecked():
              selected_list+= 'fos '
               
          if hasattr(self, 'yos') and self.yos.isChecked():
             selected_list+= 'yos '
               
          if hasattr(self, 'rob_b1') and self.rob_b1.isChecked():
             selected_list+= 'rob_b1 '
               
          if hasattr(self, 'rop_b2') and self.rop_b2.isChecked():
             selected_list+= 'rop_b2 '
               
          if hasattr(self, 'rob_b3') and self.rob_b3.isChecked():
             self.selected_list+= 'rob_b3 '
          if hasattr(self, 'rob_tcx1') and self.rob_tcx1.isChecked():
             selected_list+= 'rob_tcx1 '
          if hasattr(self, 'tcx2') and self.tcx2.isChecked():
             selected_list+= 'tcx2 '
          if hasattr(self, 'tcx3') and self.tcx3.isChecked():
             selected_list+= 'tcx3 '
          if hasattr(self, 'dsd21') and self.dsd21.isChecked():
             selected_list+= 'dsd21 '
          if hasattr(self, 'dsd22') and self.dsd22.isChecked():
             selected_list+= 'dsd22 '
          if hasattr(self, 'dsd23') and self.dsd23.isChecked():
             selected_list+= 'dsd23 '
          if hasattr(self, 'lmnb1') and self.lmnb1.isChecked():
             selected_list+= 'lmnb1 '
          if hasattr(self, 'lmnb2') and self.lmnb2.isChecked():
             selected_list+= 'lmnb2 '
          if hasattr(self, 'lmb3') and self.lmb3.isChecked():
             selected_list+= 'lmnb3 '
          if hasattr(self, 'nsc') and self.nsc.isChecked():
             selected_list+= 'nsc '
          if hasattr(self, 'ewc') and self.ewc.isChecked():
             selected_list+= 'ewc '
          else:
             pass
       
          
       #except AttributeError:
        #  pass
       
       finally:
          pass
       
            
       return selected_lists
   def add_image(self):
      import os
       
       self.file_out = QFileDialog()
       self.file_out.setAcceptMode(QFileDialog.AcceptOpen)
       #self.file_out.setLabelText('add image')
       self.file_out.setDefaultSuffix('.png')
       self.file_out.setViewMode(QFileDialog.Detail)
       #self.file_out.open()
       
       fileName = self.file_out.getOpenFileName()
       filePath = str(fileName[0])
       source_file = self.image
       self.get_image = QImage(filePath)
       new_path = r'C:\Users\ACER\Desktop\database management system\images\\'+ self.rank_title_edit.text()+ '_' + self.army_type + '.png'
   
       destination = new_path
       os.replace(source_file, new_path)
       
       return
    
     
   def save_officer(self):
        saved_data = {}
        saved_list = []
        select_list = self.accept()
        if (self.edit_name.text() == '') or (self.rank_box.text() == '') or (self.enter_unit.text() == ''):
            self.display_label.setText('you have not entered a valid detail for either name, rank or unit')
            
        else:
            if select_list != []:
                
               
                saved_data['name'] = self.edit_name.text()
                saved_list.append(str(self.edit_name.text()))
                saved_data['rank'] = self.rank_box.text()
                saved_list.append(str(self.rank_box.text()))
                saved_data['unit'] = self.enter_unit.text()
                saved_list.append(str(self.enter_unit.text()))
                saved_data['courses_attended'] = select_list
                saved_list.append(select_list)
                self.display_label.setText('your details have been saved')
        
            else:
                self.display_label.setText('you have not registered any course')
            
        
        # save data to database
        
        print('opened database and write to database')
        print(saved_list)
        unique_list = tuple(saved_list)
        print(unique_list)
        self.data_d = Database()
        self.data_d.data = unique_list
        self.data_d.update_record(self.army_number,base_type = 'officer')
        print('written to database')
        return
   
   
   
   def close_details(self):
      sys.exit(self)
      return
   
   
   
   
   
   
   
class edit_soldier(QWidget):
   def __init__(self, my_list, my_image, name):
      super().__init__()
      self.attr = my_list
      self.image = my_image
      self.army_number =name
      self.background()
      self.display_soldier_page()
      
   def background(self):
      self.width = 300
      self.height = 600
      self.setMaximumSize(300,600)
      self.label = QLabel(self)
      pixmap = QPixmap("all_background.PNG")
      self.label.setGeometry(0,0,self.width,self.height)
      self.label.setPixmap(pixmap)
      self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
      self.label.setScaledContents(True)
      self.label.show() 
      return
      
      
   def display_soldier_page(self):
      # display name
        layout = QGridLayout()
        self.name = QLabel('Name:', self)
        self.name.move(30,30)
        self.name.resize(40,30)
        layout.addWidget(self.name,1,2,1,1)


        # display entry box for name
        self.edit_name = QLineEdit('', self)
        self.edit_name.move(100,30)
        self.edit_name.resize(400,30)
        self.edit_name.setPlaceholderText("Enter officer name")
        layout.addWidget(self.edit_name,1,4,1,5)
        

        # display Rank/title
        self.rank_title = QLabel('Army Number:', self)
        self.rank_title.move(30,70)
        self.rank_title.resize(80,20)
        layout.addWidget(self.rank_title,2,2,1,1)


        # display entry box for rank or title
        self.rank_title_edit = QLineEdit('', self)
        self.rank_title_edit.move(100,70)
        self.rank_title_edit.resize(400,30)
        layout.addWidget(self.rank_title_edit,2,4,1,5)
        self.rank_title_edit.setPlaceholderText("Enter Army number")


         # display RANK
        self.rank = QLabel('Rank:', self)
        layout.addWidget(self.rank,3,2,1,1)

        # display entry box for rank or title
        self.rank_box = QLineEdit('',self)
        self.rank_box.move(100,70)
        self.rank_box.resize(400,30)
        layout.addWidget(self.rank_box,3,4,1,5)
        self.rank_box.setPlaceholderText("Enter your rank")


        # display unit
        self.officer_unit = QLabel('Unit:',self)
        self.officer_unit.move(30,110)
        self.officer_unit.resize(40,20)
        layout.addWidget(self.officer_unit,4,2,1,1)

        #dispaly entrybox for unit
        self.enter_unit = QLineEdit('', self)
        self.enter_unit.move(100,110)
        self.enter_unit.resize(400,30)
        layout.addWidget(self.enter_unit,4,4,1,5)
        self.enter_unit.setPlaceholderText("Enter Unit")
        
        
        #display soldiers details
        self.fos = QCheckBox('FOS', self)
        layout.addWidget(self.fos,5,1,1,2)
        self.fos.move(30,150)
        self.fos.setChecked(False)
        self.fos.resize(50,50)
        #self.fos.stateChanged.connect(self.accept)
        
        
        self.yos = QCheckBox('YOS', self)
        layout.addWidget(self.yos,5,4,1,2)
        self.yos.move(180,150)
        self.yos.setChecked(False)
        self.yos.resize(50,50)
        #self.yos.stateChanged.connect(self.accept)
        
        
        self.rob_b1 = QCheckBox('ROP B1', self)
        layout.addWidget(self.rob_b1,5,7,1,2)
        self.rob_b1.move(330,150)
        self.rob_b1.setChecked(False)
        self.rob_b1.resize(50,60)
        #self.rob_b1.stateChanged.connect(self.accept)


        self.rop_b2 = QCheckBox('ROP B2', self)
        layout.addWidget(self.rop_b2,5,10,1,2)
        self.rop_b2.move(480,150)
        self.rop_b2.setChecked(False)
        self.rop_b2.resize(50,60)
        #self.rop_b2.stateChanged.connect(self.accept)
        
        self.rob_b3 = QCheckBox('ROP B3', self)
        layout.addWidget(self.rob_b3,6,1,1,2)
        self.rob_b3.move(30,200)
        self.rob_b3.setChecked(False)
        self.rob_b3.resize(50,60)
        #self.rob_b3.stateChanged.connect(self.accept)
        
        
        self.rob_tcx1 = QCheckBox('TCX1', self)
        layout.addWidget(self.rob_tcx1,6,4,1,2)
        self.rob_tcx1.move(180,200)
        self.rob_tcx1.setChecked(False)
        self.rob_tcx1.resize(50,50)
        #self.rob_tcx1.stateChanged.connect(self.accept)
        
        
        self.tcx2 = QCheckBox('TCX2', self)
        layout.addWidget(self.tcx2,6,7,1,2)
        self.tcx2.move(330,200)
        self.tcx2.setChecked(False)
        self.tcx2.resize(50,50)
        #self.tcx2.stateChanged.connect(self.accept)
        
        
        self.tcx3 = QCheckBox('TCX3', self)
        layout.addWidget(self.tcx3,6,10,1,2)
        self.tcx3.move(480,200)
        self.tcx3.setChecked(False)
        self.tcx3.resize(50,50)
        #self.tcx3.stateChanged.connect(self.accept)
        
        
        self.dsd21 = QCheckBox('DSD2 1', self)
        layout.addWidget(self.dsd21,8,1,1,2)
        self.dsd21.move(30,250)
        self.dsd21.setChecked(False)
        self.dsd21.resize(50,60)
        #self.dsd21.stateChanged.connect(self.accept)
        
        self.dsd22 = QCheckBox('DSD2 2', self)
        layout.addWidget(self.dsd22,8,4,1,2)
        self.dsd22.move(180,250)
        self.dsd22.setChecked(False)
        self.dsd22.resize(50,60)
        #self.dsd22.stateChanged.connect(self.accept)
        
        self.dsd23 = QCheckBox('DSD2 3', self)
        layout.addWidget(self.dsd23,8,7,1,2)
        self.dsd23.move(330,250)
        self.dsd23.setChecked(False)
        self.dsd23.resize(50,60)
        #self.dsd23.stateChanged.connect(self.accept)
        
        self.lmnb1 = QCheckBox('LMN B1', self)
        layout.addWidget(self.lmnb1,8,10,1,2)
        self.lmnb1.move(480,250)
        self.lmnb1.setChecked(False)
        self.lmnb1.resize(50,60)
        #self.lmnb1.stateChanged.connect(self.accept)
        
        
        self.lmnb2 = QCheckBox('LMN B2', self)
        layout.addWidget(self.lmnb2,10,1,1,2)
        self.lmnb2.move(30,300)
        self.lmnb2.setChecked(False)
        self.lmnb2.resize(50,60)
        #self.lmnb2.stateChanged.connect(self.accept)
        
        
        self.lmb3 = QCheckBox('LMN B3',self)
        layout.addWidget(self.lmb3,10,4,1,2)
        self.lmb3.move(180,300)
        self.lmb3.setChecked(False)
        self.lmb3.resize(50,60)
        #self.lmb3.stateChanged.connect(self.accept)
        
        
        self.bcc = QCheckBox('BCC',self)
        layout.addWidget(self.bcc,10,7,1,2)
        self.bcc.move(330,300)
        self.bcc.setChecked(False)
        self.bcc.resize(50,50)
        #self.bcc.stateChanged.connect(self.accept)
        
        
        self.csc = QCheckBox('CSC',self)
        layout.addWidget(self.csc,10,10,1,2)
        self.csc.move(480,300)
        self.csc.setChecked(False)
        self.csc.resize(50,50)
        #self.csc.stateChanged.connect(self.accept)
        
        
        self.nhc = QCheckBox('NHC',self)
        layout.addWidget(self.nhc,12,1,1,2)
        self.nhc.move(30,350)
        self.nhc.setChecked(False)
        self.nhc.resize(50,50)
        #self.nhc.stateChanged.connect(self.accept)
        
        
        self.nsc = QCheckBox('NSC',self)
        layout.addWidget(self.nsc,12,4,1,2)
        self.nsc.move(180,350)
        self.nsc.setChecked(False)
        self.nsc.resize(50,50)
        #self.nsc.stateChanged.connect(self.accept)
        
        
        self.ewc = QCheckBox('EWC',self)
        layout.addWidget(self.ewc,12,7,1,2)
        self.ewc.move(330,350)
        self.ewc.setChecked(False)
        self.ewc.resize(50,50)
        #self.ewc.stateChanged.connect(self.accept)
        
        
        self.click_to_login = QPushButton('Save', self)
        layout.addWidget(self.click_to_login,14,2,2,3)
        self.click_to_login.resize(150,40)
        self.click_to_login.move(30,400)
        self.click_to_login.setToolTip("Save entries")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.save_soldier)
        
        self.open_file = QPushButton('Change image', self)
        layout.addWidget(self.open_file,14,6,2,3)
        self.open_file.resize(150,40)
        self.open_file.move(200,400)
        self.open_file.setToolTip("Save entries")
        self.open_file.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.open_file.clicked.connect(self.add_image)



        self.click_to_cancel = QPushButton('close', self)
        layout.addWidget(self.click_to_cancel,14,10,2,3)
        self.click_to_cancel.resize(150,40)
        self.click_to_cancel.move(370,400)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.close_win)
        
        self.display_label = QLabel('',self)
        layout.addWidget(self.display_label,16,2,2,8)
        self.display_label.resize(400,30)
        self.display_label.move(430,450)
        self.setLayout(layout)
        self.show()
        
        
   def add_image(self):
       import os
       
       self.file_out = QFileDialog()
       self.file_out.setAcceptMode(QFileDialog.AcceptOpen)
       #self.file_out.setLabelText('add image')
       self.file_out.setDefaultSuffix('.png')
       self.file_out.setViewMode(QFileDialog.Detail)
       #self.file_out.open()
       
       fileName = self.file_out.getOpenFileName()
       filePath = str(fileName[0])
       source_file = self.image
       self.get_image = QImage(filePath)
       new_path = r'C:\Users\ACER\Desktop\database management system\images\\'+ self.rank_title_edit.text()+ '_' + self.army_type + '.png'
   
       destination = new_path
       os.replace(source_file, new_path)
       return 
       
       
   
            
   def accept(self):
       
       try:
          selected_list = ''
          
          if hasattr(self, 'srcc') and self.srcc.isChecked():
             selected_list +=  'srcc ' 
          else:
             pass
         
          if hasattr(self, 'sscc') and self.sscc.isChecked():
             selected_list+= 'sscc '
          else:
             pass
                                    
                   
          if hasattr(self, 'ec') and self.ec.isChecked():
              selected_list+= 'ec '
          else:
             pass
               
          if hasattr(self, 'yoc') and self.yoc.isChecked():
              selected_list+= 'yoc '
          else:
             pass
           
           
          if hasattr(self, 'bcc') and self.bcc.isChecked():
              selected_list+= 'bcc '
          else:
             pass
               
          if hasattr(self, 'csc') and self.csc.isChecked():
              selected_list+= 'csc '
          else:
             pass
               
          if hasattr(self, 'nhc') and self.nhc.isChecked():
              selected_list+= 'nhc '
          else:
             pass
               
          if hasattr(self, 'ict') and self.ict.isChecked():
              selected_list+= 'ict '
               
          if hasattr(self, 'fos') and self.fos.isChecked():
              selected_list+= 'fos '
               
          if hasattr(self, 'yos') and self.yos.isChecked():
             selected_list+= 'yos '
               
          if hasattr(self, 'rob_b1') and self.rob_b1.isChecked():
             selected_list+= 'rob_b1 '
               
          if hasattr(self, 'rop_b2') and self.rop_b2.isChecked():
             selected_list+= 'rop_b2 '
               
          if hasattr(self, 'rob_b3') and self.rob_b3.isChecked():
             self.selected_list+= 'rob_b3 '
          if hasattr(self, 'rob_tcx1') and self.rob_tcx1.isChecked():
             selected_list+= 'rob_tcx1 '
          if hasattr(self, 'tcx2') and self.tcx2.isChecked():
             selected_list+= 'tcx2 '
          if hasattr(self, 'tcx3') and self.tcx3.isChecked():
             selected_list+= 'tcx3 '
          if hasattr(self, 'dsd21') and self.dsd21.isChecked():
             selected_list+= 'dsd21 '
          if hasattr(self, 'dsd22') and self.dsd22.isChecked():
             selected_list+= 'dsd22 '
          if hasattr(self, 'dsd23') and self.dsd23.isChecked():
             selected_list+= 'dsd23 '
          if hasattr(self, 'lmnb1') and self.lmnb1.isChecked():
             selected_list+= 'lmnb1 '
          if hasattr(self, 'lmnb2') and self.lmnb2.isChecked():
             selected_list+= 'lmnb2 '
          if hasattr(self, 'lmb3') and self.lmb3.isChecked():
             selected_list+= 'lmnb3 '
          if hasattr(self, 'nsc') and self.nsc.isChecked():
             selected_list+= 'nsc '
          if hasattr(self, 'ewc') and self.ewc.isChecked():
             selected_list+= 'ewc '
          else:
             pass
       
          
       #except AttributeError:
        #  pass
       
       finally:
          pass
       
            
       return selected_list
   
   
   def save_soldier(self):
        saved_data = {}
        saved_list = []
        select_list = self.accept()
        if (self.edit_name.text() == '') or (self.rank_box.text() == '') or (self.enter_unit.text() == ''):
            self.display_label.setText('you have not entered a valid detail for either name, rank or unit')
            
        else:
            if select_list != []:
                saved_data['name'] = self.edit_name.text()
                saved_list.append(str(self.edit_name.text()))
                saved_data['rank'] = self.rank_box.text()
                saved_list.append(str(self.rank_box.text()))
                saved_data['unit'] = self.enter_unit.text()
                saved_list.append(str(self.enter_unit.text()))
                saved_data['courses_attended'] = select_list
                saved_list.append(select_list)
                self.display_label.setText('your details have been saved')
        
            else:
                self.display_label.setText('you have not registered any course')
            
        
        # save data to database
        print('opened database and write to database')
        print(saved_list)
        unique_list = tuple(saved_list)
        print(unique_list)
        self.data_d = Database()
        self.data_d.data = unique_list
        self.data_d.update_record(self.army_number,base_type = 'soldier')
        print('written to database')
        return
   
   
   def close_details(self):
      sys.exit(self)
      return
   
   
   

   
   
