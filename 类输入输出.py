#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stuCount = 0
 
   def __init__(self, stu_no, name , stu_class , male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1
   
   def displayStuInfo(self):
     print "Student information: " ,"number:",self.stu_no , "  Name:",self.name , "  Class:",self.stu_class,"  xingbie:",self.male
 
   def displayCount(self):
      print "Count : %d " % Student.stu_Count
