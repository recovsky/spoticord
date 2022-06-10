from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import time
import os
import threading
from creator import creator

class Ui_FirstScreen(object):
    def setupUi(self, FirstScreen):
        FirstScreen.resize(680, 400)
        FirstScreen.setMinimumSize(QtCore.QSize(0, 0))
        FirstScreen.setMaximumSize(QtCore.QSize(680, 400))
        self.FirstPageWidget = QtWidgets.QWidget(FirstScreen)
        self.FirstPageWidget.setObjectName("FirstPageWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.FirstPageWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FirstPageFrame = QtWidgets.QFrame(self.FirstPageWidget)
        self.FirstPageFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FirstPageFrame.setStyleSheet("QFrame {\n"
        "    background-color: rgb(56,58,89);\n"
        "    color: rgb(220,220,220);\n"
        "    border-radius: 10px;\n"
        "}")
        self.FirstPageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FirstPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FirstPageFrame.setObjectName("FirstPageFrame")
        self.DescriptionLabel = QtWidgets.QLabel(self.FirstPageFrame)
        self.DescriptionLabel.setGeometry(QtCore.QRect(0, 120, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.DescriptionLabel.setFont(font)
        self.DescriptionLabel.setStyleSheet("color: rgb(98,114,164)")
        self.DescriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DescriptionLabel.setObjectName("DescriptionLabel")
        self.LoadingBar = QtWidgets.QProgressBar(self.FirstPageFrame)
        self.LoadingBar.setGeometry(QtCore.QRect(70, 260, 531, 23))
        self.LoadingBar.setStyleSheet("QProgressBar {\n"
        "    background-color: rgb(98,114,164);\n"
        "    color: rgb(200,200,200);\n"
        "    border-style: none;\n"
        "    border-radius: 10px;\n"
        "    text-align: center;\n"
        "}\n"
        "QProgressBar::chunk{\n"
        "    border-radius: 10px;\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255))\n"
        "};\n"
        "")
        self.LoadingBar.setProperty("value", 0)
        self.LoadingBar.setObjectName("LoadingBar")
        self.LoadingBar.setMaximum(100)   
        self.LoadingLabel = QtWidgets.QLabel(self.FirstPageFrame)
        self.LoadingLabel.setGeometry(QtCore.QRect(0, 300, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton = QtWidgets.QPushButton(self.FirstPageFrame)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(98,114,164);\n"
        "    color: rgb(200,200,200);\n"
        "    border-style: none;\n"
        "    border-radius: 10px;\n"
        "    text-align: center;\n"
        "}\n"
        "QPushButton::chunk{\n"
        "    border-radius: 10px;\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255))\n"
        "};\n"
        "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.move(290, 340)
        self.pushButton.clicked.connect(lambda: self.button_on_click())
        self.LoadingLabel.setFont(font)
        self.LoadingLabel.setStyleSheet("color: rgb(98,114,164)")
        self.pushButton2 = QtWidgets.QPushButton(self.FirstPageFrame)
        self.pushButton2.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.pushButton2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(98,114,164);\n"
"    color: rgb(200,200,200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255))\n"
"};\n"
"")
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(lambda: self.button2_on_click())
        self.NumberInput = QtWidgets.QLineEdit(self.FirstPageFrame)
        self.NumberInput.setGeometry(QtCore.QRect(200, 150, 261, 41))
        self.NumberInput.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(98,114,164);\n"
"text-align: center")
        self.NumberInput.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberInput.setObjectName("NumberInput")
        FirstScreen.setCentralWidget(self.FirstPageWidget)
        self.LoadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoadingLabel.setObjectName("LoadingLabel")
        self.DescriptionLabel_2 = QtWidgets.QLabel(self.FirstPageFrame)
        self.DescriptionLabel_2.setGeometry(QtCore.QRect(0, 50, 661, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.DescriptionLabel_2.setFont(font)
        self.DescriptionLabel_2.setStyleSheet("color: rgb(98,114,164)")
        self.DescriptionLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.DescriptionLabel_2.setObjectName("DescriptionLabel_2")
        self.verticalLayout.addWidget(self.FirstPageFrame)
        FirstScreen.setCentralWidget(self.FirstPageWidget)
        self.retranslateUi(FirstScreen)
        QtCore.QMetaObject.connectSlotsByName(FirstScreen)
        self.NumberInput.hide()
        self.NumberInput.move(200, 180)
        self.pushButton2.hide()

    def retranslateUi(self, FirstScreen):
        _translate = QtCore.QCoreApplication.translate
        FirstScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        FirstScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        FirstScreen.setWindowTitle(_translate("FirstScreen", "MainWindow"))
        self.DescriptionLabel.setText(_translate("FirstScreen", "<strong>Spotify Tool</strong>"))
        self.LoadingLabel.setText(_translate("FirstScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Loading...</span></p></body></html>"))
        self.DescriptionLabel_2.setText(_translate("FirstScreen", "<strong>SpotiCord</strong>"))
        self.pushButton.setText(_translate("FirstWindow", "Start"))
        self.pushButton2.setText(_translate("FirstWindwo", "Generate"))

    def button_on_click(self):
        self.LoadingBar.setMaximum(100)
        for i in range(101):
            time.sleep(0.005)
            self.LoadingBar.setValue(i)
        if(self.LoadingBar.value() == 100):
            self.LoadingBar.hide()
            self.pushButton.hide()
            self.LoadingLabel.hide()
            self.NumberInput.show()
            self.pushButton2.show()

    def button2_on_click(self):
        veri = int(self.NumberInput.text())
        for x in range(veri):
                t = threading.Thread(target=creator)
                t.start()
        print("[+] Created!")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstScreen = QtWidgets.QMainWindow()
    ui = Ui_FirstScreen()
    ui.setupUi(FirstScreen)
    FirstScreen.show()
    sys.exit(app.exec_())
