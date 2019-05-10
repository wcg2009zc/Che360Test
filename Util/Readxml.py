#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/10 0010   18:10
# 文件     ：Readxml.py
# IDE      : PyCharm
import xml
from xml.dom import minidom
import xml.dom.minidom
class xmlfile(object):#将XML定义一个新式类
    #def xmlfile(self,xmlfilename,labelname,labelindex):
    def logindata(self,paraname,index):
        dom = xml.dom.minidom.parse('../TestData/login.xml')#打开路径中的xml文档
        root = dom.documentElement                          #得到xml文档对象
        login = root.getElementsByTagName(paraname)         #获得子标签
        loginlist = login[index]                            #通过在loginlist位置标签区分
        return loginlist.firstChild.data                    #返回loginlist的第一个子级的数据