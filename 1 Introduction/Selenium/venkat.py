# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:01:48 2020

@author: gkvenkat

# -*- coding: utf-8 -*-
"""
"""
Created on Sun Dec  1 09:43:02 2019

@author: Priyanka Zoya
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
#import sqlite3
#import pandas as pd
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
    
driver = webdriver.Chrome(chrome_options=options)
url='https://www.amazon.com/dp/B07XTWYNYB/ref=sspa_dk_detail_0?pd_rd_i=B07XTWYNYB&pd_rd_w=xS4pR&pf_rd_p=c83c55b0-5d97-454a-a592-a891098a9709&pd_rd_wg=NJYtL&pf_rd_r=CNKATC7YKTMV82A09R5T&pd_rd_r=2049e8e6-d132-4e37-834e-a34c431b77b3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTkJZSzVSRUw3MFJPJmVuY3J5cHRlZElkPUEwNzIzNTkwMUNTR0hJOFBMNkxSRyZlbmNyeXB0ZWRBZElkPUExMDQzMDI2MUhCRVBQRDdMUEQ1SCZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'
driver.get(url)
# time.sleep(5)
# driver.close()


'''
to fetch urls of related products
'''
   
xpath_page_count = '(//h2[text()="Sponsored products related to this item"])[1]/following::span[@class="a-carousel-page-count"][1]'
count = int(Inputhandler.readText(driver,xpath_page_count).strip().split()[-1])
    
xpath_next_button='(//h2[text()="Sponsored products related to this item"])[1]/following::span[@class="a-button-inner"][2]'    
xpath_links='(//h2[@class="a-spacing-micro"]/preceding::a[@class="a-link-normal adReviewLink a-text-normal"])[{}]'
list_urls=[]
for j in range(count):
    for i in range(1,100):
        links = Inputhandler.getAttribute(driver,xpath_links.format(i),"href")
        print(links)
        if links == None:
            Inputhandler.mouseClick(driver,xpath_next_button)
            time.sleep(5)
            break
        list_urls.append(links)
    
required_urls = set(list_urls)