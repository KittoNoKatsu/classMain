from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget

class SLW(QWidget):

    valueChanged = pyqtSignal(str, int, name='valueChanged')

    def __init__(self, parent = None):
        super(SLW, self).__init__(parent)
        uic.loadUi("Slider.itui", self)
        self.L = ""

    def setLetter(self, l):
        self.L = l
        self.label.setText( "Servo " + self.L)

    # SET VALUE VALUE CHANGE
    #def valueChanged(self, l, val):
    #    self.letter = l
    #    self.value = val
    #    print("3432")

    @pyqtSlot()
    def onSetData(self, l, val):
        if self.L == l:
            self. value = val
            print("setData of ", self.L)

    @pyqtSlot(int)
    def on_verticalScrollBar_valueChanged(self, val):
        print("Scroll bar ", self.L, " changed to ", val)
        self.textEdit.setText(str(val))
        self.valueChanged.emit(self.L, val)