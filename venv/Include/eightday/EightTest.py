# -*- encoding: utf-8 -*-
"""
@File    : EightTest.py
@Time    : 2019-9-29 9:26
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import time
from threading import Thread
import sys

num = 160 + 350.0 + 78 + 26 + 18 + 5 + 15 + 48
print(num)

a = []
b = a
print(sys.getrefcount(a))




def conunt(m):
    while m > 0:
        m -= 1
startTime = time.time()
# conunt(100000000)
n = 100000000
t1 = Thread(target=conunt, args=[n // 2])
t2 = Thread(target=conunt, args=[n // 2])
t1.start()
t2.start()
t1.join()
t2.join()
endTime = time.time()

print("总共用时为:", endTime - startTime)