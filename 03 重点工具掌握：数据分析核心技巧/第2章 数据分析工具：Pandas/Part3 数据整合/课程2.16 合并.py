# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:12:25 2019

@author: lindsay.hu
"""

'''

【课程2.16】  合并 merge、join

Pandas具有全功能的，高性能内存中连接操作，与SQL等关系数据库非常相似

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
'''

import numpy as np
import pandas as pd
from datetime import datetime

# merge合并 → 类似excel的vlookup

df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
df3 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
df4 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
# left：第一个df
# right：第二个df
# on：参考键
print(pd.merge(df1,df2,on='key'))
# 多个链接键
print(pd.merge(df3, df4, on=['key1','key2']))

# 参数how → 合并方式

# inner：默认，取交集
print(pd.merge(df3,df4,on=['key1','key2'],how='inner'))
#outer:取并集，数据缺失范围NaN
print(pd.merge(df3,df4,on=['key1','key2'],how='outer'))
#left:按照d3为参考合并，数据缺失范围NaN
print(pd.merge(df3,df4,on=['key1','key2'],how='left'))
#right:按照d4为参考合并，数据缺失范围NaN
print(pd.merge(df3,df4,on=['key1','key2'],how='right'))

# 参数 left_on, right_on, left_index, right_index → 当键不为一个列时，可以单独设置左键与右键
# left_index：为True时，第一个df以index为键，默认False
# right_index：为True时，第二个df以index为键，默认False

# 所以left_on, right_on, left_index, right_index可以相互组合：
# left_on + right_on, left_on + right_index, left_index + right_on, left_index + right_index
df1 = pd.DataFrame({'lkey':list('bbacaab'),
                   'data1':range(7)})
df2 = pd.DataFrame({'rkey':list('abd'),
                   'date2':range(3)})
# df1以‘lkey’为键，df2以‘rkey’为键
print(pd.merge(df1,df2,left_on='lkey',right_on='rkey'))

df1 = pd.DataFrame({'key':list('abcdfeg'),
                   'data1':range(7)})
df2 = pd.DataFrame({'date2':range(100,105)},
                  index = list('abcde'))
# df1以‘key’为键，df2以index为键
print(pd.merge(df1, df2, left_on='key', right_index=True))

# 参数 sort
df1 = pd.DataFrame({'key':list('bbacaab'),
                   'data1':[1,3,2,4,5,9,7]})
df2 = pd.DataFrame({'key':list('abd'),
                   'date2':[11,2,33]})
#sort:按照字典顺序通过，连接键 对结果DataFrame进行排序。默认为False,设置为False会大幅提高性能
x1 = pd.merge(df1,df2,on='key',how='outer')
x2 = pd.merge(df1,df2,on='key',sort=True,how='outer')
print(x1)
print(x2)
print('-----')
# 也可直接用Dataframe的排序方法：sort_values，sort_index
print(x2.sort_values('data1'))

# pd.join() → 直接通过索引链接，即index连接
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
# 等价于：pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(left)
print(right)
print(left.join(right))
print(left.join(right, how='outer'))  
print('-----')

df1 = pd.DataFrame({'key':list('bbacaab'),
                   'data1':[1,3,2,4,5,9,7]})
df2 = pd.DataFrame({'key':list('abd'),
                   'date2':[11,2,33]})
print(df1)
print(df2)
# suffixes=('_x', '_y')默认,相当于重命名列名
print(pd.merge(df1,df2,left_index=True,right_index=True,suffixes=('_1','_2')))
print(df1.join(df2['date2']))

left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'key': ['K0', 'K1', 'K0', 'K1']})
right = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                     index=['K0', 'K1'])
print(left)
print(right)
# 等价于pd.merge(left, right, left_on='key', right_index=True, how='left', sort=False);
# left的‘key’和right的index
print(left.join(right, on = 'key'))

