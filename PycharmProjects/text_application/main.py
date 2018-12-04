import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(100,100,600,500)
        self.setWindowTitle('My text application')
        layout = QGridLayout()
        self.setLayout(layout)

        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)

        actionFile = menubar.addMenu('File')
        actionFile.addAction('New')
        actionFile.addSeparator()
        actionFile.addAction('Open...')
        actionFile.addAction('Save')
        actionFile.addAction('Save as...')


        actionEdit = menubar.addMenu("Edit")
        actionEdit.addAction('Cut')
        actionEdit.addSeparator()
        actionEdit.addAction('undo')
        actionEdit.addAction('redo')
        actionEdit.addAction('copy')
        actionEdit.addAction('Paste')
        actionEdit.addAction('Delete')

        actionSettings = menubar.addMenu('Settings')
        actionSettings.addAction('Font option...')
        actionSettings.addAction('Background color')

        actionView = menubar.addMenu('View')
        actionView.addAction('view line numbers')

        actionHelp = menubar.addMenu('Help')
        actionHelp.addAction('Help')
        actionHelp.addAction('Submit feed back')

        actionMore = menubar.addMenu('More')
        actionMore.addAction('Edit profile')
        actionMore.addAction('Save to mail')

        self.background_styling()

    def background_styling(self):
        return





if __name__ == '__main__':
    App = QApplication(sys.argv)
    main = main()
    main.show()
    sys.exit(App.exec_())
