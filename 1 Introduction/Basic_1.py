Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=1
>>> g=lambda x:x*x*x
>>> print(g(4))
64
>>> li=[5,7,22,97,54,62,77,23,73}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> li=[5,7,22,97,54,62,77,23,73]
>>> f=list(map(lambda x:x*2,li))
>>> print(f)
[10, 14, 44, 194, 108, 124, 154, 46, 146]
>>> map(lambda x:x*2,li))
SyntaxError: unmatched ')'
>>> map(lambda x:x*2,li)
<map object at 0x00000232B7E09EE0>
>>> [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [[1 if i+j==2 else 0 for i in range(3)]for j in range(3)]
[[0, 0, 1], [0, 1, 0], [1, 0, 0]]
>>> from itertools import cycle
>>> values = cycle([0, 1])
>>> [[next(values) for i in range(8)] for j in range(8)]
[[0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1]]
>>> [[1 if (i|j==0)||(i|j==4)) else 0 for in range(5)]for j in range (5)]
SyntaxError: invalid syntax
>>> [[1 if (i|j==0)|(i|j==4)) else 0 for in range(5)]for j in range (5)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> [[1 if ((i|j==0)|(i|j==4)) else 0 for in range(5)]for j in range (5)]
SyntaxError: invalid syntax
>>> [[1 if (i|j==0)|(i|j==4) else 0 for in range(5)]for j in range (5)]
SyntaxError: invalid syntax
>>> 
>>> [[1 if (i|j==0)|(i|j==4) else 0 for i in range(5)]for j in range (5)]
[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]
>>> [[1 if (i==0|j==0)|(i==4|j==4) else 0 for i in range(5)]for j in range (5)]
[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
>>> [[1 if (i==0 or j==0) or (i==4 or j==4) else 0 for i in range(5)]for j in range (5)]
[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
>>> [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
  File "<pyshell#22>", line 1, in <listcomp>
    [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
  File "<pyshell#22>", line 1, in <listcomp>
    [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
ZeroDivisionError: integer division or modulo by zero
>>> [[0 if (i%j==0) else 1 for i in range(5)]for j in range (5)]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    [[0 if (i%j==0) else 1 for i in range(5)]for j in range (5)]
  File "<pyshell#23>", line 1, in <listcomp>
    [[0 if (i%j==0) else 1 for i in range(5)]for j in range (5)]
  File "<pyshell#23>", line 1, in <listcomp>
    [[0 if (i%j==0) else 1 for i in range(5)]for j in range (5)]
ZeroDivisionError: integer division or modulo by zero
>>> [[0 if (i%j=0) else 1 for i in range(5)]for j in range (5)]
SyntaxError: invalid syntax
>>> [[1 if (i%j!=0) else 0 for i in range(8)]for j in range (8)]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    [[1 if (i%j!=0) else 0 for i in range(8)]for j in range (8)]
  File "<pyshell#25>", line 1, in <listcomp>
    [[1 if (i%j!=0) else 0 for i in range(8)]for j in range (8)]
  File "<pyshell#25>", line 1, in <listcomp>
    [[1 if (i%j!=0) else 0 for i in range(8)]for j in range (8)]
ZeroDivisionError: integer division or modulo by zero
>>> [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
  File "<pyshell#26>", line 1, in <listcomp>
    [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
  File "<pyshell#26>", line 1, in <listcomp>
    [[1 if (i%j==0) else 0 for i in range(5)]for j in range (5)]
ZeroDivisionError: integer division or modulo by zero
>>> [[1 if (i%2!=0) else 0 for i in range(8)]for j in range (8)]
[[0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1]]
>>> [[1 if (i%2!=0) else 0 for i in range(4)]for j in range (4)]
[[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]]
>>> [[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]][[1 if (i%2!=0) else 0 for i in range(4)]for j in range (4)]
SyntaxError: invalid syntax
>>> 
>>> ([[1 if (i%2!=0) else 0 for i in range(4)]for j in range (4)])
[[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]]
>>> ([1 if (i%2!=0) else 0 for i in range(4)]for j in range (4))
<generator object <genexpr> at 0x00000232B7DFECF0>
>>> (([1 if (i%2!=0) else 0 for i in range(4)]for j in range (4)))
<generator object <genexpr> at 0x00000232B7E5EDD0>
>>> tuple(([1 if (i%2!=0) else 0 for i in range(4)]for j in range (4)))
([0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1])
>>> prime_list = [x for x in range(10, 11) for y in range(2,x) if x % x == 0 and x % 1 == 0 and x % y != 0]
>>> list(prime_list)
[10, 10, 10, 10, 10, 10]
>>> prime_list = [x for x in range(10, 111) for y in range(2,x) if x % x == 0 and x % 1 == 0 and x % y != 0]
>>> list(prime_list)

>>> prime_list = [x for x in range(10, 31) for y in range(2,x) if x % x == 0 and x % 1 == 0 and x % y != 0]
>>> list(prime_list)
[10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
>>> 