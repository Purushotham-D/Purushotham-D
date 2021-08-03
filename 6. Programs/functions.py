Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i=list()
>>> d=[1,2,3,4,5]
>>> a=[i for i in range(10)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> ord('a')
97
>>> help(ord)
Help on built-in function ord in module builtins:

ord(c, /)
    Return the Unicode code point for a one-character string.

>>> char(97)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    char(97)
NameError: name 'char' is not defined
>>> chr(97)
'a'
>>> ord(A)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord(A)
NameError: name 'A' is not defined
>>> ord('A')
65
>>> a=([i for i in range(chr(90))])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a=([i for i in range(chr(90))])
TypeError: 'str' object cannot be interpreted as an integer
>>> chr(65)
'A'
>>> chr(65,90)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    chr(65,90)
TypeError: chr() takes exactly one argument (2 given)
>>> a= [chr(97) for in range(10)]
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> a= [chr(97) for  i in range(10)]
>>> a
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
>>>  a= [chr(97) for  i in range(10,1)]
 
SyntaxError: unexpected indent
>>> 
>>> a=[chr(i) for i in range(97,97+26)]
>>> a
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> a=[chr(i) for i in range(65,97+26)]
>>> a
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> a={chr(i):i  for i in range(97,97+26)]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> a={chr(i):i  for i in range(97,97+26)}
>>> a
{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> a={chr(i):i for i in range(65,97+26)}
>>> a
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> a={chr(i):i,chr(j):j for i in range(zip((65,90),(97,97+26)))}
SyntaxError: invalid syntax
>>> a={chr(i):i,chr(j):j for i in range(zip(65,97+26))}
SyntaxError: invalid syntax
>>> a={chr(i):i,chr(j):j  for i,j in range(zip(65,90),(97,97+26))}
SyntaxError: invalid syntax
>>> a={chr(i):i,chr(j):j  for i,j in range
   
SyntaxError: invalid syntax
>>> dir(a)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(a.update)
Help on built-in function update:

update(...) method of builtins.dict instance
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

>>> a={chr(i):i  for i in range(97,97+26)}
>>> d={chr(j):j  for j in range(65,90)}
>>> d.update(a)
>>> e=d.update(a)
>>> e
>>> print(d.update(a))
None
>>> a
{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> d
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> a={chr(i):i  for i in range(97,97+26)}
>>> d={chr(i):i  for i in range(65,65+26)}
>>> d
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90}
>>> a
{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> d.update(a)
>>> d
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> e={chr(i):i for i in range (list(range(65,65+26))+list(range(97,97+26)))}
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    e={chr(i):i for i in range (list(range(65,65+26))+list(range(97,97+26)))}
TypeError: 'list' object cannot be interpreted as an integer
>>> e={chr(i):i for i in (list(range(65,65+26))+list(range(97,97+26)))}
>>> e
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> e={chr(i):i for i in (set(range(65,65+26)).union(set(range(97,97+26)))}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> e={chr(i):i for i in (set(range(65,65+26)).union(set(range(97,97+26))))}
>>> e
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> f={chr(i):i for i in (set(range(65,65+26)).intersection(set(range(97,97+26))))}
>>> f
{}
>>> f={chr(i):i for i in (set(range(65,65+26)).union(set(range(97,97+26)))).intersection(set(range(0,125))}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> f={chr(i):i for i in (set(range(65,65+26)).union(set(range(97,97+26)))).intersection(set(range(0,125)))}
>>> f
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
>>> def welcome():
	print('welcome to beasant')

	
>>> welcome()
welcome to beasant
>>> welcome('puruboi')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    welcome('puruboi')
TypeError: welcome() takes 0 positional arguments but 1 was given
>>> def welcome(Name):
	print('welcome',name,' to beasant')

	
>>> welcome('puruboi')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    welcome('puruboi')
  File "<pyshell#66>", line 2, in welcome
    print('welcome',name,' to beasant')
NameError: name 'name' is not defined
>>> welcome(puruboi)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    welcome(puruboi)
NameError: name 'puruboi' is not defined
>>> welcome('puruboi')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    welcome('puruboi')
  File "<pyshell#66>", line 2, in welcome
    print('welcome',name,' to beasant')
NameError: name 'name' is not defined
>>> def welcome(Name):
	print('welcome',Name,' to beasant')

	
>>> welcome('puruboi')
welcome puruboi  to beasant
>>> def pi():
	return(22/7)

>>> pi()
3.142857142857143
>>> def pi(acc):
	return(((22/7)*(10**acc)/1)/10**acc)

>>> pi(3)
3.142857142857143
>>> pi(1000)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    pi(1000)
  File "<pyshell#78>", line 2, in pi
    return(((22/7)*(10**acc)/1)/10**acc)
OverflowError: int too large to convert to float
>>> pi(12)
3.142857142857143
\
>>> def pi(acc):
	return(((22/7)*(10**acc)/1)/(10**acc))

>>> pi(3)
3.142857142857143
>>> def pi(acc):
	return(((22/7)*(10**acc))/(10**acc))

>>> pi(3)
3.142857142857143
>>> def pi(acc):
	return(((22/7)*(10**acc)//1)/(10**acc))

>>> pi(3)
3.142
>>> def cir_details(rad):
	a=(2*pi(3)*(r**2))
	c=(2*pi(3)*r)
	d=(2*r)
	return d{}
SyntaxError: invalid syntax
>>> def cir_details(rad):
	a=(2*pi(3)*(r**2))
	c=(2*pi(3)*r)
	d=(2*r)
	return d={}
SyntaxError: invalid syntax
>>> def cir_details(rad):
	a=(2*pi(3)*(r**2))
	c=(2*pi(3)*r)
	d=(2*r)
	return
d={cir_details(rad)}
SyntaxError: invalid syntax
>>> def cir_details(rad):
	a=(2*pi(3)*(r**2))
	c=(2*pi(3)*r)
	d=(2*r)
	return

>>> d=dict{cir_details}
SyntaxError: invalid syntax
>>> d={cir_details}
>>> 
>>> d
{<function cir_details at 0x0000027D8379A310>}
>>> print(d)
{<function cir_details at 0x0000027D8379A310>}
>>> def cir_details(rad):
	d=dict()
	d['area']=(2*pi(3)*(r**2))
	d['circumference']=(2*pi(3)*r)
	d[diameter]=(2*r)
	d[radidus]=r
	return

>>> cir_details(3)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    cir_details(3)
  File "<pyshell#107>", line 3, in cir_details
    d['area']=(2*pi(3)*(r**2))
NameError: name 'r' is not defined
>>> def cir_details(rad):
	d=dict()
	d['area']=(2*pi(3)*(rad**2))
	d['circumference']=(2*pi(3)*rad)
	d[diameter]=(2*rad)
	d[radidus]=rad
	return

>>> cir_details(3)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    cir_details(3)
  File "<pyshell#110>", line 5, in cir_details
    d[diameter]=(2*rad)
NameError: name 'diameter' is not defined
>>> cir_details(3)def cir_details(rad):
	d=dict()
	d['area']=(2*pi(3)*(rad**2))
	d['circumference']=(2*pi(3)*rad)
	d[diameter]=(2*rad)
	d[radidus]=rad
	return