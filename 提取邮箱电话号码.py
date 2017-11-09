Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> import re
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> re.finddall('\w+@\w+.com',y)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    re.finddall('\w+@\w+.com',y)
AttributeError: 'module' object has no attribute 'finddall'
>>> re.findall('\w+@\w+\.com',y)
['123@qq.com', 'aaa@163.com', 'bbb@126.com']
>>> 
>>> 
>>> 
>>>  y = 'tel:010-12345678 address:changanRoad'
 
  File "<pyshell#8>", line 2
    y = 'tel:010-12345678 address:changanRoad'
    ^
IndentationError: unexpected indent
>>>  s = 'tel:010-12345678 address:changanRoad'
 
  File "<pyshell#9>", line 2
    s = 'tel:010-12345678 address:changanRoad'
    ^
IndentationError: unexpected indent
>>> s = 'tel:010-12345678 address:changanRoad'
>>> re.findall('d',y)
['d', 'd']
>>> re.findall('\d',y)
['1', '2', '3', '1', '6', '3', '1', '2', '6', '3', '3', '3', '3', '3']
>>>  y = 'tel:010-12345678 address:changanRoad tel:0514-8008208820'
 
  File "<pyshell#13>", line 2
    y = 'tel:010-12345678 address:changanRoad tel:0514-8008208820'
    ^
IndentationError: unexpected indent
>>> y = 'tel:010-12345678 address:changanRoad tel:0514-8008208820'
>>> re.findall('\d{3,4}\d{7,8}',y)
['8008208820']
>>> re.findall('\d{3,4}-d{7,8}',y)
[]
>>> re.findall('\d{3,4}\-\d{7,8}\',y)
	   
SyntaxError: EOL while scanning string literal
>>> re.findall('\d{3,4}-\d{7,8}',y)
['010-12345678', '0514-80082088']
>>> 
