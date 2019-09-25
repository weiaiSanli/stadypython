# -*- encoding: utf-8 -*-
"""
@File    : seleniumTest.py
@Time    : 2019-9-25 10:18
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
from selenium import webdriver
import time

cop = webdriver.ChromeOptions()
cop.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片
# 禁用JavaScript
cop.add_argument("--disable-javascript")
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)
driver.close()

# driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere]"))
# comment = driver.find_element_by_css_selector('div.reply-content')
# cpntent = comment.find_element_by_tag_name('p')
# print(cpntent)

# 控制css的加载


