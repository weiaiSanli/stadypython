# -*- encoding: utf-8 -*-
"""
@File    : quequeThread.py
@Time    : 2019-9-27 14:10
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm --> 使用队列Queue进行多线程
"""

import threading
import requests
import time
import queue as Queue # Queue模块实现了所有要求的锁机制。  Queue模块主要是多线程，保证线程安全使用的

link_list = []
with open('alexa.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split('\t')[1]
        line = line.replace("\n", '')
        link_list.append(line)
startTime = time.time()


def crawler(threadName, q):
    # Queue.get(item, block=True, timeout=None): 从队列里取数据。如果为空的话，blocking = False 直接报 empty异常。
    # 如果blocking = True，就是等一会，timeout必须为 0 或正数。None为一直等下去，0为不等，正数n为等待n秒还不能读取，报empty异常。
    url = q.get(timeout=2)

    try:
        r = requests.get(url, timeout=10)
        print(q.qsize(), threadName, r.status_code, url)
    except Exception as e:
        print(q.qsize(), threadName, url, "error:", e)

    pass


class MyThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print("starting" + self.name)
        while not self.q.empty():
            try:
                crawler(self.name, self.q)
            except:
                pass

        print("ending" + self.name)


threadList = ["Thread-01", "Thread-02", "Thread-03", "Thread-04", "Thread-05"]
workQueue = Queue.Queue(len(link_list))

for url in link_list:
    workQueue.put(url)


threads = []
for tName in threadList:
    thread = MyThread(tName, workQueue)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

endTime = time.time()

print("Queue多线程总时间为:", endTime - startTime)
