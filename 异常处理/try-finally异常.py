#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("E:/testfile1.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print "Error: 没有找到文件或读取文件失败"
