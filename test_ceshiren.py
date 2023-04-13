#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestCeshiren():
    def setup_method(self, method):
        # 全局动作
        self.driver = webdriver.Chrome()
        #这一部分原来不知道干啥的,好像是传参的
        #self.vars = {}
        #全局隐式等待(智能等待)
        self.driver.implicitly_wait(3)
    def setup(self):
        #方法前全局动作
        self.driver.get("https://ceshiren.com/")
    def teardown_method(self, method):
        self.driver.quit()
    #用例几个:正常搜索,特殊字符,不存在比如乱七八糟的什么内容,超长,搜索为空
    #需要抛出异常
    def test_search_normal(self):
        pass
    def test_search_special(self):
        pass
    def test_search_unexist(self):
        pass
    def test_search_long(self):
        pass
    def test_search_empty(self):
        pass