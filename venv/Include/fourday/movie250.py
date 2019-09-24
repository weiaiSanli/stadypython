# -*- encoding: utf-8 -*-
"""
@File    : movie250.py
@Time    : 2019-9-24 14:33
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import pymongo
import requests
from lxml import html

etree = html.etree

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["moviesDB"]

mycol = mydb["movies"]

if mycol.find_one():
    mycol.delete_many({})


def get_movies():
    heads = {
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

    }

    movies = []
    for position in range(0, 10):
        url = "https://movie.douban.com/top250?start=" + str(position * 25)
        # url = "https://movie.douban.com/top250"
        resbody = requests.get(url, headers=heads, verify=False).text
        # resbody = requests.get(url, headers=heads, timeout=10).text
        # print(resbody.status_code)
        s = etree.HTML(resbody)
        b = s.xpath('//*[@id="content"]/div/div[1]/ol')  #
        names = s.xpath("//*[@id='content']/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()")
        doctors = s.xpath("//*[@id='content']/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]")
        reviews = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
        spaces = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')
        desDetails = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')
        for names_i, doctor_i, review_i, introduce_i in zip(names, reviews, spaces, desDetails):
            content = {
                'names': names_i,
                'review': doctor_i,
                'person': review_i,
                'desDetail': introduce_i
            }
            movies.append(content)
    print("当前moview长度为:" + str(len(movies)))
    if movies:
        mycol.insert_many(movies)

    print(len(movies))


get_movies()
