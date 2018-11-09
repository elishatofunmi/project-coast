import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from admin_login import admin_log


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
        self.state = False
        
        
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
        self.srcc.setChecked(True)
        self.srcc.resize(20,20)
        
        self.sscc = QCheckBox('SSCC')
        layout.addWidget(self.sscc)
        self.sscc.move(60,60)
        self.sscc.setChecked(True)
        self.sscc.resize(20,20)
        
        self.ec = QCheckBox('EC')
        layout.addWidget(self.ec)
        self.ec.move(60,80)
        self.ec.setChecked(True)
        self.ec.resize(20,20)
        
        self.yoc = QCheckBox('YOC')
        layout.addWidget(self.yoc)
        self.yoc.move(80,40)
        self.yoc.setChecked(True)
        self.yoc.resize(20,20)
        
        self.bcc = QCheckBox('BCC')
        layout.addWidget(self.bcc)
        self.bcc.move(80,60)
        self.bcc.setChecked(True)
        self.bcc.resize(20,20)
        
        
        self.csc = QCheckBox('CSC')
        layout.addWidget(self.csc)
        self.csc.move(80,80)
        self.csc.setChecked(True)
        self.csc.resize(20,20)
        
        self.nhc = QCheckBox('NHC')
        layout.addWidget(self.nhc)
        self.nhc.move(100,40)
        self.nhc.setChecked(True)
        self.nhc.resize(20,20)
        
        self.ewc = QCheckBox('EWC')
        layout.addWidget(self.ewc)
        self.ewc.move(100,60)
        self.ewc.setChecked(True)
        self.ewc.resize(20,20)
        
        self.ict = QCheckBox('ICT management')
        layout.addWidget(self.ict)
        self.ict.move(100,80)
        self.ict.setChecked(True)
        self.ict.resize(20,20)


        
        
        self.click_to_login = QPushButton('Save', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(120,60)
        self.click_to_login.setToolTip("Save entries")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.save)



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
    
    def accept(self):
        selected_list = []
        if self.srcc.isChecked():
            selected_list.append('srcc')
      
        elif self.sscc.isChecked():
            selected_list.append('sscc')
                                 
                
        elif self.ec.isChecked():
            selected_list.append('ec')
            
        elif self.yoc.isChecked():
            selected_list.append('yoc')
        
        
        elif self.bcc.isChecked():
            selected_list.append('bcc')
            
        elif self.csc.isChecked():
            selected_list.append('csc')
            
        elif self.nhc.isChecked():
            selected_list.append('nhc')
    
        elif self.ewc.isChecked():
            selected_list.append('ewc')
            
        elif self.ict.isChecked():
            selected_list.append('ict management')
            
        elif self.fos.ischecked():
            selected_list.append('fos')
            
        elif self.yos.ischecked():
            selected_list.append('yos')
            
        elif self.rob_b1.ischeced():
            selected_list.append('rob_b1')
            
        elif self.rob_b2.ischecked():
            selected_list.append('rob_b2')
            
        elif self.rob_b3.ischecked():
            selected_list.append('rob_b3')
        elif self.tcx1.ischecked():
            selected_list.append('tcx1')
        elif self.tcx2.ischecked():
            selected_list.append('tcx2')
        elif self.tcx3.ischecked():
            selected_list.append('tcx3')
        elif self.dsd21.ischecked():
            selected_list.append('dsd21')
        elif self.dsd22.ischecked():
            selected_list.append('dsd22')
        elif self.dsd23.ischecked():
            selected_list.append('dsd23')
        elif self.lmnb1.ischecked():
            selected_list.append('lmnb1')
        elif self.lmnb2.ischecked():
            selected_list.append('lmnb2')
        elif self.lmnb3.ischecked():
            selected_list.append('lmnb3')
        elif self.nsc.ischecked():
            selected_list.append('nsc')
        elif self.ewc.ischecked():
            selected_list.append('ewc')
        else:
            pass
            
        return selected_list
    
    def save(self):
        saved_data = {}
        selected_list = self.accept()
        if (self.edit_name.text() == '') or (self.rank_title.text() == '') or (self.officer_unit.text() == ''):
            self.display_label.setText('you have not entered a valid detail for either name, rank or unit')
            
        else:
            if selected_list != []:
                saved_data['Name'] = self.edit_name.text()
                saved_data['Army_number'] = self.rank_title.text()
                saved_data['Unit'] = self.officer_unit.text()
                saved_data['Courses_attended'] = selected_list
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
        self.fos.setChecked(True)
        self.fos.resize(20,20)
        
        
        self.yos = QCheckBox('YOS')
        layout.addWidget(self.yos)
        self.yos.move(60,60)
        self.yos.setChecked(True)
        self.yos.toggled.connect(self.accept)
        self.yos.resize(20,20)
        
        
        self.rob_b1 = QCheckBox('ROP B1')
        layout.addWidget(self.rob_b1)
        self.rob_b1.move(60,80)
        self.rob_b1.setChecked(True)
        self.rob_b1.resize(20,20)


        self.rop_b2 = QCheckBox('ROP B2')
        layout.addWidget(self.rop_b2)
        self.rop_b2.move(80,40)
        self.rop_b2.setChecked(True)
        self.rop_b2.resize(20,20)
        
        self.rob_b3 = QCheckBox('ROP B3')
        layout.addWidget(self.rob_b3)
        self.rob_b3.move(80,60)
        self.rob_b3.setChecked(True)
        self.rob_b3.resize(20,20)
        
        
        self.rob_tcx1 = QCheckBox('TCX1')
        layout.addWidget(self.rob_tcx1)
        self.rob_tcx1.move(80,80)
        self.rob_tcx1.setChecked(True)
        self.rob_tcx1.resize(20,20)
        
        
        self.tcx2 = QCheckBox('TCX2')
        layout.addWidget(self.tcx2)
        self.tcx2.move(80,100)
        self.tcx2.setChecked(True)
        self.tcx2.resize(20,20)
        
        
        self.tcx3 = QCheckBox('TCX3')
        layout.addWidget(self.tcx3)
        self.tcx3.move(100,40)
        self.tcx3.setChecked(True)
        self.tcx3.resize(20,20)
        
        
        self.dsd21 = QCheckBox('DSD2 1')
        layout.addWidget(self.dsd21)
        self.dsd21.move(100,60)
        self.dsd21.setChecked(True)
        self.dsd21.resize(20,20)
        
        self.dsd22 = QCheckBox('DSD2 2')
        layout.addWidget(self.dsd22)
        self.dsd22.move(100,80)
        self.dsd22.setChecked(True)
        self.dsd22.resize(20,20)
        
        self.dsd23 = QCheckBox('DSD2 3')
        layout.addWidget(self.dsd23)
        self.dsd23.move(100,100)
        self.dsd23.setChecked(True)
        self.dsd22.resize(20,20)
        
        self.lmnb1 = QCheckBox('LMN B1')
        layout.addWidget(self.lmnb1)
        self.lmnb1.move(120,40)
        self.lmnb1.setChecked(True)
        self.lmnb1.resize(20,20)
        
        
        self.lmnb2 = QCheckBox('LMN B2')
        layout.addWidget(self.lmnb2)
        self.lmnb2.move(120,60)
        self.lmnb2.setChecked(True)
        self.lmnb2.resize(20,20)
        
        
        self.lmb3 = QCheckBox('LMN B2')
        layout.addWidget(self.lmb3)
        self.lmb3.move(120,80)
        self.lmb3.setChecked(True)
        self.lmb3.resize(20,20)
        
        
        self.bcc = QCheckBox('BCC')
        layout.addWidget(self.bcc)
        self.bcc.move(120,100)
        self.bcc.setChecked(True)
        self.bcc.resize(20,20)
        
        
        self.csc = QCheckBox('CSC')
        layout.addWidget(self.csc)
        self.csc.move(140,40)
        self.csc.setChecked(True)
        self.csc.resize(20,20)
        
        
        self.nhc = QCheckBox('NHC')
        layout.addWidget(self.nhc)
        self.nhc.move(140,60)
        self.nhc.setChecked(True)
        self.nhc.resize(20,20)
        
        
        self.nsc = QCheckBox('NSC')
        layout.addWidget(self.nsc)
        self.nsc.move(140,80)
        self.nsc.setChecked(True)
        self.nsc.resize(20,20)
        
        
        self.ewc = QCheckBox('EWC')
        layout.addWidget(self.ewc)
        self.ewc.move(140,100)
        self.ewc.setChecked(True)
        self.ewc.resize(20,20)
        
        
        self.click_to_login = QPushButton('Save', self)
        layout.addWidget(self.click_to_login)
        self.click_to_login.resize(20,20)
        self.click_to_login.move(160,60)
        self.click_to_login.setToolTip("Save entries")
        self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
        self.click_to_login.clicked.connect(self.save)



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
        return sys.exit()
    
    
    
    
def confirm_admin():
        log = admin_log()
        get_state = log.state
        log.show()
        
        if get_state == True:
            app = QCoreApplication.instance()
            if app is None:
                app = QApplication(sys.argv)
                app.setStyle('Fusion')
                window = sign_in()
                window.show()
                p = window.palette()
                p.setColor(window.backgroundRole(), Qt.gray)
                window.setPalette(p)
                sys.exit(App.exec())
        else:
            pass

if __name__ == '__main__':
    confirm_admin()
    
