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
    numOfJoints = 6
    if len (sys.argv) > 1:
        try:
            numOfJoints = int(sys.argv[1])
        except Exception as e:
            print("Some error on argument", e)
            exit(1)

    if numOfJoints != 6 and numOfJoints != 4:
        print("Only 6 or 4 joints are supported as number of joints")
        exit(1)

    ui = MainWindow(numOfJoints)
    ui.setAvailablePortNames(portList)

    ui.show()
    app.exec()


if __name__ == "__main__":
    main()