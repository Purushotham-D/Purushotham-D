# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:40:52 2020

@author: Anonymous
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
import logging
import time
import pandas as pd
import Inputhandler

# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='Kproxy.log', level=logging.INFO)
# importing the config file
config = configparser.RawConfigParser()
config.read('Kproxy.properties')

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

info("<Kproxy>  trying to connecting to url")
    
url = config.get('url', 'url')

for i in range(5):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    
        
    def mouseClickandSendKey(driver,controlxpath,value):
        try:
            controlClick=driver.find_element_by_xpath(controlxpath)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
            controlClick.click()
            controlClick.clear()
            time.sleep(1)
            controlClick.send_keys(value)
        except Exception as timout:
            logger.info('%s - %s - %s', "Unable to find the Xpath mouseClickandSendKey ",controlxpath,timout)