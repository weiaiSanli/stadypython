# -*- encoding: utf-8 -*-
"""
@File    : redisTest.py
@Time    : 2019-10-9 15:53
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
from bs4 import BeautifulSoup
from redis import Redis
import redis
import requests

r = Redis(host='172.16.150.113', port=6379, password='admin', db=0)
print(r.keys('*'))


def push_redis_list():
    link_list = []
    with open('alexa.txt', 'r') as file:
        file_list = file.readlines()

        for eachFile in file_list:
            eachFile = eachFile.split('\t')[1]
            eachFile = eachFile.replace('\n', '')
            link_list.append(eachFile)

    for url in link_list:
        try:
            response = requests.get(url, timeout=20)
            soup = BeautifulSoup(response.text, 'lxml')
            imgList = soup.find_all('img')
            for img in imgList:
                img_url = img['src']
                if img_url != '' and img_url.startswith('http'):
                    print("加入图片地址为:", img_url)
                    r.lpush('img_url', img_url)
        except Exception as e:
            print("error ", e)

    print("总共图片链接个数为:", r.llen('img_url'))


# push_redis_list()


def get_redis_list():
    pass
    pipe = r.pipeline()
    pipe_size = 100000
    len = 0
    key_list = []
    print(r.pipeline())
    keys = ["img_url"]
    for key in keys:
        key_list.append(key)
        print(pipe.get(key) , "1123434")
        if len < pipe_size:
            len += 1
        else:
            for (k, v) in zip(key_list, pipe.execute()):
                print(k, v)

            len = 0
            key_list = []

    for (k, v) in zip(key_list, pipe.execute()):
        print(k, v)


get_redis_list()
