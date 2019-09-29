# -*- encoding: utf-8 -*-
"""
@File    : netIoThread.py
@Time    : 2019-9-27 11:24
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import threading
import time
import requests

link_list = []
with open('alexa.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split('\t')[1]
        line = line.replace('\n', '')
        link_list.append(line)

startTime = time.time()


def crawler(threadName, link_range):
    for i in range(link_range[0], link_range[1] + 1):
        try:
            r = requests.get(link_list[i], timeout=20)
            print(threadName, r.status_code, link_list[i])
        except Exception as e:
            print("error ", e)


class myTHread(threading.Thread):
    def __init__(self, name, link_range):
        threading.Thread.__init__(self)
        self.name = name
        self.link_range = link_list

    def run(self):
        print("starting" + self.name)
        crawler(self.name, self.link_range)
        print("exiting" + self.name)


startTime = time.time()
thread_list = []
link_range_list = [(0, 200), (201, 400), (401, 600), (601, 800), (801, 1000)]
for i in range(1, len(link_range_list) + 1):
    thread = myTHread('Thread-' + str(i), link_range_list[i - 1])
    thread.start()
    thread_list.append(thread)

# 等待所有线程运行完毕
for thread in thread_list:
    thread.join()
endTime = time.time()

print("5个多线程总时间为:", endTime - startTime)
