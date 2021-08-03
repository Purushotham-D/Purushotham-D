Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1+j
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=1+j
NameError: name 'j' is not defined
>>> a=2+3j
>>> b=3+4j
>>> a
(2+3j)
>>> b
(3+4j)
>>> a+b
(5+7j)
>>> a-b
(-1-1j)
>>> a*b
(-6+17j)
>>> a/b
(0.72+0.04j)
>>> a%b
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a%b
TypeError: can't mod complex numbers.
>>> a//b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a//b
TypeError: can't take floor of complex number.
>>> a*a
(-5+12j)
>>> c=2+3i
SyntaxError: invalid syntax
>>> a='1'
>>> b='2'
>>> a+b
'12'
>>> a-b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(a.ljust)
Help on built-in function ljust:

ljust(width, fillchar=' ', /) method of builtins.str instance
    Return a left-justified string of length width.
    
    Padding is done using the specified fill character (default is a space).

>>> a='this is puruboi laptop'
>>> a
'this is puruboi laptop'
>>> print(a)
this is puruboi laptop
>>> a=""""purushotham's" laptop """
>>> a
'"purushotham\'s" laptop '
>>> print(a)
"purushotham's" laptop 
>>> b=len(a)
>>> b
23
>>> print(b)
23
>>> help (a.slipt)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    help (a.slipt)
AttributeError: 'str' object has no attribute 'slipt'
>>> help split
SyntaxError: invalid syntax
>>> help(a.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.

>>> a.split(sep='',maxsplit=2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.split(sep='',maxsplit=2)
ValueError: empty separator
>>> a.slpit
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.slpit
AttributeError: 'str' object has no attribute 'slpit'
>>> a.slpit()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.slpit()
AttributeError: 'str' object has no attribute 'slpit'
>>> d=a.split()
>>> d
['"purushotham\'s"', 'laptop']
>>> a.split(is)
SyntaxError: invalid syntax
>>> a
'"purushotham\'s" laptop '
>>> print(a.split(is))
SyntaxError: invalid syntax
>>> a.split('s)
	
SyntaxError: EOL while scanning string literal
>>> a.split('s')
['"puru', "hotham'", '" laptop ']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help (a.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> capitalize(a)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    capitalize(a)
NameError: name 'capitalize' is not defined
>>> a.capitalize(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.capitalize(a)
TypeError: capitalize() takes no arguments (1 given)
>>> caplitalize('a')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    caplitalize('a')
NameError: name 'caplitalize' is not defined
>>> d=a.capitalize()
>>> d
'"purushotham\'s" laptop '
>>> a="""" this is puruboi's laptop """
>>> a
'" this is puruboi\'s laptop '
>>> print(a)
" this is puruboi's laptop 
>>> a.capitalize()
'" this is puruboi\'s laptop '
>>> a='abcd'
>>> a.capitalize()
'Abcd'
>>> a
'abcd'
>>> help(center)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    help(center)
NameError: name 'center' is not defined
>>> help(a.center)
Help on built-in function center:

center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.
    
    Padding is done using the specified fill character (default is a space).

>>> a.center('d')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.center('d')
TypeError: 'str' object cannot be interpreted as an integer
>>> a.center('')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.center('')
TypeError: 'str' object cannot be interpreted as an integer
>>> a.center(2,'c')
'abcd'
>>> a.center(1,'dd')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.center(1,'dd')
TypeError: The fill character must be exactly one character long
>>> a.center(2,'e')
'abcd'
>>> a
'abcd'
>>> a.center(1,'')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.center(1,'')
TypeError: The fill character must be exactly one character long
>>> a.center(5,'w')
'wabcd'
>>> x='ABCD'
>>> x[0]
'A'
>>> x[1]
'B'
>>> x[3]
'D'
>>> x[5]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    x[5]
IndexError: string index out of range
>>> x[-1]
'D'
>>> x[-2]
'C'
>>> x[-3]
'B'
>>> x[-4]
'A'
>>> x[0:3:1]
'ABC'
>>> [-4:-1:1]
SyntaxError: invalid syntax
>>> [0:-1:1]
SyntaxError: invalid syntax
>>> x[-4:-1:1]
'ABC'
>>> [-1:-4:1]
SyntaxError: invalid syntax
>>> x[-1:-4:1]
''
>>> x[-1:-3:1]
''
>>> x[1:3:1]
'BC'
>>> x[1:4:1]
'BCD'
>>> x[-3:0:1]
''
>>> x[-3:-1:1]
'BC'
>>> a='abcdefghijklmnopqrstuvwxyz'
>>> len(a)
26
>>> a[0:27:2]
'acegikmoqsuwy'
>>> a[0:26:3]
'adgjmpsvy'
>>> a[0:25:2]
'acegikmoqsuwy'
>>> a[-1:-27:2]
''
>>> a[-1:-25:2]
''
>>> a[-1:-24:2]
''
>>> 
>>> a[-1:-23:1]
''
>>> a[-2:-23:-1]
'yxwvutsrqponmlkjihgfe'
>>> a[-2:-27:-1]
'yxwvutsrqponmlkjihgfedcba'
>>> a[-2-27:-2]
'abcdefghijklmnopqrstuvwx'
>>> a[-2:-26:-3]
'yvspmjgd'
>>> a[-1:-27:-2]
'zxvtrpnljhfdb'
>>> a[-1:-27:-1]
'zyxwvutsrqponmlkjihgfedcba'
>>> a[::-1]
'zyxwvutsrqponmlkjihgfedcba'
>>> a[::1]
'abcdefghijklmnopqrstuvwxyz'
>>> li=['ab',1,2.2,3+4j]
>>> li
['ab', 1, 2.2, (3+4j)]
>>> li[0]
'ab'
>>> li[1]
1
>>> li[4]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    li[4]
IndexError: list index out of range
>>> li[3]
(3+4j)
>>> li[-1:-3:1]
[]
>>> li[-1:-3:-1]
[(3+4j), 2.2]
>>> li[2:3:1]
[2.2]
>>> li[2:4:1]
[2.2, (3+4j)]
>>> li[::-1]
[(3+4j), 2.2, 1, 'ab']
>>> li[::1]
['ab', 1, 2.2, (3+4j)]
>>> dir(li)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(li.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> li.append(w,/)
SyntaxError: invalid syntax
>>> li.append('w')
>>> li
['ab', 1, 2.2, (3+4j), 'w']
>>> help(li.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Sort the list in ascending order and return None.
    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    
    The reverse flag can be set to sort in descending order.

>>> help(li.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> li.insert(2,'e')
>>> li
['ab', 1, 'e', 2.2, (3+4j), 'w']
>>> li.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    li.sort(reverse=True)
TypeError: '<' not supported between instances of 'complex' and 'str'
>>> li.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    li.sort(reverse=True)
TypeError: '<' not supported between instances of 'complex' and 'str'
>>> li.insert(-1,nav)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    li.insert(-1,nav)
NameError: name 'nav' is not defined
>>> li.insert(-2,'nav')
>>> li
['ab', 1, 'e', 2.2, 'nav', (3+4j), 'w']
>>> li=[1,2,3,4,5,6,10,9,27,11]
>>> li
[1, 2, 3, 4, 5, 6, 10, 9, 27, 11]
>>> li.sort(reverse=True)
>>> li
[27, 11, 10, 9, 6, 5, 4, 3, 2, 1]
>>> li.sort(reverse=False)
>>> li
[1, 2, 3, 4, 5, 6, 9, 10, 11, 27]
>>> help(li.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> li.extend(3)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    li.extend(3)
TypeError: 'int' object is not iterable
>>> li.extend([2,2,3])
>>> li
[1, 2, 3, 4, 5, 6, 9, 10, 11, 27, 2, 2, 3]
>>> li.append([2])
>>> li
[1, 2, 3, 4, 5, 6, 9, 10, 11, 27, 2, 2, 3, [2]]
>>> li1=[1,2,3,4]
>>> li.extend(li1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> li.extend([li1])
>>> li
[1, 2, 3, 4, 5, 6, 9, 10, 11, 27, 2, 2, 3, [2], [1, 2, 3, 4]]
>>> 
>>> a='abcd'
>>> a
'abcd'
>>> a1=a*3
>>> a1
'abcdabcdabcd'
>>> a2=a+3
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    a2=a+3
TypeError: can only concatenate str (not "int") to str
>>> a3=a/2
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a3=a/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> b='1234'
>>> a2=a*b
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    a2=a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> a1=a+b
>>> a1
'abcd1234'
>>> a/b
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    a/b
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> help(li.clear)
Help on built-in function clear:

clear() method of builtins.list instance
    Remove all items from list.

>>> 
>>> li.clear
<built-in method clear of list object at 0x0000027087F0B900>
>>> li
[1, 2, 3, 4, 5, 6, 9, 10, 11, 27, 2, 2, 3, [2], [1, 2, 3, 4]]
>>> li.
KeyboardInterrupt
>>> li.clear
<built-in method clear of list object at 0x0000027087F0B900>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> a='abcd'
>>> help(a.rfind)
Help on built-in function rfind:

rfind(...) method of builtins.str instance
    S.rfind(sub[, start[, end]]) -> int
    
    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> a.rfind(sub[2,start[3,end]])
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    a.rfind(sub[2,start[3,end]])
NameError: name 'sub' is not defined
>>> help(li.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> li.copy
<built-in method copy of list object at 0x0000027087F0B900>
>>> li
[1, 2, 3, 4, 5, 6, 9, 10, 11, 27, 2, 2, 3, [2], [1, 2, 3, 4]]
>>> li1=li.copy
>>> li1
<built-in method copy of list object at 0x0000027087F0B900>
>>> li1=li.copy()
>>> li1
[1, 2, 3, 4, 5, 6, 9, 10, 11, 27, 2, 2, 3, [2], [1, 2, 3, 4]]
>>> li1=li.clear()
>>> li1
>>> li
[]
>>> str='abcd'
>>> a.join'/'
SyntaxError: invalid syntax
>>> str.join(['a','/'])
'aabcd/'
>>> str=A,B,C,D
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    str=A,B,C,D
NameError: name 'A' is not defined
>>> x='abcd''
SyntaxError: EOL while scanning string literal
>>> x='abcd'
>>> list(x)
['a', 'b', 'c', 'd']
>>> '|'.join(list(x))
'a|b|c|d'
>>> a='abcdefghijk'
>>> list(a)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
>>> for i in range (len(list(a)):
		if (a[i]=='a'|'e'|'i'|'o'|'u'):
		
SyntaxError: invalid syntax
>>> help(li.find)
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    help(li.find)
AttributeError: 'list' object has no attribute 'find'
>>> help(a.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> 
>>> help(a.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> a='my name is puruboi'
>>> a1=a.count('i')
>>> a2=a.count('a')
>>> a1
2
>>> a3=count('e')
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    a3=count('e')
NameError: name 'count' is not defined
>>> 
>>> a3=a.count('e')
>>> a4=a.count('o')
>>> a5=a.count('u')
>>> a1
2
>>> a2
1
>>> a3
1
>>> a4
1
>>> a5
2
>>> a='my name is PURUSHOTHAM D'
>>> li=5
>>> li
5
>>> li=[1,2,2,3,4,4]
>>> li[3]=5
>>> li
[1, 2, 2, 5, 4, 4]
>>> tuple()
()
>>> li=t1()
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    li=t1()
NameError: name 't1' is not defined
>>> li==ti()
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    li==ti()
NameError: name 'ti' is not defined
>>> tuple(li)
(1, 2, 2, 5, 4, 4)
>>> 
>>>
