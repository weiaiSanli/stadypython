# -*- encoding: utf-8 -*-
"""
@File    : asyncTest.py
@Time    : 2019-10-11 17:05
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import asyncio
import time


async def work_01():
    print("work_01_start")
    await asyncio.sleep(1)
    print("work_01_end")


async def work_02():
    print("work_02_start")
    await asyncio.sleep(1)
    print("work_02_end")

async def main():
    task1 = asyncio.create_task(work_01())
    task2 = asyncio.create_task(work_02())
    time.sleep(1)
    print("before...")
    await task1 # 等待1运行结束即可
    print("await task1")
    await task2
    print("await task2")

asyncio.run(main())


