# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:37:18 2019

@author: ms_am
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
import pandas as pd
import sqlite3
import Inputhandler




# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='amazon.log', level=logging.INFO)

# setting options for chrome driver
options = Options()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--disable-infobars')
options.add_argument('--start-fullscreen')
options.add_argument("--disable-popup-blocking")



def info(msg1='',msg2='',msg3=''):
    logging.info(str(msg1)+str(msg2)+str(msg3))
    print(msg1,msg2,msg3)


info("<amazon>  trying to connecting to url", ' at ',time.ctime())
    
url = "https://www.amazon.in/s?k=mobiles&ref=nb_sb_noss_2"
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

header="(//h2)[{}]"
rating ="(//h2/following::span[@class='a-icon-alt'])[{}]"
price = '(//span[@class="a-price-whole"])[{}]'
for i in range(1,26):
    xpath_header = header.format(i)
    print(i,'-->',Inputhandler.readText(driver,xpath_header),end = " -- ")
    xpath_rating = rating.format(i)
    print(Inputhandler.getAttribute(driver,xpath_rating,"innerHTML"),end=' -- ')
    xpath_price = price.format(i)
    print(Inputhandler.readText(driver,xpath_price))
  