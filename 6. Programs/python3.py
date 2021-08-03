Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li=[1,2,3,4,5]
>>> li
[1, 2, 3, 4, 5]
>>> li1=[1,'e']
>>> li1
[1, 'e']
>>> li2=(1,2,e,4)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    li2=(1,2,e,4)
NameError: name 'e' is not defined
>>> li=(1,2,3,4,5)
>>> l1
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
>>> type(li)
<class 'tuple'>
>>> li
(1, 2, 3, 4, 5)
>>> dir(li)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> str="this is a class"
>>> len(str.split(''))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    len(str.split(''))
ValueError: empty separator
>>> s='the the heheh hehe'
>>> str=len(s.split(''))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str=len(s.split(''))
ValueError: empty separator
>>> li1=len(s.split(' '))
>>> li1
4
>>> print(li1)
4
>>> di={'key':2}
>>> dir(di)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> w={1,2,3,4}
>>> w
{1, 2, 3, 4}
>>> di={'a':1,'b':2,'c':3}
>>> di(keys)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    di(keys)
NameError: name 'keys' is not defined
>>> help(di.keys)
Help on built-in function keys:

keys(...) method of builtins.dict instance
    D.keys() -> a set-like object providing a view on D's keys

>>> di.keys
<built-in method keys of dict object at 0x00000174F8C54440>
>>> print(di.keys)
<built-in method keys of dict object at 0x00000174F8C54440>
>>> di.values
<built-in method values of dict object at 0x00000174F8C54440>
>>> d1=di.keys
>>> d1
<built-in method keys of dict object at 0x00000174F8C54440>
>>> di.keys()
dict_keys(['a', 'b', 'c'])
>>> s1={1,2,3,4,5,5,6}
>>> s2={1,3,4,5,6,7,7}
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s2
{1, 3, 4, 5, 6, 7}
>>> e=di.items()
>>> e
dict_items([('a', 1), ('b', 2), ('c', 3)])
>>> dir(s1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7}
>>> s1.intersection(s2)
{1, 3, 4, 5, 6}
>>> s1-s2
{2}
>>> s2-s1
{7}
>>> for i in range(10)
SyntaxError: invalid syntax
>>> range(10)
range(0, 10)
>>> li[range(100]
   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> list(range(10)]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> list(range(101))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> list(range(1,101))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> range(1,101,2)
range(1, 101, 2)
>>> list(range(1,101,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> for i in range(10):
	print(i)

0
1
2
3
4
5
6
7
8
9
>>> li=[1,2,3,4,5,6,'r']
>>> li
[1, 2, 3, 4, 5, 6, 'r']
>>> for i in li:
	print(i)

	
1
2
3
4
5
6
r
>>> str='ABCD'
>>> for i in str:
	print(i)

	
A
B
C
D
>>> for i in 'ABCD'
SyntaxError: invalid syntax
>>> for i in 'ABCD':
	print(i)

	
A
B
C
D
>>> s='this is a class'
>>> for word in s:
	print(word)

	
t
h
i
s
 
i
s
 
a
 
c
l
a
s
s
>>> for i in s.split( ):
	print(i)

	
this
is
a
class
>>> a=dict()
>>> a[word]=s.count(word)
>>> a
{'s': 4}
>>> print(a)
{'s': 4}
>>> 
>>> a=dict()
\
>>> for i in s.split():
	print(word)
	a[i]=s.count(i)
	print(a)

	
s
{'this': 1}
s
{'this': 1, 'is': 2}
s
{'this': 1, 'is': 2, 'a': 2}
s
{'this': 1, 'is': 2, 'a': 2, 'class': 1}
>>> dir(li)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> for i in s.split():
	print(word)
	a[i]=s.split().count(i)
	print(a)

	
s
{'this': 1, 'is': 2, 'a': 2, 'class': 1}
s
{'this': 1, 'is': 1, 'a': 2, 'class': 1}
s
{'this': 1, 'is': 1, 'a': 1, 'class': 1}
s
{'this': 1, 'is': 1, 'a': 1, 'class': 1}
>>> for i in s.split():
	print(word)
	a[i]=s.count(i)
print(a)
SyntaxError: invalid syntax
>>> for i in s.split():
	print(word)
	a[i]=s.count(i)

	
s
s
s
s
>>> print(a)
{'this': 1, 'is': 2, 'a': 2, 'class': 1}
>>> a=dict()
for word in s.split():
	print(word)
	a[word]=s.split().count(word)
print(a)
SyntaxError: multiple statements found while compiling a single statement
>>> clear
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> s='this is a class,this is a python class'.lower()
>>> s
'this is a class,this is a python class'
>>> 
KeyboardInterrupt
>>>  s='This is a Class,this is a python class'.lower()
 
SyntaxError: unexpected indent
>>> s
'this is a class,this is a python class'
>>>  s='This is a Class,this is a python class'
 
SyntaxError: unexpected indent
>>> s='This is a Class,this is a python class'
>>> s
'This is a Class,this is a python class'
>>> s=s.lower()
>>> s
'this is a class,this is a python class'
>>> a=dict()
>>> for i in s.split():
	print(i)
	a[word]=s.split().count(word)
   print(a)
   
SyntaxError: unindent does not match any outer indentation level
>>> for i in s.split():
	print(i)
	a[word]=s.split().count(word)

this
is
a
class,this
is
a
python
class
>>> print(a)
{'s': 0}
>>> for i in s.split():
	print(i)
	a[word]=s.split().count(word)
print(a)
SyntaxError: invalid syntax
>>> for i in s.split():
	print(i)
	a[word]=s.split().count(word)
print(a)
SyntaxError: invalid syntax
>>> for i in s.split():
	print(i)
	a[word]=s.split().count(word)

this
is
a
class,this
is
a
python
class
>>> a
{'s': 0}
>>> for i in s.split():
	print(i)
	a[i]=s.split().count(word)

	
this
is
a
class,this
is
a
python
class
>>> for i in s.split():
	print(i)
	a[i]=s.split().count(i)

	
this
is
a
class,this
is
a
python
class
>>> a
{'s': 0, 'this': 1, 'is': 2, 'a': 2, 'class,this': 1, 'python': 1, 'class': 1}
>>> for i in s.split():
	print(i)
	a[word]=s.split().count(word)
print(a)
SyntaxError: invalid syntax
>>> 
>>> 
>>> for i in '!,.:;':
	s=s.replace(i,'')

	
>>> s
'this is a classthis is a python class'
>>> for i in '!,.:;':
	s=s.replace(i,' ')

	
>>> s
'this is a classthis is a python class'
>>> s= 'the rocking,joking,laughing,hen. the clas is interesting'
>>> for i in '!,.;':
	s=s.replace(i,' ')

>>> print(s)
the rocking joking laughing hen  the clas is interesting
>>> a=dict()
>>> for word in s.split():
	print(word)
	a[word]=s.split().count(word)

	
the
rocking
joking
laughing
hen
the
clas
is
interesting
>>> a
{'the': 2, 'rocking': 1, 'joking': 1, 'laughing': 1, 'hen': 1, 'clas': 1, 'is': 1, 'interesting': 1}
>>> s='this is a class,this is a python class'
>>> for i in '!,.;':
	s=s.replace(' ')

	
Traceback (most recent call last):
  File "<pyshell#146>", line 2, in <module>
    s=s.replace(' ')
TypeError: replace expected at least 2 arguments, got 1
>>> s=s.replace(i,' ')
>>> s
'this is a class,this is a python class'
>>> for i in '!,.;':
	s=s.replace(i,' ')

	
>>> s
'this is a class this is a python class'
>>> a=dict(_)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a=dict(_)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> a=dict()
>>> for word in set(s.split()):
	print(word)
	a[word]=s.split().count(word)

	
is
python
a
this
class
>>> print(a)
{'is': 2, 'python': 1, 'a': 2, 'this': 2, 'class': 2}
>>> 
>>> a={'this':1,'a':1,'class':1}
>>> for i in a:
	print(i)

	
this
a
class
>>> for i in a.items():
	print(i)

	
('this', 1)
('a', 1)
('class', 1)
>>> a.items()
dict_items([('this', 1), ('a', 1), ('class', 1)])
>>> c=[1,2,3,4]
>>> d=['a','b','c']
>>> for i,j in zip(c,d):
	print(i,',',j):
		
SyntaxError: invalid syntax
>>> for i,j in zip(c,d):
	print(i,',',j)

	
1 , a
2 , b
3 , c
>>> zip(c,d)
<zip object at 0x00000174F8CE0B80>
>>> list(zip(c,d))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> for i,j in a.items():
	print(i,',',j)

	
this , 1
a , 1
class , 1
>>> help zip()
SyntaxError: invalid syntax
>>> help zip
SyntaxError: invalid syntax
>>> 
>>> 
>>> d=[1,2,3,4,5,6]
>>> dir(a)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help (a.popitem)
Help on built-in function popitem:

popitem() method of builtins.dict instance
    Remove and return a (key, value) pair as a 2-tuple.
    
    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.

>>> a=dict{'a':1,'b':2,'c':1}
SyntaxError: invalid syntax
>>> a={'a':1,'b':2,'c':1}
>>> a.popitem('a':1)
SyntaxError: invalid syntax
>>> 