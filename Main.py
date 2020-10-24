from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import csv

import os
import time

# Install by calling "pip3 install pandas"
import pandas as pd
import json

# Install by calling "pip3 install numpy"
import numpy as np
import re

# Install by calling "pip3 install besutifulsoup4"
import requests
from bs4 import BeautifulSoup
    
# Path to the chromedriver executable, downloadable at https://chromedriver.chromium.org/downloads
PATH = "C:\\Users\\kurri\\Downloads\\chromedriver_win32\\chromedriver.exe" # change to relevant directory

Maint_url = [] #Conncatination of all values into a functional URL link for the Maintance page
TCO_url = [] #Conncatination of all values into a functional URL link for the TCO page
years_list = [] # Scraped from dropdown menu
makes_list = [] # Scraped from dropdown menu
temp_makes = []
makes_name_list = [] # Scraped from dropdown menu
models_list = [] # Scraped from dropdown menu
temp_models = []
models_name_list = [] # Scraped from dropdown menu
trims_list = [] # Scraped from dropdown menu
trims_name_list = [] # Scraped from dropdown menu
engines_list = [] # Scraped from dropdown menu
engines_name_list = [] # Scraped from dropdown menu
transmissions_list = [] # Scraped from dropdown menu
mileage_list = [] # Scraped from dropdown menu

# The heading for how the data will be formatted 
header_list = ['Maint_url', 'TCO_url', 'trim_id', 'trim_name', 'year', 'make_id', 'make_name', 'model_id', 'model_name', 'engine_id', 'engine_name', 'transmission'] 

dr = webdriver.Chrome(PATH)
x = 0
check1 = True
check2 = False
check3 = False
while(x == 0):
    try:
        url_google = "https://www.google.com/"
        url_google_scholar = "https://scholar.google.com/"
        url_duck_duck_go = "https://duckduckgo.com/"
        if(check1):
            val = input("Enter what you would like to search: ")
            dr.get(url_google)
            google_textbox = dr.find_element_by_class_name("gLFyf.gsfi")
            google_textbox.send_keys(val)
            google_textbox.send_keys(Keys.ENTER)
            google_links = dr.find_elements_by_class_name("yuRUbf")
            for links in google_links:
                links.click()
                 

        if(check2):
            val = input("Enter what you would like to search: ")
            dr.get(url_google_scholar)
            google_textbox = dr.find_element_by_class_name("gLFyf.gsfi")
            google_textbox.send_keys(val)
            google_textbox.send_keys(Keys.ENTER)

        if(check3):
            val = input("Enter what you would like to search: ")
            dr.get(url_duck_duck_go)
            google_textbox = dr.find_element_by_class_name("gLFyf.gsfi")
            google_textbox.send_keys(val)
            google_textbox.send_keys(Keys.ENTER)



    except Exception as e:
        print(e)

    
time.sleep(2)
dr.close()
