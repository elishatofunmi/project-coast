import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton



from PyQt5.QtCore import QCoreApplication




class sign_in(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'sign in'
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 200
        self.setMaximumSize(700,500)
        self.selected_list = []
        self.get_image = None
        
        
        self.show_officer_or_soldier()
            
    
       
        
    def show_officer_or_soldier(self):
        mb = QMessageBox()
        mb.setText('select Either officer or soldier')
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('select detail')
            
            
        self.cancel_but = QPushButton("Cancel")
        self.cancel_but.clicked.connect(self.cancel)
        self.officer_but = QPushButton('Officer')
        self.officer_but.clicked.connect(self.offi_cer)
        self.member_but = QPushButton('soldier')
        self.member_but.clicked.connect(self.mem_ber)
            
            
        mb.addButton(self.member_but, mb.YesRole)
        mb.addButton(self.officer_but, mb.NoRole)
        mb.addButton(self.cancel_but, mb.RejectRole)
        ret = mb.exec_()
        mb.show() 
        
        

    def display_background(self):
        self.setWindowTitle(self.title)


        self.label = QLabel(self)
        #pixmap = QPixmap("army_details.png")
        #self.label.setGeometry(0,0,self.width,self.height)
        #self.label.setPixmap(pixmap)
        self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.label.setScaledContents(True)
        self.label.show()

        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(self.top, self.left,self.width, self.height)
        return


    def display_officer_details(self):
        
        layout = QVBoxLayout()

        # display name
        self.name = QLabel('Name:')
        self.name.move(30,40)
        #self.label_name.resize()
        layout.addWidget(self.name)


        # display entry box for name
        self.edit_name = QLineEdit()
        self.edit_name.move(30,50)
        self.edit_name.resize(20,20)
        self.edit_name.setPlaceholderText("Enter officer name")
        layout.addWidget(self.edit_name)
        

        # display Rank/title
        self.rank_title = QLabel('Army Number:')
        self.rank_title.move(40,40)
        layout.addWidget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit()
        self.rank_title_edit.move(40,50)
        self.rank_title_edit.resize(20,20)
        layout.addWidget(self.rank_title_edit)
        self.rank_title_edit.setPlaceholderText("Enter Army number")


        # display unit
        self.officer_unit = QLabel('Unit:')
        self.officer_unit.move(50,40)
        layout.addWidget(self.officer_unit)

        #dispaly entrybox for unit
        self.enter_unit = QLineEdit()
        self.enter_unit.move(50,50)
        self.enter_unit.resize(20,20)
        layout.addWidget(self.enter_unit)
        self.enter_unit.setPlaceholderText("Enter Unit")



        # course_attended
        self.srcc = QCheckBox('SRCC')
        layout.addWidget(self.srcc)
        self.srcc.move(60,40)
        self.srcc.setChecked(False)
        self.srcc.resize(20,20)
        #self.srcc.stateChanged.connect(self.accept)
        
        self.sscc = QCheckBox('SSCC')
        layout.addWidget(self.sscc)
        self.sscc.move(60,60)
        self.sscc.setChecked(False)
        self.sscc.resize(20,20)
        #self.sscc.stateChanged.connect(self.accept)
        
        self.ec = QCheckBox('EC')
        layout.addWidget(self.ec)
        self.ec.move(60,80)
        self.ec.setChecked(False)
        self.ec.resize(20,20)
        #self.ec.stateChanged.connect(self.accept)
        
        self.yoc = QCheckBox('YOC')
        layout.addWidget(self.yoc)
        self.yoc.move(80,40)
        self.yoc.setChecked(False)
        self.yoc.resize(20,20)
        #self.yoc.stateChanged.connect(self.accept)
        
        self.bcc = QCheckBox('BCC')
        layout.addWidget(self.bcc)
        self.bcc.move(80,60)
        self.bcc.setChecked(False)
        self.bcc.resize(20,20)
        #self.bcc.stateChanged.connect(self.accept)
        
        
        self.csc = QCheckBox('CSC')
        layout.addWidget(self.csc)
        self.csc.move(80,80)
        self.csc.setChecked(False)
        self.csc.resize(20,20)
        #self.csc.stateChanged.connect(self.accept)
        
        self.nhc = QCheckBox('NHC')
        layout.addWidget(self.nhc)
        self.nhc.move(100,40)
        self.nhc.setChecked(False)
        self.nhc.resize(20,20)
        #self.nhc.stateChanged.connect(self.accept)
        
        self.ewc = QCheckBox('EWC')
        layout.addWidget(self.ewc)
        self.ewc.move(100,60)
        self.ewc.setChecked(False)
        self.ewc.resize(20,20)
        #self.ewc.stateChanged.connect(self.accept)
        
        self.ict = QCheckBox('ICT management')
        layout.addWidget(self.ict)
        self.ict.move(100,80)
        self.ict.setChecked(False)
        self.ict.resize(20,20)
        #self.ict.stateChanged.connect(self.accept)


        
        
        self.click_to_login = QPushButton('Save', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(120,60)
        self.click_to_login.setToolTip("Save entries")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.save)

        
        self.open_file = QPushButton('Add image', self)
        layout.addWidget(self.open_file)
        self.open_file.resize(20,20)
        self.open_file.move(160,100)
        self.open_file.setToolTip("Save entries")
        self.open_file.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.open_file.clicked.connect(self.add_image)
        

        self.click_to_cancel = QPushButton('close', self)
        layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(20,20)
        self.click_to_cancel.move(120,80)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.close_win)
        
        self.display_label = QLabel('',self)
        layout.addWidget(self.display_label)
        self.display_label.resize(40,30)
        self.display_label.move(150,40)
   
    
        self.setLayout(layout)
        self.show()
        return
    
    
    
    def save(self):
        saved_data = {}
        select_list = self.accept()
        if (self.edit_name.text() == '') or (self.rank_title_edit.text() == '') or (self.enter_unit.text() == ''):
            self.display_label.setText('you have not entered a valid detail for either name, rank or unit')
            
        else:
            if select_list != []:
                saved_data['Name'] = self.edit_name.text()
                saved_data['Army_number'] = self.rank_title_edit.text()
                saved_data['Unit'] = self.enter_unit.text()
                saved_data['Courses_attended'] = select_list
                saved_data['image'] = self.get_image
                self.display_label.setText('your details have been saved')
        
            else:
                self.display_label.setText('you have not registered any course')
            
        
        # save data to database
        print (saved_data)
        return
    
    
        
    def display_soldier_details(self):
        # display name
        layout = QVBoxLayout()
        self.name = QLabel('Name:')
        self.name.move(30,40)
        #self.label_name.resize()
        layout.addWidget(self.name)


        # display entry box for name
        self.edit_name = QLineEdit()
        self.edit_name.move(30,50)
        self.edit_name.resize(20,20)
        self.edit_name.setPlaceholderText("Enter officer name")
        layout.addWidget(self.edit_name)
        

        # display Rank/title
        self.rank_title = QLabel('Army Number:')
        self.rank_title.move(40,40)
        layout.addWidget(self.rank_title)


        # display entry box for rank or title
        self.rank_title_edit = QLineEdit()
        self.rank_title_edit.move(40,50)
        self.rank_title_edit.resize(20,20)
        layout.addWidget(self.rank_title_edit)
        self.rank_title_edit.setPlaceholderText("Enter Army number")


        # display unit
        self.officer_unit = QLabel('Unit:')
        self.officer_unit.move(50,40)
        layout.addWidget(self.officer_unit)

        #dispaly entrybox for unit
        self.enter_unit = QLineEdit()
        self.enter_unit.move(50,50)
        self.enter_unit.resize(20,20)
        layout.addWidget(self.enter_unit)
        self.enter_unit.setPlaceholderText("Enter Unit")
        
        
        #display soldiers details
        self.fos = QCheckBox('FOS')
        layout.addWidget(self.fos)
        self.fos.move(60,40)
        self.fos.setChecked(False)
        self.fos.resize(20,20)
        #self.fos.stateChanged.connect(self.accept)
        
        
        self.yos = QCheckBox('YOS')
        layout.addWidget(self.yos)
        self.yos.move(60,60)
        self.yos.setChecked(False)
        self.yos.resize(20,20)
        #self.yos.stateChanged.connect(self.accept)
        
        
        self.rob_b1 = QCheckBox('ROP B1')
        layout.addWidget(self.rob_b1)
        self.rob_b1.move(60,80)
        self.rob_b1.setChecked(False)
        self.rob_b1.resize(20,20)
        #self.rob_b1.stateChanged.connect(self.accept)


        self.rop_b2 = QCheckBox('ROP B2')
        layout.addWidget(self.rop_b2)
        self.rop_b2.move(80,40)
        self.rop_b2.setChecked(False)
        self.rop_b2.resize(20,20)
        #self.rop_b2.stateChanged.connect(self.accept)
        
        self.rob_b3 = QCheckBox('ROP B3')
        layout.addWidget(self.rob_b3)
        self.rob_b3.move(80,60)
        self.rob_b3.setChecked(False)
        self.rob_b3.resize(20,20)
        #self.rob_b3.stateChanged.connect(self.accept)
        
        
        self.rob_tcx1 = QCheckBox('TCX1')
        layout.addWidget(self.rob_tcx1)
        self.rob_tcx1.move(80,80)
        self.rob_tcx1.setChecked(False)
        self.rob_tcx1.resize(20,20)
        #self.rob_tcx1.stateChanged.connect(self.accept)
        
        
        self.tcx2 = QCheckBox('TCX2')
        layout.addWidget(self.tcx2)
        self.tcx2.move(80,100)
        self.tcx2.setChecked(False)
        self.tcx2.resize(20,20)
        #self.tcx2.stateChanged.connect(self.accept)
        
        
        self.tcx3 = QCheckBox('TCX3')
        layout.addWidget(self.tcx3)
        self.tcx3.move(100,40)
        self.tcx3.setChecked(False)
        self.tcx3.resize(20,20)
        #self.tcx3.stateChanged.connect(self.accept)
        
        
        self.dsd21 = QCheckBox('DSD2 1')
        layout.addWidget(self.dsd21)
        self.dsd21.move(100,60)
        self.dsd21.setChecked(False)
        self.dsd21.resize(20,20)
        #self.dsd21.stateChanged.connect(self.accept)
        
        self.dsd22 = QCheckBox('DSD2 2')
        layout.addWidget(self.dsd22)
        self.dsd22.move(100,80)
        self.dsd22.setChecked(False)
        self.dsd22.resize(20,20)
        #self.dsd22.stateChanged.connect(self.accept)
        
        self.dsd23 = QCheckBox('DSD2 3')
        layout.addWidget(self.dsd23)
        self.dsd23.move(100,100)
        self.dsd23.setChecked(False)
        self.dsd23.resize(20,20)
        #self.dsd23.stateChanged.connect(self.accept)
        
        self.lmnb1 = QCheckBox('LMN B1')
        layout.addWidget(self.lmnb1)
        self.lmnb1.move(120,40)
        self.lmnb1.setChecked(False)
        self.lmnb1.resize(20,20)
        #self.lmnb1.stateChanged.connect(self.accept)
        
        
        self.lmnb2 = QCheckBox('LMN B2')
        layout.addWidget(self.lmnb2)
        self.lmnb2.move(120,60)
        self.lmnb2.setChecked(False)
        self.lmnb2.resize(20,20)
        #self.lmnb2.stateChanged.connect(self.accept)
        
        
        self.lmb3 = QCheckBox('LMN B3')
        layout.addWidget(self.lmb3)
        self.lmb3.move(120,80)
        self.lmb3.setChecked(False)
        self.lmb3.resize(20,20)
        #self.lmb3.stateChanged.connect(self.accept)
        
        
        self.bcc = QCheckBox('BCC')
        layout.addWidget(self.bcc)
        self.bcc.move(120,100)
        self.bcc.setChecked(False)
        self.bcc.resize(20,20)
        #self.bcc.stateChanged.connect(self.accept)
        
        
        self.csc = QCheckBox('CSC')
        layout.addWidget(self.csc)
        self.csc.move(140,40)
        self.csc.setChecked(False)
        self.csc.resize(20,20)
        #self.csc.stateChanged.connect(self.accept)
        
        
        self.nhc = QCheckBox('NHC')
        layout.addWidget(self.nhc)
        self.nhc.move(140,60)
        self.nhc.setChecked(False)
        self.nhc.resize(20,20)
        #self.nhc.stateChanged.connect(self.accept)
        
        
        self.nsc = QCheckBox('NSC')
        layout.addWidget(self.nsc)
        self.nsc.move(140,80)
        self.nsc.setChecked(False)
        self.nsc.resize(20,20)
        #self.nsc.stateChanged.connect(self.accept)
        
        
        self.ewc = QCheckBox('EWC')
        layout.addWidget(self.ewc)
        self.ewc.move(140,100)
        self.ewc.setChecked(False)
        self.ewc.resize(20,20)
        #self.ewc.stateChanged.connect(self.accept)
        
        
        self.click_to_login = QPushButton('Save', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(160,60)
        self.click_to_login.setToolTip("Save entries")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.save)
        
        self.open_file = QPushButton('Add image', self)
        layout.addWidget(self.open_file)
        self.open_file.resize(20,20)
        self.open_file.move(160,100)
        self.open_file.setToolTip("Save entries")
        self.open_file.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.open_file.clicked.connect(self.add_image)



        self.click_to_cancel = QPushButton('close', self)
        layout.addWidget(self.click_to_cancel)
        self.click_to_cancel.resize(20,20)
        self.click_to_cancel.move(160,80)
        self.click_to_cancel.setToolTip("close window")
        self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_cancel.clicked.connect(self.close_win)
        
        self.display_label = QLabel('',self)
        layout.addWidget(self.display_label)
        self.display_label.resize(40,30)
        self.display_label.move(200,40)
        self.setLayout(layout)
        self.show()
        
        
    def add_image(self):
       
       self.file_out = QFileDialog()
       self.file_out.setAcceptMode(QFileDialog.AcceptOpen)
       #self.file_out.setLabelText('add image')
       self.file_out.setDefaultSuffix('.png')
       self.file_out.setViewMode(QFileDialog.Detail)
       #self.file_out.open()
       
       fileName = self.file_out.getOpenFileName()
       filePath = str(fileName[0])

       self.get_image = QImage(filePath)
       return 
       
       
   
            
    def accept(self):
       
       try:
          selected_list = []
          
          if hasattr(self, 'srcc') and self.srcc.isChecked():
             selected_list.append('srcc')
          else:
             pass
         
          if hasattr(self, 'sscc') and self.sscc.isChecked():
             selected_list.append('sscc')
          else:
             pass
                                    
                   
          if hasattr(self, 'ec') and self.ec.isChecked():
              selected_list.append('ec')
          else:
             pass
               
          if hasattr(self, 'yoc') and self.yoc.isChecked():
              selected_list.append('yoc')
          else:
             pass
           
           
          if hasattr(self, 'bcc') and self.bcc.isChecked():
              selected_list.append('bcc')
          else:
             pass
               
          if hasattr(self, 'csc') and self.csc.isChecked():
              selected_list.append('csc')
          else:
             pass
               
          if hasattr(self, 'nhc') and self.nhc.isChecked():
              selected_list.append('nhc')
          else:
             pass
               
          if hasattr(self, 'ict') and self.ict.isChecked():
              selected_list.append('ict management')
               
          if hasattr(self, 'fos') and self.fos.isChecked():
              selected_list.append('fos')
               
          if hasattr(self, 'yos') and self.yos.isChecked():
             selected_list.append('yos')
               
          if hasattr(self, 'rob_b1') and self.rob_b1.isChecked():
             selected_list.append('rob_b1')
               
          if hasattr(self, 'rop_b2') and self.rop_b2.isChecked():
             selected_list.append('rob_b2')
               
          if hasattr(self, 'rob_b3') and self.rob_b3.isChecked():
             self.selected_list.append('rob_b3')
          if hasattr(self, 'rob_tcx1') and self.rob_tcx1.isChecked():
             selected_list.append('tcx1')
          if hasattr(self, 'tcx2') and self.tcx2.isChecked():
             selected_list.append('tcx2')
          if hasattr(self, 'tcx3') and self.tcx3.isChecked():
             selected_list.append('tcx3')
          if hasattr(self, 'dsd21') and self.dsd21.isChecked():
             selected_list.append('dsd21')
          if hasattr(self, 'dsd22') and self.dsd22.isChecked():
             selected_list.append('dsd22')
          if hasattr(self, 'dsd23') and self.dsd23.isChecked():
             selected_list.append('dsd23')
          if hasattr(self, 'lmnb1') and self.lmnb1.isChecked():
             selected_list.append('lmnb1')
          if hasattr(self, 'lmnb2') and self.lmnb2.isChecked():
             selected_list.append('lmnb2')
          if hasattr(self, 'lmb3') and self.lmb3.isChecked():
             selected_list.append('lmnb3')
          if hasattr(self, 'nsc') and self.nsc.isChecked():
             selected_list.append('nsc')
          if hasattr(self, 'ewc') and self.ewc.isChecked():
             selected_list.append('ewc')
          else:
             pass
       
          
       #except AttributeError:
        #  pass
       
       finally:
          pass
       
            
       return selected_list
    
    def cancel(self):
        #back to initial window
        return
    
    def offi_cer(self):
        # go to officers page
        self.display_background()
        self.display_officer_details()
        return
    
    def mem_ber(self):
        # go to soldiers page
        self.display_background()
        self.display_soldier_details()
        return
    
    def close_win(self):
        self.dict_details = {}
        self.destroy()
        sys.exit()
        return sys.exit()
    
    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   app.setStyle('Fusion')
   window = sign_in()
   window.show()
   p = window.palette()
   p.setColor(window.backgroundRole(), Qt.gray)
   window.setPalette(p)
   sys.exit(app.exec())
   
    
