# -*- coding: utf-8 -*-
"""
Title: Practical step towards panda lib 
Created on Thu Mar 19 11:23:14 2020

@author: Puruboi
"""

import pandas as pd   # import the lib panda as pd 
pd.__version__    # version of pandas 
dir(pd)    # gives the list of function in pd for acessing and manipulation 

# Example-1 data frame declaration using dictionary  
df= pd.DataFrame({'names':['amith','roshan','raj'],'mob':[24214134,1433555,5457684546768]})
print(df)
# Example-2
df_1=pd.DataFrame({'alphabets':list(chr(i) for i in range(65,91)),'postion':list(range(1,27))})
# or 
df_2 = pd.DataFrame({'alpha':list(map(chr,range(65,65+26))),'pos':list(range(1,27))})
# operations on df
df['alphabets']
df['postion'] 
df[df['postion']>=10]  
df['alphabets'] [(df['postion']>=10) & (df['postion']<=21)]
# addding another coloumn
df['lower']=df['alphabets'].apply(str.lower)
# getting only required 2 col out of 3
df[['alphabets','postion']]


# Example-3

df_3 = pd.DataFrame({'A':[1,2,3],'C':[6,7,8]})

df1 = pd.DataFrame({'B':[4,5,6],'C':[4,3,2]})


df_k = pd.DataFrame({'Names':['Pu','Pr','Gi'],'marks':[67,78,89]})

df_e = pd.DataFrame({'Names':['Pu','Pr','Gi'],'marks':[97,58,99]})

df_s = pd.DataFrame({'Names':['Pu','Pr','Gi'],'marks':[87,68,69]})

# example-4 

d=pd.Series([1,2,3,4])

d_1=pd.Series([10,20,30,40],index=['2015 sales','2016 sales','2017 sales','2017 sales'],name='product A')


