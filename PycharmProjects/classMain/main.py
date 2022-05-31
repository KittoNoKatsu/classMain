#!/usr/bin/env python3

from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from mainWindow import MainWindow
import sys


def main():
    serial = QSerialPort()
    serial.setBaudRate(115200)

    portList = []
    ports = QSerialPortInfo().availablePorts()
    for port in ports:
        portList.append(port.portName())

    app = QtWidgets.QApplication([])
    """ui = None
   if len (sys.argv) > 1:
        ui = MainWindow(sys.argv[1])
    else:
        ui = MainWindow(6)"""

    ui = MainWindow(sys.argv[1] if len(sys.argv) > 1 else 6)
    ui.setAvailablePortNames(portList)

    ui.show()
    app.exec()


if __name__ == "__main__":
    main()