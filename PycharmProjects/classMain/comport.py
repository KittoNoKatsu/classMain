from PyQt5 import uic
from PyQt5.QtCore import QIODevice, pyqtSignal

class port():
    changeValue = pyqtSignal(int)
    def __init__(self, name, parent = None):
        super(port, self).__init__(parent)
        ui_form, ui_base = uic.loadUiType('manipulator.ui')
        self.ui = ui_form()
        self.ui.setupUi(self)
        self.ui.label.setText(name)
        self._name = name
        #self.changeValue.connect(self.on_vc_external)

    def onOpen(self):
        self.serial.setPortName(ui.comL.currentText())
        self.serial.open(QIODevice.ReadWrite)
        # serial.write('90a'.encode())
        # print("rrr")

    def onClose(self):
        serial.close()
        # serial.write('b'.encode())

    ui.openB.clicked.connect(onOpen)
    ui.closeB.clicked.connect(onClose)