import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
o = 0
class window(QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        loadUi("supersearcher.ui", self)
        self.darkMode.clicked.connect(self.darkModeToggle)
        self.pushButton.clicked.connect(self.sendQuery)
        self.radioButtonG.pressed.connect(self.sendEngine)
        self.radioButtonGS.pressed.connect(self.sendEngine)
        self.radioButtonD.pressed.connect(self.sendEngine)
        self.radioButtonB.pressed.connect(self.sendEngine)
        self.setStyleSheet("background-color: #FFFFFF")
        self.darkMode.setIcon(QIcon("Darkmode_Inactive.svg"))
        self.settings.setIcon(QIcon("Settings_Inactive.svg"))
        self.queryInput.setStyleSheet("background-color: #dddddd;"
                                      "font: 32pt Oswald;")
    def darkModeToggle(self, o):
        o = o + 1
        if o == 2: #dark mode on
            self.darkMode.setIcon(QIcon('Darkmode_DMode.svg'))
            self.settings.setIcon(QIcon("Settings_DMode.svg"))
            self.setStyleSheet("background-color: #2c2f33")
            self.queryInput.setStyleSheet("background-color: rgb(64, 68, 72);"
"font: 32pt Oswald;")
        if o == 1: #dark mode off
            self.darkMode.setIcon(QIcon('Darkmode_Inactive.svg'))
            self.settings.setIcon(QIcon("Settings_Inactive.svg"))
            self.setStyleSheet("background-color: #FFFFFF")
            self.queryInput.setStyleSheet("background-color: #dddddd;"
                                          "font: 32pt Oswald;")
    def sendQuery(self):
        query = self.queryInput.text()
            # engine = self.radioButtonG.text()
        # if self.radioButtonGS.ischecked():
        #     engine = self.radioButtonGS.text()
        # if self.radioButtonD.ischecked():
        #     engine = self.radioButtonD.text()
        # if self.radioButtonB.ischecked():
        #     engine = self.radioButtonB.text()
        print(query)
        # print(engine)
    def sendEngine(self):
        engine = self.sender().text()
        print(engine)



app=QApplication(sys.argv)
mainwindow=window()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
app.exec_()