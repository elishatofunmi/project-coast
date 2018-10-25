# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:41:53 2018

@author: ACER
"""

#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)
        
        label = QLabel("Label 1")
        layout.addWidget(label, 0)
        label = QLabel("Label 2")
        layout.addWidget(label, 0)
        
        layout2= QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)
        
        label = QLabel("Label 3")
        layout2.addWidget(label, 0)
        label = QLabel("Label 4")
        layout2.addWidget(label, 0)
        
app = QApplication(sys.argv)
screen = Window()
screen.show()


sys.exit(app.exec_())
