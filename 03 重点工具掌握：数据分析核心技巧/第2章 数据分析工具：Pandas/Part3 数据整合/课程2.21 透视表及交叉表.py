# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:36:58 2019

@author: lindsay.hu
"""

'''
【课程2.21】  透视表及交叉表

类似excel数据透视 - pivot table / crosstab
 
'''
import numpy as np
import pandas as pd

# 透视表：pivot_table
# pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
date = ['2017-5-1','2017-5-2','2017-5-3']*3
rng = pd.to_datetime(date)
df = pd.DataFrame({'date':rng,
                   'key':list('abcdabcda'),
                  'values':np.random.rand(9)*10})
print(df)
print('-----')
# data：DataFrame对象
# values：要聚合的列或列的列表
# index：数据透视表的index，从原数据的列中筛选
# columns：数据透视表的columns，从原数据的列中筛选
# aggfunc：用于聚合的函数，默认为numpy.mean，支持numpy计算方法
print(pd.pivot_table(df, values = 'values', index = 'date', columns = 'key', aggfunc=np.sum))  # 也可以写 aggfunc='sum'
print('-----')
# 这里就分别以date、key共同做数据透视，值为values：统计不同（date，key）情况下values的平均值
# aggfunc=len(或者count)：计数
print(pd.pivot_table(df, values = 'values', index = ['date','key'], aggfunc=len))
print('-----')

# 交叉表：crosstab
# 默认情况下，crosstab计算因子的频率表，比如用于str的数据透视分析
# pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, dropna=True, normalize=False)

df = pd.DataFrame({'A': [1, 2, 2, 2, 2],
                   'B': [3, 3, 4, 4, 4],
                   'C': [1, 1, np.nan, 1, 1]})
print(df)
print('-----')

print(pd.crosstab(df['A'],df['B']))
print('-----')
# 如果crosstab只接收两个Series，它将提供一个频率表。
# 用A的唯一值，统计B唯一值的出现次数

print(pd.crosstab(df['A'],df['B'],normalize=True))
print('-----')
# normalize：默认False，将所有值除以值的总和进行归一化 → 为True时候显示百分比

print(pd.crosstab(df['A'],df['B'],values=df['C'],aggfunc=np.sum))
print('-----')
# values：可选，根据因子聚合的值数组
# aggfunc：可选，如果未传递values数组，则计算频率表，如果传递数组，则按照指定计算
# 这里相当于以A和B界定分组，计算出每组中第三个系列C的值

print(pd.crosstab(df['A'],df['B'],values=df['C'],aggfunc=np.sum, margins=True))
print('-----')
# margins：布尔值，默认值False，添加行/列边距（小计）


