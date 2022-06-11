from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from slider_widget import SLW


class MainWindow(QMainWindow):


    setData = pyqtSignal(str, int, name ="setData")


    def __init__(self, count):
        super().__init__()
        self.fab = None
        self.inst = None
        self.singles = []
        uic.loadUi("manipulator.ui", self)
        self.numOfJoints = count
        print("received count =", count)
        for i in range(count):
            ss = SLW(self)
            ss.setLetter(chr(ord('A') + i))
            self.horizontalLayout.addWidget(ss)
            self.singles.append(ss)
            # setData(letter, value) - pyqtSignal (char, int) of MainWindow
            # valueChanged(letter, value)  - pyqtSignal of SLW
            self.setData.connect(ss.onSetData) # onSetData - slot of SLW
            ss.valueChanged.connect(self.onVC)  # onVC - slot of MainWindow

    def setAvailablePortNames(self, portNames):
        for i in portNames:
            self.comL.addItem("/dev/" + i)

    @pyqtSlot()
    def on_openB_clicked(self):
        print("port open called")
        #wrapper is selecte
        wrapperName = self.wrapperType.text
        portName = self.comL.text
        self.inst = self.fab.createWErapper("PRL_UART", portName)
        if self.inst is None:
            # TODO inform user on fail of operation
            return
            pass
        if not self.inst.isOpen():
            #inform user
            self.inst = None
            return

        self.inst.newData.connect(self.superReceiveSlot)
        self.newRqSignal.connect( self.inst.newPosRQ_Slot)


    @pyqtSlot()
    def on_closeB_clicked(self):
        print("port close called")
        if self.inst is None:
            return

        #disconnect
        #disconnect
        #self.inst.close()
        #self.inst = None

    def setWrapperFabric(self, fab):
        self.fab = fab

    def updateControl(self):
        if self.fab is not None:
            pass
            #for i in self.fab.getSupportedWrappers():
                #self.wrapperType.addItem(i.getName())
                #??portNames = self.fab.getWrapper("PRL_UART").getPortsList()
                #??for p in portNames:
                #??    self.comL.addItem("/dev/" + p)

    @pyqtSlot(str, int)
    def onVC(self, letter, val):
        print("onVC", letter, "   ", val )

    @pyqtSlot()
    def updateControls(self):
        pass