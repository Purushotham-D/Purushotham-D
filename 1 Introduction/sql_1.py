# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:41:18 2020

@author: Anonymous
"""
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT *C:\Users\Anonymous\Downloads\Microsoft.SkypeApp_kzf8qxf38zg5c!App\All\african_crises.csv')

cursor.execute('''
                INSERT INTO TestDB.dbo.Person (Name)
                ''')
conn.commit()