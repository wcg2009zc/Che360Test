#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/10    22:11
# 文件     ：Driver1.py
# IDE      : PyCharm

"""driver配置文件把浏览器初始化操作封装成一个类，使用装饰器添加共有变量中"""
from selenium import webdriver
from Util.singleton import singleton

@singleton                  #使用单例模式
class DriverHandle(object): #单例Driver为一个类，使用程序在不同位置都能取到同一个driver
    def __init__(self):
        self.driver = webdriver.Chrome()