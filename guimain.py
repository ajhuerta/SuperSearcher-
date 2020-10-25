import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
o = 0
blacklist = []
engine = 'Google'
tabs = '5' # these are the default values of all the settings
keepHistory = 'Yes'
query = ''
class window(QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        loadUi("supersearcher.ui", self)
        blacklist = []
        self.darkMode.clicked.connect(self.darkModeToggle)
        self.pushButton.clicked.connect(self.sendQuery)
        self.radioButtonG.pressed.connect(self.sendEngine)
        self.radioButtonGS.pressed.connect(self.sendEngine)
        self.radioButtonD.pressed.connect(self.sendEngine)
        self.radioButtonB.pressed.connect(self.sendEngine)
        self.radioButton1.pressed.connect(self.sendTabs)
        self.radioButton2.pressed.connect(self.sendTabs)
        self.radioButton3.pressed.connect(self.sendTabs)
        self.radioButton4.pressed.connect(self.sendTabs)
        self.radioButton5.pressed.connect(self.sendTabs)
        self.radioButtonCom.pressed.connect(self.sendDomains)
        self.radioButtonEdu.pressed.connect(self.sendDomains)
        self.radioButtonGov.pressed.connect(self.sendDomains)
        self.radioButtonOrg.pressed.connect(self.sendDomains)
        self.radioButtonNet.pressed.connect(self.sendDomains)
        self.radioYes.pressed.connect(self.keepHistory)
        self.radioNo.pressed.connect(self.keepHistory)
        self.setStyleSheet("background-color: #FFFFFF") # this is so the program starts in light mode
        self.label.setStyleSheet("background-color: #FFFFFF")
        self.darkMode.setIcon(QIcon("Darkmode_Inactive.svg"))
        self.settings.setIcon(QIcon("Settings_Inactive.svg"))
        self.queryInput.setStyleSheet("background-color: #dddddd;"
                                      "font: 32pt Oswald;") # light mode in input box
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
    def keepHistory(self):
        keepHistory = str(self.sender().text()) # takes the text of the radio button, i.e Yes or No
        print(keepHistory)
    def sendDomains(self): # makes/modifies the blacklist of domains
        print('t')
        ext = self.sender().text()
        if ext not in blacklist:
            blacklist.append(ext)
        else:
            blacklist.remove(ext)
        print(blacklist)
        return blacklist
    def sendEngine(self): # grabs the search engine chosen by user live
        engine = self.sender().text()
        print(engine)
    def sendQuery(self): # grabs the text from the input field once the search button is pressed
        query = self.queryInput.text()
        print(query)
    def sendTabs(self): # grabs the preferred number of tabs specified by user, in an integer form
        tabs = int(self.sender().text())
        print(tabs)
    def openSettings(self): # reveals settings options, sends the box thats blocking the settings to the back of the gui
        self.label.lower()
        self.pushButton_2.clicked.connect(self.closeSettings)
    def closeSettings(self): # hides settings by sending the blocking box up to the front of the gui, and confirms correct execution by printing string after
        self.label.raise_()
        print('settings confirmed')

app=QApplication(sys.argv)
mainwindow=window()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(700)
widget.setFixedWidth(800)
widget.show()
app.exec_()