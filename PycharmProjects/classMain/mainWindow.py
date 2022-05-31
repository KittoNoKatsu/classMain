from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from slider_widget import SLW


class MainWindow(QMainWindow):
    def __init__(self, count):
        super().__init__()
        uic.loadUi("manipulator.ui", self)
        self.numOfJoints = count
        print("received count =", count)
        for i in range(count):
            ss = SLW(self)
            ss.setLetter(chr(ord('A') + i))
            self.horizontalLayout.addWidget(ss)

    def setAvailablePortNames(self, portNames):
        for i in portNames:
            self.comL.addItem("/dev/" + i)