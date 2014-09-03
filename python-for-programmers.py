# Sample file with different examples for each common programming feature

# python principles - Zen of Python
import this

print('Hello word!') # printing

# math ops
2 + 2
2 * 3

# _ (underscore) returns the last return value in REPL

# identation for block delimitation, python programmers use 4 spaces but the interpreter accepts any consistent white space number as identation - don't mix tabs with spaces, better use spaces
for i in range(5):
    x = i * 10
    print(x)

# PEP - Python enhancements proposals - they are documents that guide the development of Python language. PEP 8 for example explains the rules of identation

import math # importing modules

math.sqrt(81) # square root
help # looking for help inside the REPL
help(math) # help for the module math
help(math.sqrt) # help for the math.sqrt()

math.sqrt(math.pi) * math.sqrt(math.pi) # simple math operation

# if you do
from math import sqrt # you import the sqrt() from module math
# so you can type just sqrt instead of math.sqrt:
sqrt(math.pi) * sqrt(math.pi)

# if you do
from math import sqrt, pi # you import the sqrt() and the pi() from module math
# so you can type just sqrt and pi instead of math.sqrt and math.pi:
sqrt(pi) * sqrt(pi)

# you can also create aliases
from math import factorial as fac
fac(8) # same as math.fac(8) after import as, this is not recommended in general and should be used thoughtfully

# / does division while // does the division and convert result to integer
10 / 2 # returns a float 5.0
10 // 2 # returns an integer 5
5 / 2 # returns 2.5
5 // 2 # returns 2

# str() converts things to string
str(5 // 2) # converts integer to string

# scalar types and values - int, float, NoneType (the null object), bool

#int
10 # normal int
0b10 # binary
0o10 # octal
0x10 # hex
int(3.5) # 3
int(0b10) # 2
int("6") # convert string to integer

#float
3.15
3e8
1.616e-35
float(2) # 2.0
float(2.0) # same as 2.0
float("1.4") # generate float from int
float("nan") # not a number value
float("inf") # infinite value
float("-inf") # infinite value

#none
None # null value, dont return anything on the REPL
a = None
a is None # returns True

# Bool
True
False
bool(0) # False
bool(42) # True
bool(0.0) # False
bool(-1) # True
bool([]) # False
bool("") # False
bool("Spam") # True
bool("False") # True

# Relational operation ==, !=, <, >, <=, >=
g = 20
g == 20 # True
g == 13 # False
g != 20 # False and so on

# Conditional statements
if True:     # dont forget the : at the end!!!
    print("It is true")

if 2 > 1:
    print("two is bigger than one")

if bool("hey"):
    print("yeah!!!")

if "hey":  # auto convert the expression as bool(expression)
    print("hey!!")


# if else
if 2 > 1:
    print("2 bigger than 1")
else:
    print("2 not bigger than 1")

# multiples elses:
if 1 > 2:
    print("1 bigger than 2")
elif 2 > 1:
    print("2 is bigger than 1")
else:
    print("none of them")

# while loops
c = 0
while c != 5:
    print(c)
    c += 1

while True:
    if 1 == 1:
       break;

# strings - they are utf-8
'Word 1'
"Word 2"
'Ho' "He" 'He' # concatenates to HoHeHe
""" This is
a multiline
String"""
''' This is also a 
multiline string'''
# \n in Python translates to the correct \n for windows or unix
# RAW STRING
print(r'\n') # will print "\n" and not a new line because it is a raw string

# bytes - accept basically the same methods as strings
d = b'some bytes'


# list - mutable sequences of objects
[1, 3, 5]
a = ["el1", "2", "3"]
a = ["el1", "2", "3",] # also works
a[0]
a[2]
b = [] # empty list
b.append("a")
list("char") #  ['c','h','a','r']

# dics
d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# for-each
#for item in ieterable:

# functions
def square(x):
    return x*x
# module codes are only executed once when imported

def square(x=2): # default param 2
    return x*x

glb_var = 0
b = 0
def glb_function(a):
    global glb_var
    b = a
    glb_var = a
glb_function(10)
print(b) # 0
print(glb_var) # 10
' ',join(['a', 'b', 'c']) # 'a b c'
"i.am.here".partition('.') # ('i', 'am', 'here')

departure, separator, arrival = "London:Edinburgh".partition(':')
departure # London
separator # :
arrival # Edinburgh

origin, _, destination = "Seattle-Boston".partition('-') # _ to discard the separator used as dummy value

"Math constants: pi={m.pi}, e={m.e}".format(m=math)

a = [0, 1, 3] 
a[-1] # returns 3, avoid to use a[len(a) - 1]
a[:2] # [0, 1]
a[2:] # [3]
b = a[:] # copies the whole list


a = [0, 3, 9] 
a.index(9) # 2 -> returned the index of the element 9
