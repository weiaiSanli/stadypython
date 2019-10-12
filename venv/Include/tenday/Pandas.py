# -*- encoding: utf-8 -*-
"""
@File    : Pandas.py
@Time    : 2019-10-11 14:46
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
import pandas as pd
from pandas import Series , DataFrame

x1 = Series([1, 2,3,4])
x2 = Series(index= x1 , data = ['a' , 'b' , 'c' , 'd'])

print(x1)
print(x2)

