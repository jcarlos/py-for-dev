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

