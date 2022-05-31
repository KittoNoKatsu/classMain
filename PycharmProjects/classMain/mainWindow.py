from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
#from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("manipulator.ui", self)

    def setAvailablePortNames(self, portNames):
        #self.comL.addItems(portNames)
        for i in portNames:
            self.comL.addItem("/dev/" + i)