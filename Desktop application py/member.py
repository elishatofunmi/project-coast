import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import pandas as pd


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.stackedwidget = QStackedWidget()
        layout.addWidget(self.stackedwidget, 0,0)
        
        
        for x in range(1,4):
            label = QLabel('stack child%i' % (x))
            self.stackedwidget.addWidget(label)
            
            button = QPushButton('stack %i' % (x))
            button.page = x
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button, x, 0)
            
    def on_button_clicked(self):
        button = self.sender()
        self.stackedwidget.setCurrentIndex(button.page - 1)
        
app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec())







def save(self):
        self.dict_details['Name'] = self.lineedit_name.text()
        self.dict_details['Rank/Title'] = self.rank_title_edit.text()
        self.dict_details['Password'] = self.password_me.text()
        self.dict_details['confirm_password'] = self.password_conf.text()
        if self.confirm_details() == True:
            self.display_label.setText('your details have been saved successfully')
            
            file_open = open('admin_details.txt', 'w')
            list_both = [self.lineedit_name.text(),',', self.rank_title_edit.text(),',', self.password_me.text(),
                         ',',self.password_conf.text()]
            file_open.writelines(list_both)
            file_open.close()
            
        return self.log_in


    def confirm_details(self):
        solution = False
        if self.verify_details() == False:
            if self.dict_details['Password'] != self.dict_details['confirm_password']:
                self.display_label.setText('your password does not match')
                solution = False
                
            else:
                solution = True
        else:
            self.display_label.setText('Invalid entry, please enter your details')
        return solution
    
    
    
    def verify_details(self):
        return ('' in self.dict_details.values())


    def get_name(self):
        self.dict_details['Name'] = self.lineedit_name.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return
    
    def get_rank(self):
        self.dict_details['Rank/Title'] = self.rank_title_edit.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return
    
    def get_password(self):
        self.dict_details['password'] = self.password_me.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return
    
    def get_confirm_password(self):
        self.dict_details['confirm_password'] = self.password_conf.text()
        file_open = open('admin_details.txt', 'w')
        file_open.writelines(self.dict_details)
        file_open.close()
        return

        