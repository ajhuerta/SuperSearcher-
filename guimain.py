import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
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
        self.label.setStyleSheet("background-color: #FFFFFF")
        self.darkMode.setIcon(QIcon("Darkmode_Inactive.svg"))
        self.settings.setIcon(QIcon("Settings_Inactive.svg"))
        self.queryInput.setStyleSheet("background-color: #dddddd;"
                                      "font: 32pt Oswald;")
        self.settings.clicked.connect(self.openSettings)
    def darkModeToggle(self, o):
        o = o + 1
        if o == 2: #dark mode on
            windowbg = "background-color: #2c2f33;" "transition: 0.3s;"
            self.darkMode.setIcon(QIcon('Darkmode_DMode.svg'))
            self.settings.setIcon(QIcon("Settings_DMode.svg"))
            self.queryInput.setStyleSheet("background-color: rgb(64, 68, 72);"
"font: 32pt Oswald;")
        if o == 1: #dark mode off
            windowbg = "background-color: #FFFFFF"
            self.darkMode.setIcon(QIcon('Darkmode_Inactive.svg'))
            self.settings.setIcon(QIcon("Settings_Inactive.svg"))
            self.queryInput.setStyleSheet("background-color: #dddddd;"
                                          "font: 32pt Oswald;")
        self.label.setStyleSheet(windowbg)
        self.setStyleSheet(windowbg)
    def sendQuery(self):
        query = self.queryInput.text()
        print(query)
    def sendEngine(self):
        engine = self.sender().text()
        print(engine)
    def openSettings(self):
        # self.label.setStyleSheet("background-color: transparent")
        self.label.lower()
        self.pushButton_2.clicked.connect(self.closeSettings)
    def closeSettings(self):
        self.label.raise_()
# class settingsMenu(QDialog):
#     def __init__(self):
#         super(settingsMenu,self).__init__()
#         loadUi("settings.ui",self)
#         self.buttonBox.accepted.connect(self.goBack)
#     def goBack(self):
#         widget.addWidget(window())
#         widget.setCurrentIndex(widget.currentIndex()+1)

app=QApplication(sys.argv)
mainwindow=window()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(700)
widget.setFixedWidth(800)
widget.show()
app.exec_()