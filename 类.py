#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class isYoungPioneers:
   '所有小学生的基类'
class isLeagueMember:
   '所有中学生的基类'
 
   def __init__(self , canRecite , canOral):
      self.canRecite = canRecite
      self.canOral = canOral

   def __init__(self , canChemistry , canPhysics):
      self.canChemistry = canChemistry
      self.canPhysics = canPhysics

   def displayStuInfo(self):
     print "小学生: " ,"背诵:",self.canRecite , "  口语:",self.canOral
   def displayStuInfo(self):
     print "中学生: " ,"化学:",self.Chemistry , "  物理:",self.canPhysics 
