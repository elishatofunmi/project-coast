import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "parent_form.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
LandingPageUI, LandingPageBase = uic.loadUiType("child_form.ui")

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnOpenChild.clicked.connect(self.showChildForm) 


    def showChildForm(self):
        self.child_win = childForm(self, 123)        
        self.child_win.show()      


class childForm(LandingPageBase, LandingPageUI):
    def __init__(self,  myInt, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        LandingPageBase.__init__(self)
        self.setupUi(self)

        self.myInt = myInt

        print("My int: " + str(self.myInt))


if __name__ == "__main__":
    app=QtWidgets.QApplication.instance() 
    if not app:  
         app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())