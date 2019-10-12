# -*- encoding: utf-8 -*-
"""
@File    : paidouban.py
@Time    : 2019-10-12 15:44
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import time

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


def main():
    url = 'https://movie.douban.com/cinema/later/beijing/'
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'lxml')
    linesup = soup.find('div', id="showing-soon")
    for line in linesup.find_all('div', class_="item"):
        aTypes = line.find_all('a')
        liTypes = line.find_all('li')
        movie_name = aTypes[1].text
        movie_data = liTypes[0].text
        imgUrl = line.find('a', class_='thumb')['href']
        imgr = requests.get(imgUrl, headers=headers, verify=False)
        imgSoup = BeautifulSoup(imgr.text, 'lxml')
        asoup = imgSoup.find('a', class_='nbgnbg')
        img = asoup.find('img')['src']
        # print('影片: {} 上映: {} 图片: {}'.format(movie_name, movie_data, img))


startTime = time.time()
main()
endTime = time.time()
print("总共用时为:", endTime - startTime)
