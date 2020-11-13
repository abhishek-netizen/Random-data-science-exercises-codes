Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # string in python
>>> str1 = "python"
>>> type(str1)
<class 'str'>
>>> str2 = 'hello'
>>> type(str2)
<class 'str'>
>>> # accesssing characters
>>> str1
'python'
>>> str1[2]
't'
>>> str1[4]
'o'
>>> # accessing range of elements
>>> str1[1:3]
'yt'
>>> str1[1:]
'ython'
>>> str1[:2]
'py'
>>> str1[:]
'python'
>>> str1[-1]
'n'
>>> str1[1:-2]
'yth'
>>> str1[4:-5]
''
>>> str1[::1]
'python'
>>> str1[1:-2]
'yth'
>>> str1[4:-5:-1]
'oht'
>>> str1[::-1]
'nohtyp'
>>> 'nohtyp'
'nohtyp'
>>> str[::]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    str[::]
TypeError: 'type' object is not subscriptable
>>> str[::2]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    str[::2]
TypeError: 'type' object is not subscriptable
>>> str1[::2]
'pto'
>>> str1[::3]
'ph'
>>> str1[1::3]
'yo'
>>> str1[::-2]
'nhy'
>>> str1[::-]
SyntaxError: invalid syntax
>>> str1[::-1]
'nohtyp'
>>> # string built in functions
>>> str1
'python'
>>> # capitalize()
>>> str1.capitalize()
'Python'
>>> # lower() and upper()
>>> str1 = "PythoN"
>>> str1.lower()
'python'
>>> str1.upper()
'PYTHON'
>>> str1.swapcase()
'pYTHOn'
>>> # title()
>>> str1 = "hello How arE yOU"
>>> str1.title()
'Hello How Are You'
>>> 
>>> # count()
>>> # number of times a string exist in another string
>>> str1 ="i play cricket and i play chess"
>>> str1.count("play")
2
>>> str1.count("i ")
2
>>> str1.count("i")
3
>>> str1.count(" i ")
1
>>> # islower()
>>> str1 = "python"
>>> str1.islower()
True
>>> str1 = "Python"
>>> str1.islower()
False
>>> 
>>> # isupper()
>>> str1 = "python"
>>> str1.isupper()
False
>>> 
>>> # isdecimal()
>>> #True if all the charcters are number
>>> str1 = "9000468563"
>>> str1.isdeciaml()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    str1.isdeciaml()
AttributeError: 'str' object has no attribute 'isdeciaml'
>>> str1.isdecimal()
True
>>> str1 = "432dff"
>>> str1.isdecimal()
False
>>> 
>>> # is alpha()
>>> #only alphabets
>>> str1 = "phani123"
\
>>> str1.isalpha()
False
>>> str1 = "phani"
>>> str1.isalpha()
True
>>> 
================== RESTART: F:/python programs/exampleif.py ==================
Enter marks:25
pass
lets celebrate
>>> 36
36
>>> 
================== RESTART: F:/python programs/exampleif.py ==================
Enter marks:25
pass
lets celebrate
>>> 
================== RESTART: F:/python programs/exampleif.py ==================
Enter marks:25
pass
lets celebrate
Enter marks:
================== RESTART: F:/python programs/exampleif.py ==================
Enter marks:25
pass
lets celebrate
Enter marks:1000
Invalid marks
>>> 
================== RESTART: F:/python programs/example2.py ==================
