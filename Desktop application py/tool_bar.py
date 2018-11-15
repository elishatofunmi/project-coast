from PyQt5.QtWidgets import *
import sys
# toolbar typically provides common shortcuts to features of an
# application(e.g. open file, find, zoom)
class Window(QWidget):
	QWidget.__init__(self)
	
	layout = QGridLayout()
	self.setLayout(layout)
	
	toolbar = QToolBar()
	layout.addWidget(toolbar)
	
	toolbutton = QToolBar()
	layout.addWidget(toolbar)
	
	toolbutton = QToolButton()
	toolbutton.setText('button 1')
	toolbutton.setCheckable(True)
	toolbutton.setAutoExclusive(True)
	toolbar.addWidget(toolbutton)
	
	
	toolbutton = QToolButton()
	toolbutton.setText('Button 2')
	toolbutton.setCheckable(True)
	toolbutton.setAutoExclusive(True)
	toolbar.addWidget(toolbutton)
	
	
app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())