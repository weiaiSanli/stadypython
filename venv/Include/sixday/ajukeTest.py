# -*- encoding: utf-8 -*-
"""
@File    : ajukeTest.py
@Time    : 2019-9-26 11:03
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm-->爬取安居客二手房排行榜信息
@decs: 用于爬取安居客网址下的房价
"""
import requests
from bs4 import BeautifulSoup

import pymongo
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 创建库
houseDB = myclient["houseDB"]
# 创建表
bj = houseDB["nanyang"]

if bj.find_one():
    bj.delete_many({})

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# 爬取城市选择,更改城市名称即可
link = 'https://nanyang.anjuke.com/sale/'


def requestNet(url):
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, "lxml")
    hourList = soup.find_all('li', class_='list-item')
    for hour in hourList:
        # 房屋名字
        hour_name = hour.find('div', class_='house-title').a.text.strip()
        # 房屋总价
        price = hour.find('span', class_='price-det').text.strip()
        # 房屋单价
        unit_price = hour.find('span', class_='unit-price').text.strip()
        # 房屋类型,庭室
        room_type = hour.find('div', class_='details-item').span.text
        # 房屋面积
        room_area = hour.find('div', class_='details-item').contents[3].text
        # 房屋层数
        room_floor = hour.find('div', class_='details-item').contents[5].text
        # 房屋年代
        room_year = hour.find('div', class_='details-item').contents[7].text
        # 房屋地址
        room_address = hour.find('span', class_='comm-address').text.strip()
        room_address = room_address.replace('\xa0\xa0\n ', ' ')
        # 房屋简介
        room_decs = hour.find_all('span', class_='item-tags tag-others')
        room_des = []
        for i in room_decs:
            room_des.append(i.text)
        content = {
            'hour_name': hour_name,
            'price': price,
            'unit_price': unit_price,
            'room_type': room_type,
            'room_area': room_area,
            'room_floor': room_floor,
            'room_year': room_year,
            'room_address': room_address,
            'room_des': str(room_des)
        }
        bj.insert_one(content)


def getAllRoomsInfo():
    for i in range(1, 5):
        url = link + "p" + str(i)
        print("当前请求第" + str(i) + "页")
        requestNet(url)


getAllRoomsInfo()

print("全部存储成功!")
