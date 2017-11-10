Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var= '1'
>>> print type(var)
<type 'str'>
>>> n_var = int(var)+1
>>> print n_var
2
>>> var = 'abc'
>>> int(var)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(var)
ValueError: invalid literal for int() with base 10: 'abc'
>>> page_num = 1
>>> print "第"，page_num,"页"
SyntaxError: invalid syntax
>>> print "第", page_num,"页"
第 1 页
>>> print type(page_num)
<type 'int'>
>>> print"第" + str(page_num) + "页"
第1页
>>> 
>>> 
>>> 
>>> 
>>> import random
>>> ramdom.Random()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ramdom.Random()
NameError: name 'ramdom' is not defined
>>> random.Random
<class 'random.Random'>
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
'a'
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
'['
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
'c'
>>> random.choice("['a','b','c']")
','
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
'a'
>>> random.choice("['a','b','c']")
']'
>>> random.choice("['a','b','c']")
'b'
>>> random.choice("['a','b','c']")
'['
>>> random.choice("['a','b','c']")
"'"
>>> list1 = ['physics', 'chemistry', 1997, 2000];
>>> list1[0]
'physics'
>>> list1[1]
'chemistry'
>>> list1[0:1]
['physics']
>>> list1[0:2]
['physics', 'chemistry']
>>> list1[1:3]
['chemistry', 1997]
>>> list1[1:2】
      
SyntaxError: invalid syntax
>>> list1[1:2]
['chemistry']
>>> list2 = [1,2,3,4,5]
>>> list1+list2
['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]
>>> list1*2
['physics', 'chemistry', 1997, 2000, 'physics', 'chemistry', 1997, 2000]
>>> list2*3
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> 3 in [1,2.3]:
	
SyntaxError: invalid syntax
>>> 3 in [1,2,3]:
	
SyntaxError: invalid syntax
>>> 3 in [1,2,3]
True
>>> if 3 in [1,2,3]:
	print "OK"

	
OK
>>> list = []
>>> list.append ("a")
>>> list
['a']
>>> list1 = ['physics', 'chemistry', 1997, 2000];
>>> list[2]

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    list[2]
IndexError: list index out of range
>>> list = ['physics', 'chemistry', 1997, 2000];
>>> list [2]
1997
>>> list
['physics', 'chemistry', 1997, 2000]
>>> list1
['physics', 'chemistry', 1997, 2000]
>>> list2
[1, 2, 3, 4, 5]
>>> cmp(list1,list2)
1
>>> list1=[2,3,4,5,6]
>>> cmp(list1,list2)
1
>>> list1,list2 = [123,'xyz'],[456, 'abc']
>>> cmp(list1, list2)
-1
>>> aTuple = (123, 'xyz', 'zara', 'abc')
>>> aList = list(aTuple)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    aList = list(aTuple)
TypeError: 'list' object is not callable
>>> list2
[456, 'abc']
>>> list2.reverse()
>>> list2
['abc', 456]
>>> 
