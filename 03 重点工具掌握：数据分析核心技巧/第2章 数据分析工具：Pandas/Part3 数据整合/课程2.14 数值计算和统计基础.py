# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:36:16 2019

@author: lindsay.hu
"""

'''
【课程2.14】  数值计算和统计基础

常用数学、统计方法
 
'''

import numpy as np
import pandas as pd
from datetime import datetime

# 基本参数：axis、skipna
df = pd.DataFrame({'key1':[4,5,3,np.nan,2],
                 'key2':[1,2,np.nan,4,5],
                 'key3':[1,2,3,'j','k']},
                 index = ['a','b','c','d','e'])
print(df)
print(df['key1'].dtype,df['key2'].dtype,df['key3'].dtype,)

# np.nan ：空值
# .mean()计算均值
# 只统计数字列
# 可以通过索引单独统计一列

# axis参数：默认为0，以列来计算，axis=1，以行来计算，这里就按照行来汇总了
print(df.mean(),type(df.mean())) #默认给出列的平均值
print(df.mean(axis=1)) #按行计算平均值
# skipna参数：是否忽略NaN，默认True，如False，有NaN的列统计结果仍未NaN
print(df.mean(skipna=False)) 
print('单独统计一列:',df['key2'].mean())
 
# 主要数学计算方法，可用于Series和DataFrame（1）
df = pd.DataFrame({'key1':np.arange(10),
                  'key2':np.random.rand(10)*10})
print(df)
print('-----')

print(df.count(),'→ count统计非Na值的数量\n')
print(df.min(),'→ min统计最小值\n',df['key2'].max(),'→ max统计最大值\n')
print(df.quantile(q=0.75),'→ quantile统计分位数，参数q确定位置\n')
print(df.sum(),'→ sum求和\n')
print(df.mean(),'→ mean求平均值\n')
print(df.median(),'→ median求算数中位数，50%分位数\n')
print(df.std(),'\n',df.var(),'→ std,var分别求标准差，方差\n')
print(df.skew(),'→ skew样本的偏度\n')
print(df.kurt(),'→ kurt样本的峰度\n')

df['key1_s'] = df['key1'].cumsum()
df['key2_s'] = df['key2'].cumsum()
print(df,'→ cumsum样本的累计和\n')

df['key1_p'] = df['key1'].cumprod()
df['key2_p'] = df['key2'].cumprod()
print(df,'→ cumprod样本的累计积\n')

print(df.cummax(),'\n',df.cummin(),'→ cummax,cummin分别求累计最大值，累计最小值\n')
# 会填充key1，和key2的值

# 唯一值：.unique()
# 得到一个唯一值数组
# 通过pd.Series重新变成新的Series
s = pd.Series(list('asdvasdcfgg'))
sq = s.unique()
print(s)
print(sq,type(sq))
print(pd.Series(sq))

sq.sort()
print(sq)
# 重新排序

# 值计数：.value_counts()
# 得到一个新的Series，计算出不同值出现的频率
# sort参数：排序，默认为True
sc = s.value_counts(sort = False)  # 也可以这样写：pd.value_counts(sc, sort = False)
print(sc)

# 成员资格：.isin()
# 用[]表示
# 得到一个布尔值的Series或者Dataframe
s = pd.Series(np.arange(10,15))
df = pd.DataFrame({'key1':list('asdcbvasd'),
                  'key2':np.arange(4,13)})
print(s)
print(df)
print('-----')

print(s.isin([5,14]))
print(df.isin(['a','bc','10',8]))

