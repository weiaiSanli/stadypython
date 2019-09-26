# -*- encoding: utf-8 -*-
"""
@File    : lxmlTest.py
@Time    : 2019-9-26 10:53
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""

from lxml import html
etree = html.etree
import requests

link = 'http://www.santostang.com/'
headers = {
    'Host': 'www.santostang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

r = requests.get(link, headers=headers, verify=False)
s = etree.HTML(r.text)
print(s.xpath('//*[@id="main"]/div/div/article[2]/header/h1/a/text()'))

