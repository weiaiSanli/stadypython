# -*- encoding: utf-8 -*-
"""
@File    : ProcessTest.py
@Time    : 2019-9-29 17:05
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
from multiprocessing import Process, Queue
import time
import requests

link = []

with open('alexa.txt', 'r') as file:
    file_list = file.readlines()
    for line in file_list:
        line = line.split('\t')[1]
        line = line.replace("\n", '')
        link.append(line)

startTime = time.time()


def crawler(q):
    pass
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=10)
        print(q.qsize(), r.status_code, url)
    except Exception as e:
        print(q.qsize(), url, 'error:', e)


class MyProcess(Process):
    def __init__(self, q):
        Process.__init__(self)
        self.q = q

    def run(self):
        print("starting", self.pid)
        while not self.q.empty():
            crawler(self.q)

        print("exiting", self.pid)


if __name__ == '__main__':  # 只有调用加载当前类才会运行其下的函数,否则外部调用类中对象,不会运行该判断下面的函数
    ProcessNames = ["process-01", "process-02", "process-03"]
    workQueue = Queue(len(link))

    for url in link:
        workQueue.put(url)

    for i in range(0, 3):
        print("当前为:"  , i)
        p = MyProcess(workQueue)
        print("创建了第一个:", i)
        p.daemon = True
        p.start()
        p.join()
    endTime = time.time()
    print("多进程爬虫时间为:", endTime - startTime)

    print("爬虫结束了!")
