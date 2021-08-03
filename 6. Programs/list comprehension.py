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
>>> 