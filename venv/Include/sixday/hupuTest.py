# -*- encoding: utf-8 -*-
"""
@File    : hupuTest.py
@Time    : 2019-9-26 15:47
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import requests
from bs4 import BeautifulSoup
import datetime
import pymongo
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 创建库
houseDB = myclient["hupuDB"]
# 创建表
bxjtable = houseDB["bxjtable"]

if bxjtable.find_one():
    bxjtable.delete_many({})

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

link = 'https://bbs.hupu.com/bxj'


def getSoup(linkUrl):
    r = requests.get(linkUrl, headers=headers)
    html = r.content  # content-encoding: gzip封装使用content获取将UTF_8解码为unicode
    html = html.decode('UTF_8')
    soup = BeautifulSoup(html, 'lxml')
    return soup


def getListItem(soup):
    # listsLi = soup.select('.for-list li')
    listsLi = soup.find('ul' , class_='for-list')

    for item in listsLi.find_all('li'):
        # 主题
        inviteName = item.find('div', class_='titlelink box').a.text.strip()
        # 作者
        inviteWrite = item.find('div', class_='author box').a.text.strip()
        # 作者个人网址
        writeurl = item.find('div', class_='author box').a['href']
        # 发布时间
        publishtime = item.find('div', class_='author box').contents[5].text.strip()
        # <span class="ansour box">0&nbsp;/&nbsp;2742219</span>
        replay_view = item.find('span', class_='ansour box').text.strip()
        splits = replay_view.split('/')
        recoveryNum = splits[0].strip()  # 回复量
        pageViewNum = splits[1].strip()  # 浏览量
        # 最后回复
        lastRecoveryTime = item.find('div', class_='endreply box').a.text.strip()
        # 最后回复人
        lastRecoveryName = item.find('span', class_='endauthor').text.strip()

        content = {
            'inviteName': inviteName,
            'inviteWrite': inviteWrite,
            'writeurl': writeurl,
            'publishtime': publishtime,
            'recoveryNum': recoveryNum,
            'pageViewNum': pageViewNum,
            'lastRecoveryTime': lastRecoveryTime,
            'lastRecoveryName': lastRecoveryName
        }

        bxjtable.insert_one(content)


for index in range(1, 4):
    time.sleep(1)
    soup = getSoup(link + "-" + str(index))
    getListItem(soup)


print("全部下载成功")