import self as self
from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog

class ReadServo():

    def __init__(self, valA, valB, valC, valD, valE, valF):
        self.valA = valA
        self.valB = valB
        self.valC = valC
        self.valD = valD
        self.valE = valE
        self.valF = valF

    def onRead(self):
        rx = self.serial.readLine()
        rxs = None
        try:
            rxs = str(rx, 'utf-8').split("\n")
        except UnicodeDecodeError as ude:
            print("il a un erreour: ", ude)
            return
        except:
            print("unexpected exception occured")
            return
        finally:
            print("finally part: rxs=", rxs)

        if "=" in rxs[0] and '\r' in rxs[0]:
            print(rxs[0])
            ar1 = rxs[0].split(" ")
            for aar in ar1:
                if "A" in aar:
                    va = aar.split("=")
                    ui.valA.setText(va[1])
                elif "B" in aar:
                    va = aar.split("=")
                    ui.valB.setText(va[1])
                elif "C" in aar:
                    va = aar.split("=")
                    ui.valC.setText(va[1])
                elif "D" in aar:
                    va = aar.split("=")
                    ui.valD.setText(va[1])
                elif "E" in aar:
                    va = aar.split("=")
                    ui.valE.setText(va[1])
                elif "F" in aar:
                    va = aar.split("=")
                    ui.valF.setText(va[1])

    self.serial.readyRead.connect(onRead)


class ServoA(port):

    def __init__(self, ServoA):
        super().__init__(ServoA)


    def servoControlA(val):
        txs = ""
        txs += str(val + 5)
        txs += 'a'
        serial.write(txs.encode())

    ui.servoA.valueChanged.connect(servoControlA)

   # def serialSend(data):
   #     txs = ""
    #    for val in data:
    #        txs += str(val)
     #       txs += ','
     #   txs = txs[:-1]
     #   txs += ';'

class ServoB(port):

    def __init__(self, ServoB):
        super().__init__(ServoB)

    def servoControlB(val):
        txs = ""
        txs += str(val + 5)
        txs += 'b'
        serial.write(txs.encode())

    ui.servoB.valueChanged.connect(servoControlB)


class ServoC(port):

    def __init__(self, ServoC):
        super().__init__(ServoC)

    def servoControlC(val):
        txs = ""
        txs += str(val + 5)
        txs += 'c'
        serial.write(txs.encode())

    ui.servoC.valueChanged.connect(servoControlC)


class ServoD(port):

    def __init__(self, ServoD):
        super().__init__(ServoD)

    def servoControlD(val):
        txs = ""
        txs += str(val + 5)
        txs += 'd'
        serial.write(txs.encode())

    ui.servoD.valueChanged.connect(servoControlD)


class ServoE(port):

    def __init__(self, ServoE):
        super().__init__(ServoE)

    def servoControlE(val):
        txs = ""
        txs += str(val + 5)
        txs += 'e'
        serial.write(txs.encode())

    ui.servoE.valueChanged.connect(servoControlE)


class ServoF(port):

    def __init__(self, ServoF):
        super().__init__(ServoF)

    def servoControlF(val):
        txs = ""
        txs += str(val + 5)
        txs += 'f'
        serial.write(txs.encode())

    ui.servoF.valueChanged.connect(servoControlF)