# -*- encoding: utf-8 -*-
"""
@File    : mongotest.py
@Time    : 2019-9-24 11:22
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)
print(x)

for item in mycol.find():
    print(item)

print(x.inserted_id)

# if "runoobdb" in mydb:
#     print("数据库在其中")
# else :
#     print("数据库bu在其中")

