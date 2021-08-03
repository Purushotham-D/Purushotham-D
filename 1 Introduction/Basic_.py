# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:12:47 2020

@author: Puruboi
"""
#Numbers 
#int,float,complex
#strings
name='puruboi'
len(name)
#indexing
name[3]
name[2:8]
#negative indexing
name[-1]
name[-1:-8:-1]
name[-7:]

#list
#tuple
#dict
#set
#range
#type conversations

#python collections module
import collections as z
a=z.namedtuple('courses','name,technologu')
s= a('datascience','python')
print(s)

b=['e','d','u','r','k','a']
c=z.deque(b)
print(c)
c.append('python')
c.appendleft('x')
c.pop()
c.popleft()

A={1:'a',2:'b'}
B={3:'c',4:'d'}
A=z.ChainMap(A,B)
print(A)

d=[1,2,1,3,2,3,1,2,3,4,1,2,3,1,2,3,1,2,3]
count=z.Counter(d)
count

# refer and study all functions in collections

## Arrays

