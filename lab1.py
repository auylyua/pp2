#pyton home
print("Hello, World!")

#pyton intro
print("Hello, World!")

#python getting started
import sys #To check the Python version of the editor, you can find it by importing the 'sys' module:
print(sys.version) # the result is -> 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

#python syntax
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") #The number of spaces has to be at least one
        
#python comments
"""
This is a comment
written in
more than just one line
"""
#or with hastag
print("Hello, World!")

#python variables
x = 5
y = "John"
print(type(x)) # the result is -> <class 'int'>
print(type(y)) # the result is -> <class 'str'>

#variables names
"""Variable names in Python must start with a letter or an underscore, can only contain letters, digits, and underscores, are case-sensitive, and cannot be a reserved keyword.
Variable names in Python cannot start with a number, contain spaces or special characters (except underscores), or use reserved keywords."""
my_var = "John"
myvar = "John" 
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#assigning multiple variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #apple
print(y) #banana
print(z) #cherry

#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Global Variables
x = "awesome" #this is a global variable

def myfunc():
  x = "fantastic" #this is a local variable
  print("Python is " + x)

myfunc() #result -> "Python is fantastic"

print("Python is " + x) #result -> "Python is awesome"

#Python Data Types
"""Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""
x = str("Hello World")	
x = int(20)	
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

#Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Python Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Python Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Slicing Strings
b = "Hello, World!"
print(b[-5:-2]) #output -> orl

#Modify Strings
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concatenate Strings
a = "Hello"
b = "World"
c = a + b
print(c) #output -> HelloWorld

#Format Strings
price = 59
txt = f"The price is {price} dollars"
print(txt) #output -> The price is 59 dollars

#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
a = " Hello, World! "
print(a.strip())  # Output: "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))  # Output: "Jello, World!"
a = " Hello, World! "
print(a.strip())  # Output: "Hello, World!"