# -*- encoding: utf-8 -*-
"""
@File    : LoginZhihu.py
@Time    : 2019-9-25 14:40
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=chrome_options)

# browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/signin")


def loginZhihu(browser):
    # 获取登录名框
    try:

        bol = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div/form/div[1]/div[2]')
        print(bol.text)

        bol.click()
        time.sleep(5)

        userName = browser.find_element_by_name("username")
        if not userName.text:
            print("是否为null")
        userName.send_keys("17610551703")
        userName.send_keys(Keys.RETURN)  # 回车键

        time.sleep(3)

        pwd = browser.find_element_by_name('password')
        pwd.clear()
        pwd.send_keys('sqlm1314/...')
        pwd.send_keys(Keys.RETURN)
        time.sleep(2)
        inp = input("是否登录 Y/N \n")
        # if inp.islower():
        if True:
            print("start login...")
            btn = browser.find_element_by_css_selector('Button SignFlow-submitButton Button--primary Button--blue')
            btn.click()
            print("开始等待")
            element = WebDriverWait(browser, 15).until(EC.title_contains(u'发现'))
            print("已选择首页")

    except TimeoutException:
        print("时间超时")
    # except NoSuchElementException:
    #     print("no Such!")


loginZhihu(browser)

urls = set()


def getZhihuList(browser):
    elems = browser.find_elements_by_css_selector('.ContentItem-title')
    for elem in elems:
        link_elem = elem.find_element_by_tag_name('a')
        if link_elem.text in urls:
            pass
        else:
            print(link_elem.text)  # 标题
            print(link_elem.get_attribute("href"))  # 链接
            urls.add(link_elem.get_attribute("href"))

    pass


# getZhihuList(browser)
# <a href="http://www.tingdongfang.com/book22927a60l1p2.html" title="206东汉之得陇望蜀.mp3">206东汉之得陇望蜀.mp3</a>
# <a href="http://www.tingdongfang.com/book22927a56l1p2.html" title="202东汉之定都洛阳.mp3">202东汉之定都洛阳.mp3</a>

def scrool_load(browser):
    pass
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
browser.implicitly_wait(2)


scrool_load(browser)
