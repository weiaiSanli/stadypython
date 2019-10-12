# -*- encoding: utf-8 -*-
"""
@File    : xiecPaidouban.py
@Time    : 2019-10-12 16:16
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import time

import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


async def fetch_url(url):
    async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = 'https://movie.douban.com/cinema/later/beijing/'
    r = await fetch_url(url)
    soup = BeautifulSoup(r, 'lxml')
    movie_names, movie_datas, movie_urls = [], [], []
    linesup = soup.find('div', id="showing-soon")
    for line in linesup.find_all('div', class_="item"):
        aTypes = line.find_all('a')
        liTypes = line.find_all('li')
        movie_name = aTypes[1].text
        movie_data = liTypes[0].text
        movie_names.append(movie_name)
        movie_datas.append(movie_data)
        movie_urls.append(line.find('a', class_='thumb')['href'])

    tasks = [fetch_url(url) for url in movie_urls]
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_data, page in zip(movie_names, movie_datas, pages):
        soup = BeautifulSoup(page, 'lxml')
        asoup = soup.find('a', class_='nbgnbg')
        imgUrl = asoup.find('img')['src']
        print('电影:  {}  时间:  {}  图片Url:  {}'.format(movie_name, movie_data, imgUrl))


startTime = time.time()
asyncio.run(main())
endTime = time.time()
print("总共用时为:", endTime - startTime)
