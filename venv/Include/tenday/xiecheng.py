# -*- encoding: utf-8 -*-
"""
@File    : xiecheng.py
@Time    : 2019-10-11 16:37
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import time
import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):

    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]

    await asyncio.gather(*tasks)




startTime = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

endTime = time.time()
print("花费的总时间为:", endTime - startTime)
