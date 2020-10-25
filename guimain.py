import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import csv
from os import system
import time
from datetime import date, datetime
# Path to the chromedriver executable, downloadable at https://chromedriver.chromium.org/downloads
PATH = "chromedriver.exe" # change to relevant directory
with open('history.csv', mode='w', encoding='utf-8') as history_log:
    history_writer = csv.writer(history_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    history_writer.writerow(['Query', 'Engine', 'Tabs', 'Date', 'Time'])
o = 0
blacklist = []
engine = 'DuckDuckGo'
tabs = 5 # these are the default values of all the settings
keepHistory = 'Yes'
query = ''
dr = webdriver.Chrome(PATH)
date = date.today().strftime("%m/%d/%y")
time = datetime.now().strftime('%H:%M:%S')
class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        loadUi("supersearcher.ui", self)
        self.blacklist = []
        self.tabs = 5
        self.engine = 'Google'
        self.keepHistory = 'True'
        self.query = ' '
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
        self.radioYes.pressed.connect(self.checkHistory)
        self.radioNo.pressed.connect(self.checkHistory)
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
            windowbg = "background-color: #2c2f33;"
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

    def checkHistory(self):
        self.keepHistory = str(self.sender().text()) # takes the text of the radio button, i.e Yes or No

    def sendDomains(self): # makes/modifies the blacklist of domains
        ext = self.sender().text()
        if ext not in self.blacklist:
            self.blacklist.append(ext)
        else:
            self.blacklist.remove(ext)

    def openSettings(self): # reveals settings options, sends the box thats blocking the settings to the back of the gui
        self.label.lower()
        self.pushButton_2.clicked.connect(self.closeSettings)

    def closeSettings(self): # hides settings by sending the blocking box up to the front of the gui, and confirms correct execution by printing string after
        self.label.raise_()

    def sendTabs(self): # grabs the preferred number of tabs specified by user, in an integer form
        self.tabs = int(self.sender().text())

    def sendEngine(self): # grabs the search engine chosen by user live
        self.engine = self.sender().text()

    def sendQuery(self): # grabs the text from the input field once the search button is pressed
        self.query = self.queryInput.text()
        i = 0
        #These are the base URLS for all of the search engines.
        url_google = "https://www.google.com/search?q="
        url_google_scholar = "https://scholar.google.com/scholar?q="
        url_duck_duck_go = "https://duckduckgo.com/?q="
        url_bing = "https://www.bing.com/search?q="
        url_search = ""
        #If the google engine is selected, this code will execute
        if(self.engine == "Google"):
            #This replaces all spaces that the user inputs and converts it into + signs to create a functionable URL
            url_search = url_google + self.query.replace(" ", "+")
            dr.get(url_search)
            #This line locates all of the links within the first page that relates to the user's search
            google_links = dr.find_elements_by_class_name("yuRUbf")
            for links in google_links:
                i = i + 1
                # Creates an actionchain that will create a new window tab for every link within the page
                if i < 5:
                    actions = ActionChains(dr)
                    actions \
                        .move_to_element(links) \
                        .key_down(Keys.CONTROL) \
                        .key_down('t') \
                        .click(links) \
                        .key_up(Keys.CONTROL) \
                        .key_up('t') \
                        .perform()
        if(self.engine == "Google Scholar"):
            url_search = url_google_scholar + self.query.replace(" ","+")
            dr.get(url_search)
            google_scholar_links = dr.find_elements_by_xpath('//*[@id="gs_res_ccl_mid"]')
            count = 0   
            for links in google_scholar_links:
                # Creates an actionchain that will create a new window tab after all dropdown menus are filled                                 
                i = i + 1
                if i < self.tabs + 1:
                    actions = ActionChains(dr)
                    actions \
                        .move_to_element(links) \
                        .key_down(Keys.CONTROL) \
                        .key_down('t') \
                        .click(links) \
                        .key_up(Keys.CONTROL) \
                        .key_up('t') \
                        .perform()
        if(self.engine == "DuckDuckGo"):
            url_search = url_duck_duck_go + self.query.replace(" ","+")
            dr.get(url_search)
            duck_duck_go_links = dr.find_elements_by_class_name("result__a")
            count = 0
            for links in duck_duck_go_links:
                i = i + 1
                if i < self.tabs + 1:
                    actions = ActionChains(dr)
                    actions \
                        .move_to_element(links) \
                        .key_down(Keys.CONTROL) \
                        .key_down('t') \
                        .click(links) \
                        .key_up(Keys.CONTROL) \
                        .key_up('t') \
                        .perform()
                # Creates an actionchain that will create a new window tab after all dropdown menus are filled                                 


        if(self.engine == "Bing"):
            url_search = url_bing + self.query.replace(" ","+")
            dr.get(url_search)
            bing_links = dr.find_elements_by_tag_name('h2')
            count = 0
            for links in bing_links:
                # Creates an actionchain that will create a new window tab after all dropdown menus are filled                                 
                i = i + 1
                if i < self.tabs + 1:
                    actions = ActionChains(dr)
                    actions \
                        .move_to_element(links) \
                        .key_down(Keys.CONTROL) \
                        .key_down('t') \
                        .click(links) \
                        .key_up(Keys.CONTROL) \
                        .key_up('t') \
                        .perform()
        self.logData()
    def logData(self):
        query = self.query
        engine = self.engine
        tabs = self.tabs
        with open('history.csv', mode='a', encoding='utf-8') as history_log:
            history_writer = csv.writer(history_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            history_writer.writerow([query, engine, tabs, date, time])
app=QApplication(sys.argv)
mainwindow=window()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(700)
widget.setFixedWidth(800)
widget.setWindowTitle('Super Searcher')
widget.show()
app.exec_()