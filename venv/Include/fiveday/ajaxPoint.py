# -*- encoding: utf-8 -*-
"""
@File    : ajaxPoint.py
@Time    : 2019-9-25 8:58
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""

import requests
import time
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


def getUrlAddress(offeset):
    url = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403875065810118634_1569375700070&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1569375700072" + 'offset=' + str(offeset)
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963316"
    page_str = str(offeset)
    link = link1 + page_str + link2

    print("当前地址为:" + url)
    return url



hasData = True
def getUrlInfo(urlAdd):
    r = requests.get(urlAdd, headers=headers ,verify = False )
    jsonStr = r.text
    print(jsonStr)
    # if jsonStr:
    #     global hasData
    #     print("当前列表数据为null")
    #     hasData = False
    #     return

    json_data = jsonStr[jsonStr.find('{'): -2]
    print(json_data)
    jsonInfo = json.loads(json_data)  # load加载文件,loads加载内存中的String
    print(jsonInfo['results']['parents'])
    contentList = jsonInfo['results']['parents']
    for item in contentList:
        print(item['name'] + "评论了: " + item['content'])


for index in range(0, 10):
    if hasData:
        time.sleep(1)
        urlAdd = getUrlAddress(index)
        getUrlInfo(urlAdd)