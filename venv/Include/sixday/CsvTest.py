# -*- encoding: utf-8 -*-
"""
@File    : CsvTest.py
@Time    : 2019-9-26 14:06
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import csv

with open('test.csv' , 'r' ,encoding='UTF_8') as csvFile:
  csvReads = csv.reader(csvFile)
  for row in csvReads:
    print(row)


# csvfile = open('test.csv', 'w' , encoding='utf-8')
# writer = csv.writer(csvfile)
# writer.writerow(['id', 'url', 'keywords'])
# data = [
#   ('1', 'http://www.baidu.com/', '百度'),
#   ('2', 'http://www.taobao.com/', '淘宝'),
#   ('3', 'http://www.jd.com/', '京东')
# ]
# writer.writerows(data)
# csvfile.close()

