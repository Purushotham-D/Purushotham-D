# DEMO_21
# python_programing
# dir
# help

# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:
# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview

x = "Hello World" 	                          # str 	
x = 20 	                                      #int 	
x = 20.5 	                                    #float 	
x = 1j 	                                      #complex 	
x = ["apple", "banana", "cherry"] 	          #list 	
x = ("apple", "banana", "cherry") 	          #tuple 	
x = range(6) 	                                #range 	
x = {"name" : "John", "age" : 36} 	          #dict 	
x = {"apple", "banana", "cherry"} 	          #set 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	
x = True 	                                    #bool 	
x = b"Hello" 	                                #bytes 	
x = bytearray(5) 	                            #bytearray 	
x = memoryview(bytes(5)) 	                    #memoryview

x = str("Hello World") 	                      #str 	
x = int(20) 	                                #int 	
x = float(20.5) 	                            #float 	
x = complex(1j) 	                            #complex 	
x = list(("apple", "banana", "cherry")) 	    #list 	
x = tuple(("apple", "banana", "cherry")) 	    #tuple 	
x = range(6) 	                                #range 	
x = dict(name="John", age=36) 	              #dict 	
x = set(("apple", "banana", "cherry")) 	      #set 	
x = frozenset(("apple", "banana", "cherry")) 	#frozenset

# Convert from one type to another:
x = 1 # int
y = 2.8 # float
z = 1j # complex
# convert from int to float:
a = float(x)
# convert from float to int:
b = int(y)
# convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c)) 

# Random Number: Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers
import random
print(random.randrange(1,10)) 

# Specify a Variable Type
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
# casting in python is therefore done using constructor functions:
# int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 

# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function
a = "Hello"
print(a)
# multiple line 
# triple double codes 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
# triple single codes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string
# Use negative indexes to start the slice from the end of the string
# The len() function returns the length of a string

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

## To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Check if the phrase "ain" is NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 

# To concatenate, or combine, two strings you can use the + operator.
# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
## You will get an error if you use double quotes inside a string that is surrounded by double quotes:
#       txt = "We are the so-called "Vikings" from the north."

# To fix this problem, use the escape character \"
## The escape character allows you to use double quotes when you normally would not be allowed:
  # txt = "We are the so-called \"Vikings\" from the north."
  
  \' 	Single Quote 	
\\ 	  Backslash 	
\n 	  New Line 	
\r 	  Carriage Return 	
\t 	  Tab 	
\b 	  Backspace 	
\f 	  Form Feed 	
\ooo 	Octal value 	
\xhh 	Hex value

# string methods 
capitalize()	Converts the first character to upper case
casefold()	  Converts string into lower case
center()	    Returns a centered string
count()	      Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	  Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	      Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	      Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	  Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	  Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle() 	  Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	      Joins the elements of an iterable to the end of the string
ljust()	      Returns a left justified version of the string
lower()	      Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	  Returns a translation table to be used in translations
partition()	  Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	      Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	      Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	      Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	      Returns a trimmed version of the string
swapcase()	  Swaps cases, lower case becomes upper case and vice versa
title()	      Converts the first character of each word to upper case
translate()	  Returns a translated string
upper()	      Converts a string into upper case
zfill()	      Fills the string with a specified number of 0 values at the beginning

# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

# Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))
# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
# Arithmetic operators
 + 	Addition 	x + y 	
 - 	Subtraction 	x - y 	
 * 	Multiplication 	x * y 	
 / 	Division 	x / y 	
 % 	Modulus 	x % y 	
 ** 	Exponentiation 	x ** y 	
 // 	Floor division 	x // 
 
 # Assignment operators
 # Comparison operators
 # Logical operators
 # Identity operators
 # Membership operators
 # Bitwise operators
 
# string and multipication operator
y=('#-'*10,'-#'*10)

# The symmetric difference of two sets A and B is the set of elements that are in either A or B, but not in their intersection.
# syntax of symmetric_difference() is:
  # syntax: A.symmetric_difference(B)
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print(A.symmetric_difference(C))
print(B.symmetric_difference(C))

# List is a collection which is ordered and changeable. Allows duplicate members.
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# syntax: range(start, stop, step) 
# You access the list items by referring to the index number
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

a=list(range(1,10,1))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# You can loop through the list items by using a for loop
Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
  
# To determine if a specified item is present in a list use the in keyword
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
  
# Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To add an item at the specified index, use the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# the remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist 

# The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join two list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) 

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1) 

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) 

# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.
  # syntax: set.difference(set)
z=set(range(1,10,1))
# You can get the data type of any object by using the type() function
type(a)
type(z)
z.difference(a)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset) 

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
# Add Items
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add multiple items to a set, using the update() method:
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset) 

# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) 

# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.

# Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) 

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items.
# There are other methods that joins two sets and keeps ONLY the duplicates, or NEVER the duplicates, check the full list of set methods in the bottom of this page

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

# set methods 
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Create and print a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets
# Get the value of the "model" key:
x = thisdict["model"]
# There is also a method called get() that will give you the same result
# Get the value of the "model" key:
x = thisdict.get("model")

# Change the "year" to 2018:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x) 
  
# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
  
# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y) 
 
# Check if "model" is present in the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
  
 # To determine how many items (key-value pairs) a dictionary has, use the len() method.
 # Print the number of items in the dictionary:
print(len(thisdict))

# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

# Or, if you want to nest three dictionaries that already exists as dictionaries:
# Create three dictionaries, than create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

# The dict() Constructor
It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# dictionary methods 
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

# Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 
 
# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) 

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Using the tuple() method to make a tuple:
  thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
  print(thistuple)

# Tuple Methods
# Python has two built-in methods that you can use on tuples.
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

#These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement" is written by using the if keyword
a = 33
b = 200
if b > a:
  print("b is greater than a")

# In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

# One line if statement:
if a > b: print("a is greater than b")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B") 

# You can also have multiple else statements on the same line:
# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 

# The and keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


