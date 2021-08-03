# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 06:27:27 2019

@author: ms_am
"""

import sqlite3
import time

conn = sqlite3.connect('tutorial.db')



c = conn.cursor()

def create_table():
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(index_value REAL, datestamp TEXT, value REAL)')
    c.close()

def data_entry():
    c = conn.cursor()
    c.execute('INSERT INTO stuffToPlot VALUES(145, "2019-30-07",09876)')
    conn.commit()
    c.close()
    
def data_entry_1(val):
    c = conn.cursor()
    query = 'INSERT INTO stuffToPlot VALUES('+str(val)+', "2019-30-07",09876)'
    c.execute(query)
    conn.commit()
    c.close()
    
def close_db_connection():
    c.close()
    conn.close()
    
def read_from_db():
    c = conn.cursor()
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)
    c.execute('SELECT * FROM stuffToPlot')
    for row in c.fetchall():
        print(row)
    c.close()

def dynamic_data_entry(index,date,value):
    c = conn.cursor()
    c.execute('INSERT INTO stuffToPlot (value,  datestamp , index_value ) VALUES(?,?,?)',(index,date,value))
    conn.commit()
    c.close()


dynamic_data_entry(1,'1 dec 2019',56789)
#create_table()
#data_entry()
#read_from_db()
read_from_db()
#for i in range(1,11):
#    data_entry_1(i)
def data_entry(val):
    for i in range(1,101):
        c = conn.cursor()
        query = 'INSERT INTO stuffToPlot VALUES({}, "01-12-2019",{})'.format(i,i**2)
        c.execute(query)
        conn.commit()
        c.close()


for i in range(200,301):
    dynamic_data_entry(i**3,time.ctime(),i)

import time
time.time()
