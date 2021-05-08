import sys
from os import system
from time import sleep
from PyQt5 import QtWidgets, QtCore, QtGui
from interfaces.interfaz01 import Ui_MainWindow
from Logic.logicpart import main

class Window_GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window_GUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.addMat)
        self.ui.btnSubstract.clicked.connect(self.substractMat)
        self.ui.btnStart.clicked.connect(self.iniciar)
        self.ui.rbtnYes.clicked.connect(self.checkYes)
        self.ui.rbtnNo.clicked.connect(self.checkNo)
        self.inicializarTab()

    def addMat(self):
        self.ui.matN = self.ui.matN +1
        self.ui.tblMatA.setRowCount(self.ui.matN)
        self.ui.tblMatA.setColumnCount(self.ui.matN)
        self.ui.tblMatAn.setRowCount(self.ui.matN)
        self.ui.tblMatAn.setColumnCount(self.ui.matN)
        num = 0
        for i in range(self.ui.matN):
            celda = QtWidgets.QTableWidgetItem(str(num))
            celda2 = QtWidgets.QTableWidgetItem(str(num))
            self.ui.tblMatA.setItem(i,self.ui.matN-1,celda)
            self.ui.tblMatAn.setItem(i,self.ui.matN-1,celda2)
        
        for i in range(self.ui.matN-1):
            celda = QtWidgets.QTableWidgetItem(str(num))
            celda2 = QtWidgets.QTableWidgetItem(str(num))
            self.ui.tblMatA.setItem(self.ui.matN-1,i,celda)
            self.ui.tblMatAn.setItem(self.ui.matN-1,i,celda2)
        
                
    def substractMat(self):
        if(self.ui.matN>2):
            self.ui.matN = self.ui.matN -1
            self.ui.tblMatA.setRowCount(self.ui.matN)
            self.ui.tblMatA.setColumnCount(self.ui.matN)
            self.ui.tblMatAn.setRowCount(self.ui.matN)
            self.ui.tblMatAn.setColumnCount(self.ui.matN)
    
    def iniciar(self):
        main(self.ui)
    
    def checkYes(self):
        self.ui.btnContinue.setEnabled(True)
        self.ui.btnContinue.setStyleSheet("background-color: rgb(30,120,10);\n"
        "color: rgb(250,250,250)")
    
    def checkNo(self):
        self.ui.btnContinue.setEnabled(False)
        self.ui.btnContinue.setStyleSheet("background-color: rgb(30,30,30);\n"
        "color: rgb(30,30,30)")
    
    def inicializarTab(self):
        num=0
        for i in range(self.ui.matN):
            for j in range(self.ui.matN):
                celda = QtWidgets.QTableWidgetItem(str(num))
                celda2 = QtWidgets.QTableWidgetItem(str(num))
                self.ui.tblMatA.setItem(i,j,celda)
                self.ui.tblMatAn.setItem(i,j,celda2)


app = QtWidgets.QApplication([])
mi_app = Window_GUI()
mi_app.show()
sys.exit(app.exec())