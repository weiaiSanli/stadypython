# -*- encoding: utf-8 -*-
"""
@File    : MemoryTest.py
@Time    : 2019-9-29 14:59
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import os
import psutil
import sys
import gc

a = []
print(sys.getrefcount(a)) # 应用完毕舍弃
print(sys.getrefcount(a)) # 应用完毕舍弃
print(sys.getrefcount(a)) # 应用完毕舍弃

b= a
print(sys.getrefcount(a))






print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    a.append(b)
    b.append(a)
    show_memory_info("after a created")


func()
show_memory_info("finished")

gc.collect()

show_memory_info("finished")

