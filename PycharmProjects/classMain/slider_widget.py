from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget

class SLW(QWidget):
    def __init__(self, parent = None):
        super(SLW, self).__init__(parent)
        uic.loadUi("Slider.ui", self)
        self.L = ""

    def setLetter(self, l):
        self.L = l
        self.label.setText( "Servo " + self.L)
