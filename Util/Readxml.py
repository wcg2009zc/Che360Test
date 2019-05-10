#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/10 0010   18:10
# 文件     ：Readxml.py
# IDE      : PyCharm
import xml
from xml.dom import minidom
import xml.dom.minidom
class xmlfile(object):
    #def xmlfile(self,xmlfilename,labelname,labelindex):
    def logindata(self,paraname,index):
        dom = xml.dom.minidom.parse('../../TestData/loginData.xml')
        root = dom.documentElement
        login = root.getElementsByTagName(paraname)
        loginlist = login[index]
        return loginlist.firstChild.data