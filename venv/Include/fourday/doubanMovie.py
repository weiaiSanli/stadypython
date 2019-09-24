# -*- encoding: utf-8 -*-
"""
@File    : doubanMovie.py
@Time    : 2019-9-24 14:18
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import pymongo
import requests
from lxml import html

etree = html.etree
class DoubanMovie():

    def getMovieDetail(self , url , movie_profile):
        url = 'https://movie.douban.com/subject/1292052/'
        data = requests.get(url, verify=False).text
        s = etree.HTML(data)
        name = s.xpath('//*[@id="content"]/h1/span[1]/text()')
        doctor = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
        point = s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
        lookPersons = s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
        contentInfo = {
            "movie_name" : name,
            "movie_director" : doctor,
            "movie_score" : point,
            "score_person" : lookPersons,
            "movie_profile" : movie_profile,
        }
        return contentInfo


bean = DoubanMovie()
print(bean.getMovieDetail("", ""))


