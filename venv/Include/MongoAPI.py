# -*- encoding: utf-8 -*-
"""
@File    : MongoAPI.py
@Time    : 2019-9-26 17:44
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm --> 用于mongo数据库更新数据
"""
import pymongo


class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        pymongo.MongoClient(host=self.db_ip, port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]

    def get_one(self, query):
        return self.table.find_one(query, projection={'_id': False})

    def get_all(self, query):
        return self.table.find(query)

    def add(self, kv_dict):
        return self.table.insert(kv_dict)

    def delete(self, query):
        return self.table.delete_many(query)

    def check_exit(self, query):
        ret = self.table.find_one(query)
        return ret is not None

    def update(self, query, kv_dict):
        self.table.update_one(query, {
            '$set': kv_dict
        }, upsert=True)
