Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1 = ('physics', 'chemistry', 1997, 2000);
>>> tup2 = (1, 2, 3, 4, 5 );
>>> tup3 = "a", "b", "c", "d";
>>> tup1()

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup1()
TypeError: 'tuple' object is not callable
>>> tup1 = ();
>>> tup1 = (50,);
>>> 
KeyboardInterrupt
>>> tup1 = ('physics', 'chemistry', 1997, 2000);
>>> 
==================== RESTART: D:/网络163zy/11.10/元组.py ====================
tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)
>>> 
================== RESTART: D:/网络163zy/11.10/修改元组.py ==================
(12, 34.56, 'abc', 'xyz')
>>> 
================== RESTART: D:/网络163zy/11.10/删除元组.py ==================
('physics', 'chemistry', 1997, 2000)
After deleting tup : 

Traceback (most recent call last):
  File "D:/网络163zy/11.10/删除元组.py", line 8, in <module>
    print tup;
NameError: name 'tup' is not defined
>>> 
================ RESTART: D:/网络163zy/11.10/无关闭分隔符.py ================
abc -4.24e+93 (18+6.6j) xyz
Value of x , y :  1 2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> tup1 = ("all")
>>> print tup1
all
>>> tup1 = ("all",)
>>> print tup1
('all',)
>>> 
