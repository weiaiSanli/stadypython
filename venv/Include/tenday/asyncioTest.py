# -*- encoding: utf-8 -*-
"""
@File    : asyncioTest.py
@Time    : 2019-10-12 15:22
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import asyncio


async def work_01():
    print("before work_01")
    await asyncio.sleep(1)
    print("end work_01")
    return 1


async def work_02():
    print("before work_02")
    await asyncio.sleep(2)
    print("end work_02")
    return 1 / 0


async def work_03():
    print("before work_03")
    await asyncio.sleep(3)
    print("end work_03")
    return 1 / 0


async def main():
    task_01 = asyncio.create_task(work_01())
    task_02 = asyncio.create_task(work_02())
    task_03 = asyncio.create_task(work_03())

    print("before main")
    await asyncio.sleep(2) # await是交出协成控制权交个其他task
    print("我是等待啊")
    task_03.cancel()

    res = await asyncio.gather(task_01, task_02, task_03, return_exceptions=True)
    print(res)


asyncio.run(main())
