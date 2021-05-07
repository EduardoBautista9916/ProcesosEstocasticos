import sys
from PyQt5 import QtWidgets, QtCore
from interfaces.interfaz01 import Ui_MainWindow
from Logic.logicpart import main

class Window_GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window_GUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.addMat)
        self.ui.btnSubstract.clicked.connect(self.substractMat)

    def addMat(self):
        self.ui.matN = self.ui.matN +1
        self.ui.tblMatA.setRowCount(self.ui.matN)
        self.ui.tblMatA.setColumnCount(self.ui.matN)
        self.ui.tblMatAn.setRowCount(self.ui.matN)
        self.ui.tblMatAn.setColumnCount(self.ui.matN)
    
    def substractMat(self):
        if(self.ui.matN>2):
            self.ui.matN = self.ui.matN -1
            self.ui.tblMatA.setRowCount(self.ui.matN)
            self.ui.tblMatA.setColumnCount(self.ui.matN)
            self.ui.tblMatAn.setRowCount(self.ui.matN)
            self.ui.tblMatAn.setColumnCount(self.ui.matN)

app = QtWidgets.QApplication([])
mi_app = Window_GUI()
mi_app.show()
sys.exit(app.exec())