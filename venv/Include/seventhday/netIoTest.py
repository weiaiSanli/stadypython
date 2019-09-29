# -*- encoding: utf-8 -*-
"""
@File    : netIoTest.py
@Time    : 2019-9-27 11:14
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import requests
import time

link_list = []

with open('alexa.txt', 'r') as file:
    file_list = file.readlines()
    for line in file_list:
        link = line.split('\t')[1]
        link = link.replace('\n', '')

        link_list.append(link)
start = time.time()
for neturl in link_list:
    try:
        r = requests.get(neturl , timeout=20)
        print(r.status_code, neturl)
    except Exception as e:
        print("error", e)
end = time.time()
print("串行的时间为:", end - start)
