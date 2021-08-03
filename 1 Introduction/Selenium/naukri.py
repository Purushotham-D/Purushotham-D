# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:50:57 2019

@author: amith_ms
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
import logging
import time
import pandas as pd
import Inputhandler


# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='myntra.log', level=logging.INFO)
# importing the config file
config = configparser.RawConfigParser()
config.read('naukrirconfig.properties')

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


info("<naukri>  trying to connecting to url")
    
url = config.get('url', 'url')

for i in range(5):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    
    try:
        Inputhandler.mouseClick(driver, config.get('xpath', 'login'))
        Inputhandler.mouseClickandSendKey(driver,config.get('xpath', 'email.id'),config.get('data', 'username'))
        Inputhandler.mouseClickandSendKey(driver,config.get('xpath', 'login.password'),config.get('data', 'password'))
        Inputhandler.mouseClick(driver, config.get('xpath', 'login.button'))
    except Exception as e:
        print('no login required')
    try:
        Inputhandler.mouseClick(driver, config.get('xpath', 'skip.paid.version'))
    except Exception as e:
        print('no adds')
     
    Inputhandler.mouseClick(driver, config.get('xpath', 'update.profile'))
    Inputhandler.mouseClick(driver, config.get('xpath', 'edit.profile'))
    Inputhandler.mouseClickandSendKey(driver,config.get('xpath', 'text.area'),config.get('data', 'headline'))
    Inputhandler.mouseClick(driver, config.get('xpath', 'profile.save'))
    time.sleep(3)
    driver.close()
    print("Profile Updated")
    info("Profile Updated")






