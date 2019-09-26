# -*- encoding: utf-8 -*-
"""
@File    : BeautifulTest.py
@Time    : 2019-9-26 10:09
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import requests
from bs4 import BeautifulSoup


link = 'http://www.santostang.com/'
headers = {
    'Host': 'www.santostang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

r = requests.get(link, headers=headers, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')


print(soup.select("header div[class='sns']"))

firstTitle = soup.find('h1', class_='post-title').a.text.strip()
print(firstTitle)

title_all = soup.find_all('h1', class_='post-title')
for i in range(len(title_all)):
    print(title_all[i].a['href'].strip())
