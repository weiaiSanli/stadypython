# -*- encoding: utf-8 -*-
"""
@File    : movie250Details.py
@Time    : 2019-9-24 16:19
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
from lxml import html
import requests

from Include.fourday.doubanMovie import DoubanMovie

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
newDB = myclient['moviesDB']
mycol = newDB['movies_doctor']

if mycol.find_one():  # 如果数据库中有数据就删除表
    mycol.delete_many({})

etree = html.etree

headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 获取电影列表数据
movies250 = []


# 获取一级电影列表数据
def getmovieList():
    baseUrl250 = "https://movie.douban.com/top250?start="
    for position in range(0, 10):
        url = baseUrl250 + str(position * 25)
        resposeBody = requests.get(url, headers=headers, verify=False).text
        htmlStr = etree.HTML(resposeBody)
        hrefList = htmlStr.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
        desDetails = htmlStr.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')
        for positionUrl, desDetail in zip(hrefList, desDetails):
            content = {
                'positionUrl': positionUrl,
                'desDetail': desDetail
            }
            movies250.append(content)

    print("当前存储的电影总共网址为:" + str(len(movies250)))


def getMovieDetails():
    for movieBean in movies250:
        context = movieUtil.getMovieDetail(movieBean['positionUrl'], movieBean['desDetail'])
        mycol.insert_one(context)


movieUtil = DoubanMovie()
getmovieList()
getMovieDetails()
