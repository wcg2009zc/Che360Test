#!usr/bin/env python
# -*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/30 0030   11:25
# 文件     ：Tsetsuite.py
# IDE      : PyCharm
import unittest,time
from Util.Driver import DriverHandle
from Element.basepage import Basic,Assertions
from Util.Readxml import xmlfile


class Back_stageTestcase(unittest.TestCase):
    @classmethod                    #@classmethod修饰的方法Class()通过cls参数传递当前类对象
    def setUpClass(cls):
        cls.dr = DriverHandle().driver
        cls.dr.get(xmlfile().logindata("url", 0))
        cls.dr.implicitly_wait(30)
        cls.dr.maximize_window()

    def setUp(self):
         time.sleep(3)

    def test_case01(self):
        #验证：资讯元素是否正确
        Assertions().assertEqual_xpath('资讯','//*[@id="sitenav"]/dl[1]/dt/a')
        print('执行了吗')


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2)










