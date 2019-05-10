#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/8 0008   18:24
# 文件     ：Driver1.py
# IDE      : PyCharm

"""driver配置文件把浏览器初始化操作封装成一个类方便调用"""
from selenium import webdriver
from Util.singleton import singleton

@singleton
class DriverHandle(object):
    def __init__(self):
        self.driver = webdriver.Chrome()