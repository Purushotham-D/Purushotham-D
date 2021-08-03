Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='the is a class room'
>>> s
'the is a class room'
>>> a=dict()
>>> for word in s.split():
	print(word)
	a{word}=s.split().count(word)
	
SyntaxError: invalid syntax
>>> for word in s.split():
	print(word)
	a[word]=s.split().count(word)

	
the
is
a
class
room
>>> a
{'the': 1, 'is': 1, 'a': 1, 'class': 1, 'room': 1}
>>> s='the is a class room'
>>> s='the is a class class classs rooom room'
>>> for word in s.split():
	print(word)
	a[word]=s.split().count(word)

	
the
is
a
class
class
classs
rooom
room
>>> a
{'the': 1, 'is': 1, 'a': 1, 'class': 2, 'room': 1, 'classs': 1, 'rooom': 1}
>>> s='the is a class class class room room'
>>> for word in s.split():
	print(word)
	a[word]=s.split().count(word)

	
the
is
a
class
class
class
room
room
>>> a
{'the': 1, 'is': 1, 'a': 1, 'class': 3, 'room': 2, 'classs': 1, 'rooom': 1}
>>> i=0
>>> whiel i<10:
	
SyntaxError: invalid syntax
>>> while i<10:
	i+=1
	else:
		
SyntaxError: invalid syntax
>>> while i<10:
	i+=1
else:
	i-=0

	
>>> i
10
>>> i=20
>>> while i<10:
	i+=1
else:
	i-=0

	
>>> i=
SyntaxError: invalid syntax
>>> i
20
>>> while i<10:
	i+=1
else:
	i-=1

	
>>> i
19
>>> a=range(-1,11)
>>> a
range(-1, 11)
>>> aa=list(range(-1,11))
>>> aa
[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> aa=list(range(10,1,-1))
>>> aa
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> aa=list(range(10,-1,-1))
>>> aa
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> l=['A','B','c']
>>> i=[1,2,3]
>>> for i,j in range(len(l)):
	print(list(l[i]:i[j]))
	
SyntaxError: invalid syntax
>>> i1=[1,2,3]
>>> for i,j in range(len(l)):
	print(list(l[i]:i1[j]))
	
SyntaxError: invalid syntax
>>> for i,j in range(len(l)):
	print((l[i]':'i1[j]))
	
SyntaxError: invalid syntax
>>> for i,j in range(len(l)):
	print(l[i],':',i1[j])

	
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    for i,j in range(len(l)):
TypeError: cannot unpack non-iterable int object
>>> for i,j in range(len(l)and len(i1)):
	print(l[i],':',i1[j])

	
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    for i,j in range(len(l)and len(i1)):
TypeError: cannot unpack non-iterable int object
>>> for i in range(len(l)):
	print(l[i],':',i1[i])

	
A : 1
B : 2
c : 3
>>> list(zip(l,i1))
[('A', 1), ('B', 2), ('c', 3)]
>>> for i,j in zip(l,i1):
	print(i,'---->',j)

	
A ----> 1
B ----> 2
c ----> 3
>>> for i,j in zip(l,i1):
	print(dict(i,'---->',j))

	
Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    print(dict(i,'---->',j))
TypeError: dict expected at most 1 argument, got 3
>>> for i,j in zip(l,i1):
	a=dict(i,'---->',j))
	
SyntaxError: unmatched ')'
>>> for i,j in zip(l,i1):
	a=dict(i,'---->',j)

	
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    a=dict(i,'---->',j)
TypeError: dict expected at most 1 argument, got 3
>>> for i,j in zip(l,i1):
	a=(i,'---->',j)

	
>>> a
('c', '---->', 3)
>>> d=dict(zip(l,i1))
>>> d
{'A': 1, 'B': 2, 'c': 3}
>>> d.items()
dict_items([('A', 1), ('B', 2), ('c', 3)])
>>> 
>>> [0]*10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> 0 for i in range(10)
SyntaxError: invalid syntax
>>> 0 for i in range(10):
	
SyntaxError: invalid syntax
>>> i=0 for i in range(10):
	
SyntaxError: invalid syntax
>>> [0 for i range(10)]
SyntaxError: invalid syntax
>>> [0 for i in range(10)]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> [[0 for i in range(3)]*3]
[[0, 0, 0, 0, 0, 0, 0, 0, 0]]
>>> [[0 for i in range(3)]for j in range(3)]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> [[i for i in range(3)]for j in range(3)]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
>>> [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
>>> [[i for i in range(3)],i+1 for j in range(3)]
SyntaxError: invalid syntax
>>> [[i for i in range(3)]:
 
SyntaxError: invalid syntax
>>> [[i+(j*3) for i in range(3)] for j in range(3)]
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
>>> [0 for i in range(5)] for j in range(5)]
SyntaxError: invalid syntax
>>> [0 for i in range(5)]for j in range(5)]
SyntaxError: invalid syntax
>>> [[0 for i in range(3)]for j in range(3)]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> [[0 for i in range(5)]for j in range(5)]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> [0 for i in range(5) if i%2]
[0, 0]
>>> [0 for i in range(5)]
[0, 0, 0, 0, 0]
>>> [0 for i in range(5) if i%2==0]
[0, 0, 0]
>>> [0 for i in range(5) if i%2==1]
[0, 0]
>>> [0 if i%2==0 else 1 for i in range(5)]
[0, 1, 0, 1, 0]
>>> [0 if i%2=0 else 1 for i in range(5)]
SyntaxError: invalid syntax
>>> [0 if i%2==1 else 0 for i in range(5)]
[0, 0, 0, 0, 0]
>>> [0 if i%2==0 else 1 for i in range(5)]
[0, 1, 0, 1, 0]
>>> {i:i**2 for i in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}{i:i*2 for i in range(10)}
SyntaxError: invalid syntax
>>> {i:i*2 for i in range(10)}
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
>>> 
>>> def greet():
	print('hi')
	print('welcome')
	print(' ')

	
>>> greet()
hi
welcome
 
>>> def pi()
SyntaxError: invalid syntax
>>> def pi():
	return(3.143)

>>> pi()
3.143
>>> print(greet())
hi
welcome
 
None
>>> print(pi())
3.143
>>> a=greet()
hi
welcome
 
>>> print(a)
None
>>> a
>>> import math
>>> defdef greet('name'):
	print('hi')
	print('welcome')
	print('name')
	
SyntaxError: invalid syntax
>>> defdef greet('name'):
	print('hi')
	print('welcome')
	print(name)
	
SyntaxError: invalid syntax
>>> def greet('name'):
	print('hi')
	print('welcome')
	print(name)
	
SyntaxError: invalid syntax
>>> def greet(name):
	print('hi')
	print('welcome')
	print(name)

	
>>> greet('puruboi')
hi
welcome
puruboi
>>> def greet(name):
	print('hi')
	print('welcome')
	print(name)
	return name.capitalise()

>>> greet(puruboi)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    greet(puruboi)
NameError: name 'puruboi' is not defined
>>> greet('puruboi')
hi
welcome
puruboi
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    greet('puruboi')
  File "<pyshell#131>", line 5, in greet
    return name.capitalise()
AttributeError: 'str' object has no attribute 'capitalise'
>>> def greet(name):
	print('hi')
	print('welcome')
	print(name)
	return name.capitalize()

>>> greet('puruboi')
hi
welcome
puruboi
'Puruboi'
>>> print(greet())
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    print(greet())
TypeError: greet() missing 1 required positional argument: 'name'
>>> print(greet(puruboi))
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    print(greet(puruboi))
NameError: name 'puruboi' is not defined
>>> print(greet('puruboi'))
hi
welcome
puruboi
Puruboi
>>> ### TO FIND NUMBER OF TIMES THE WORDS PRESENT IN A LOOP
##s="A tale is a story, especially one that's full of creative embellishments. You can read a tale from a book, or tell a bedtime tale to the kids you're babysitting."
##for i in s.split():
##    if (i==',.;?&!./\:^*'):
##        s=s.replace(' ')
##        s=s.lower(s)
##        print(s)
##a=dict()
##for word in s.split():
##    print(word)
##    a[word]=s.split().count(word)
##print(a)
##
#tuple([[1 if i+j==2 else 0 for i in range(3)]for j in range(3)])

