import sys
import random
import cv2 as cv
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bagaruto")


        self.signe = None
        self.hpDif = 0
        self.vid = cv.VideoCapture(0)
        self.frameAttack = 30
        self.posMain = (300,300)

        self.timechr = QtCore.QTime(0,0,5,0)
        self.chrono = QtWidgets.QLabel("no time")
        self.chrono.setText(self.timechr.toString("ss:zz"))

        self.image1 = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.image2 = QtWidgets.QLabel("Hello World",
                                       alignment=QtCore.Qt.AlignCenter)
        self.hpBar2 = QtWidgets.QProgressBar()
        self.hpBar2.setValue(100)
        self.hpBar1 = QtWidgets.QProgressBar()
        self.hpBar1.setValue(100)

        self.imagefor2 = cv.imread("punching_ball.jpg")
        ret, image = self.vid.read()
        self.imagefor2 = cv.resize(self.imagefor2,(image.shape[1],image.shape[0]))
        self.image2.setPixmap(QtGui.QPixmap.fromImage(
            QtGui.QImage(self.imagefor2.data, self.imagefor2.shape[1], self.imagefor2.shape[0], QtGui.QImage.Format_BGR888)))

        self.layout = QtWidgets.QVBoxLayout(self)
        self.Hlayout = QtWidgets.QHBoxLayout(self)
        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.chrono)

        self.subLayoutG = QtWidgets.QVBoxLayout(self)
        self.subLayoutG.addWidget(self.hpBar1)
        self.subLayoutG.addWidget(self.image1)
        self.Hlayout.addLayout(self.subLayoutG)

        self.subLayoutD = QtWidgets.QVBoxLayout(self)
        self.subLayoutD.addWidget(self.hpBar2)
        self.subLayoutD.addWidget(self.image2)
        self.Hlayout.addLayout(self.subLayoutD)


        self.timerCam = QtCore.QTimer()
        self.timerCam.timeout.connect(self.actualize_image)
        self.timerCam.start(1000/30)

        self.timerSign = QtCore.QTimer()
        self.timerSign.timeout.connect(self.do_attack)
        self.timerSign.start(5000)

        self.timerChr = QtCore.QTimer()
        self.timerChr.timeout.connect(self.update_chr)
        self.timerChr.start(10)

    @QtCore.Slot()
    def actualize_image(self):
        ret,image = self.vid.read()
        if(self.frameAttack<15):
            self.signe = cv.resize(self.signe, (round(self.signe.shape[1] * 0.55)*2, round(self.signe.shape[0] * 0.55)*2))
            posY = int(self.posMain[0]-(self.signe.shape[0]/2))
            posX = int(self.posMain[1]- (self.signe.shape[1]/2))
            image[posY:posY+self.signe.shape[0], posX:posX+self.signe.shape[1]] = self.signe
            self.frameAttack = self.frameAttack + 1
        elif(self.frameAttack < 30):
            image2copy = self.imagefor2.copy()
            self.signe = cv.resize(self.signe,
                                   (round(self.signe.shape[1] * 0.45) * 2, round(self.signe.shape[0] * 0.45) * 2))
            posY = int(self.posMain[0] - (self.signe.shape[0] / 2))
            posX = int(self.posMain[1] - (self.signe.shape[1] / 2))
            image2copy[posY:posY + self.signe.shape[0], posX:posX + self.signe.shape[1]] = self.signe
            self.frameAttack = self.frameAttack + 1
            self.image2.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(image2copy.data, image2copy.shape[1], image2copy.shape[0], QtGui.QImage.Format_BGR888)))
            self.frameAttack = self.frameAttack + 1
        elif(self.frameAttack < 32):
            self.image2.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(self.imagefor2.data, self.imagefor2.shape[1], self.imagefor2.shape[0],
                             QtGui.QImage.Format_BGR888)))
            if(self.hpBar2.value()-self.hpDif>0):
                self.hpBar2.setValue(self.hpBar2.value()-self.hpDif)
            else:
                self.hpBar2.setValue(0)
                self.timerChr.stop()
                self.timerSign.stop()
                self.timechr.setHMS(0,0,5,0)
                self.chrono.setText(self.timechr.toString("ss:zz"))
                messBox = QtWidgets.QMessageBox()
                messBox.setWindowTitle("Victoire")
                messBox.setText("You beat a punching ball!")
                if (messBox.exec()):
                    self.hpBar2.setValue(100)
                    self.timerChr.start(10)
                    self.timerSign.start(5000)
            self.frameAttack = self.frameAttack + 1
        self.image1.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_BGR888)))

    @QtCore.Slot()
    def do_attack(self):
        self.timechr.setHMS(0, 0, 5, 0)
        self.chrono.setText(self.timechr.toString("ss:zz"))
        ret, image = self.vid.read()
        self.posMain, classe = (300,300),""

        if classe == "boeuf":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "cheval":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "chevre":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "chien":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "cochon":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "lapin":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "oiseau":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "rat":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "serpent":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "singe":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        elif classe == "tigre":
            self.signe = 0
            self.frameAttack = 0
            self.hpDif = 0
        else:
            self.signe = cv.imread("rasengan.jpg")
            self.frameAttack = 0
            self.hpDif = 50

        self.signe = cv.resize(self.signe, (round(image.shape[1] * 0.1), round(image.shape[0] * 0.1)))

    @QtCore.Slot()
    def update_chr(self):
        ms = self.timechr.msec()
        s = self.timechr.second()
        print(s)
        print(ms)
        if ms==0:
            if s!= 0:
                ms = 990
                s =s-1
        else:
            ms = ms - 10
        self.timechr.setHMS(0,0,s,ms)
        self.chrono.setText(self.timechr.toString("ss:z"))







def main():
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
    return 0

main()
