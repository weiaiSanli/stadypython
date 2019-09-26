# -*- encoding: utf-8 -*-
"""
@File    : htmlTest.py
@Time    : 2019-9-26 17:30
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

link = 'https://bbs.hupu.com/bxj'

r = requests.get(link, headers=headers)
html = r.content  # content-encoding: gzip封装使用content获取将UTF_8解码为unicode
html = html.decode('UTF_8')
soup = BeautifulSoup(html, 'lxml')
proces = soup.find('ul', class_='for-list')
print(len(proces))

for item in proces.find_all('li'):

    print(item)

# with open('testfirst.html', 'r') as tf:
#     soup = BeautifulSoup(tf, 'lxml')
#     proces = soup.find('ul', class_='producers')
#     print(len(proces))
#     print(proces.find_all('li'))
