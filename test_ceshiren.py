#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains




'''
作业内容
要求实现搜索功能的Web自动化测试。
冒烟功能。
高级别的异常场景。
Selenium 常用操作与用例编写。
使用隐式等待优化代码。
生成测试报告，测试报告需要体现测试步骤的截图。
如果代码执行出现异常，则截图当前执行的页面。
提交内容:
代码的git地址或帖子地址。
'''
class BrowserDriver:
    def __init__(self, browser):
        self.driver = self.open_browser(browser)

    def open_browser(self, browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            exclude = ["enable-automation"]
            options.add_experimental_option("excludeSwitches", exclude)
            driver = webdriver.Chrome(chrome_options=options)
        else:
            driver = webdriver.Edge()
        return driver
class TestCeshiren():
    def setup_class(self):
        # 全局动作
        # 因为我用的英文的chrome默认语言,所以就切换成英文了
        esoptions = webdriver.ChromeOptions()
        esoptions.add_argument("--lang=en-US")
        prefs = {"intl.accept_languages": "en-US"}
        esoptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=esoptions)
        #这一部分原来不知道干啥的,好像是传参的
        #self.vars = {}
        #全局隐式等待3秒(智能等待)
        print("\nall setup_class succeed")
    def setup(self):
        #方法前全局动作
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".search-input").click() //这个可以不要
        self.driver.implicitly_wait(3)
        print("setup succeed,Button clicked")
    def teardown_class(self):
        self.driver.quit()
        print("\nteardown_class succeed,close browse")
    #用例几个:正常搜索,特殊字符,不存在比如乱七八糟的什么内容,超长,搜索为空
    #需要抛出异常
    def test_search_normal(self):
        #time.sleep(5)
        '''
        self.driver.switch_to.frame(0)
        move = self.driver.find_element(By.CSS_SELECTOR, ".search-input")
        actions = ActionChains(self.driver)
        actions.move_to_element(move).perform()
        '''
        #self.driver.find_element(By.CSS, "/html/body/section/div/div[1]/header/div/div/div[2]/div/div/div/div/div[1]/input").send_keys("自动化")
        #这个地方定位到这个搜索框能让输入文本试了id,css_selector后会报错 "element not interactable" 试了什么 iframe switch啥的没啥用,最后用xpath绝对路径有用了
        search_box=self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/header/div/div/div[2]/div/div/div/div/div[1]/input")
        search_box.send_keys("自动化")
        #两次enter,这样才能打开全局搜索窗口
        self.driver.implicitly_wait(3)
        search_box.send_keys(Keys.RETURN)
        print("我输入回车咯")
        #这里好像必须强制等待一下,用隐式等待没用
        time.sleep(3)
        search_box.send_keys(Keys.RETURN)
        print("我输入回车咯X2")
        self.driver.implicitly_wait(3)
        res=self.driver.find_element(By.CSS_SELECTOR, ".fps-result-entries")
        #认为有内容结果就是 正确 返回
        assert res.text != None
    def test_search_special(self):
        #使用高级测试去搜索 !@# 然后判断结果是No results found.
        self.driver.find_element(By.CSS_SELECTOR, ".show-advanced-search").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR, ".search-bar input").send_keys("!@#")
        self.driver.find_element(By.CSS_SELECTOR, ".search-bar button").click()
        res=self.driver.find_element(By.XPATH, "//h3[contains(text(),'No results found.')]")
        print(res.text)
        assert res.text == "No results found."
        #time.sleep(10)
    '''
    def test_search_unexist(self):
        pass
    def test_search_long(self):
        pass
    def test_search_empty(self):
        pass
    '''