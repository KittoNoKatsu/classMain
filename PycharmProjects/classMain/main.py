from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from mainWindow import MainWindow


def main():
    serial = QSerialPort()
    serial.setBaudRate(115200)

    portList = []
    ports = QSerialPortInfo().availablePorts()
    for port in ports:
        portList.append(port.portName())

    app = QtWidgets.QApplication([])
    #ui = uic.loadUi("manipulator.ui")

    #ui.comL.addItems(portList)
    ui = MainWindow()
    ui.setAvailablePortNames(portList)

    ui.show()
    app.exec()


if __name__ == "__main__":
    main()