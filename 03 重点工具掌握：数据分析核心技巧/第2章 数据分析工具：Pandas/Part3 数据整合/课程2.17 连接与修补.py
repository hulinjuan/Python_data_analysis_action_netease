# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:39:00 2019

@author: lindsay.hu
"""

'''
【课程2.17】  连接与修补 concat、combine_first

连接 - 沿轴执行连接操作

pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)

'''
import numpy as np
import pandas as pd

#连接：concat
s1 = pd.Series([1,2,3])
s2 = pd.Series([2,3,4])
s3 = pd.Series([1,2,3],index = ['a','c','h'])
s4 = pd.Series([2,3,4],index = ['b','e','d'])
# 默认axis=0，行+行
print(pd.concat([s1,s2]))
print(pd.concat([s3,s4]).sort_index())
# axis=1,列+列，成为一个Dataframe
print(pd.concat([s3,s4], axis=1))
print('-----')

# 连接方式：join，join_axes
# join：{'inner'，'outer'}，默认为“outer”。如何处理其他轴上的索引。outer为联合和inner为交集。
# join_axes：指定联合的index
s5 = pd.Series([1,2,3],index = ['a','b','c'])
s6 = pd.Series([2,3,4],index = ['b','c','d'])
print(pd.concat([s5,s6],axis=1))
print(pd.concat([s5,s6],axis=1,join='inner'))
print(pd.concat([s5,s6],axis=1,join_axes=[['a','b','d']]))

# 覆盖列名

# keys：序列，默认值无。使用传递的键作为最外层构建层次索引
sre = pd.concat([s5,s6], keys = ['one','two'])
print(sre,type(sre))
print(sre.index)
# axis = 1, 覆盖列名
sre = pd.concat([s5,s6], axis=1, keys = ['one','two'])
print(sre,type(sre))

# 修补 pd.combine_first()

df1 = pd.DataFrame([[np.nan, 3., 5.], [-4.6, np.nan, np.nan],[np.nan, 7., np.nan]])
df2 = pd.DataFrame([[-42.6, np.nan, -8.2], [-5., 1.6, 4]],index=[1, 2])
print(df1)
print(df2)
# 根据index，df1的空值被df2替代
# 如果df2的index多于df1，则更新到df1上，比如index=['a',1]
print(df1.combine_first(df2))
print('-----')

# update，直接df2覆盖df1，相同index位置
df1.update(df2)
print(df1)