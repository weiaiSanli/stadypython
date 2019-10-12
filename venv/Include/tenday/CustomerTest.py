# -*- encoding: utf-8 -*-
"""
@File    : CustomerTest.py
@Time    : 2019-10-12 15:32
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import asyncio
import random


async def customer(queue, customerId):
    while True:
        value = await  queue.get()
        print('{} get Value : {} '.format(customerId, value))
        await asyncio.sleep(1)


async def produce(queue, produceId):
    for i in range(5):
        value = random.randint(1, 10)
        await queue.put(value)
        print('{} put Value : {} '.format(produceId, value))
        await asyncio.sleep(2)


async def main():
    queue = asyncio.Queue()
    customer1 = asyncio.create_task(customer(queue , "customer_01"))
    customer2 = asyncio.create_task(customer(queue , "customer_02"))

    produce1 = asyncio.create_task(produce(queue , "produce_01"))
    produce2 = asyncio.create_task(produce(queue , "produce_02"))

    await asyncio.sleep(20)
    customer1.cancel()
    customer2.cancel()

    await asyncio.gather(customer1 ,customer2 , produce1 , produce2 , return_exceptions=True)

asyncio.run(main())