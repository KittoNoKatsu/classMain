from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, count):
        super().__init__()
        uic.loadUi("manipulator.ui", self)
        self.numOfJoints = count
        print("received count =", count)

    def setAvailablePortNames(self, portNames):
        for i in portNames:
            self.comL.addItem("/dev/" + i)