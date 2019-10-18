# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:30:31 2019

@author: lindsay.hu
"""


'''
【课程2.6】 数据结构Dataframe：基本技巧

数据变量、转置/添加、修改、删除值/对齐/排序

'''
import numpy as np
import pandas as pd

#数据查看、转置
df = pd.DataFrame(np.random.rand(16).reshape(8,2)*100,
                  columns = ['a','b'])
print(df.head(2)) #查看前2行，head()查看头部数据
print(df.tail()) #查看尾部，默认5行

print(df.T) #.T转置

#添加与修改
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  columns = ['a','b','c','d'])
print(df)
#新增列/行，并赋值
df['e'] = 10
df.loc[4] = 20
print(df)
#索引后直接修改值
df['e'] = 20
df[['a','c']] = 100
df.iloc[::2] = 101
print(df)

#删除 del / drop()
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  columns = ['a','b','c','d'])
print(df)

#del语句删除列
del df['a']
print(df)
print('----')
#drop()删除行，inplace=False ->删除后生成新的数据，不改变原数据
print(df.drop(0))
print(df.drop([1,2]))
print(df)
#drop()删除列，需要加上axis=1，inplace=False->删除后生成新的数据，不改变原数据
print(df.drop(['d'],axis=1))
print(df)

#对齐
#DataFrame对象之间的数据自动按照列和索引(行标签)对齐
df1 = pd.DataFrame(np.random.randn(10,4),columns=['A','B','C','D'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['A','B','C'])
print(df1)
print(df2)
print(df1 + df2)

#排序1 ： 按值排序，sort_values
#同样适用于Series

df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  columns = ['a','b','c','d'])
print(df1)
#单列排序，ascending参数设置升序降序，默认升序
print(df1.sort_values(['a'],ascending = True)) #升序
print(df1.sort_values(['a'],ascending = False)) #降序
print('---------')
#多列排序，按列顺序排序
df2 = pd.DataFrame({'a':[1,1,1,1,2,2,2,2],
                    'b':list(range(8)),
                    'c':list(range(8,0,-1))})
print(df2)
print(df2.sort_values(['a','c']))

#排序2 ： 按索引排序，sort_index
#默认ascending =True,inplace=False
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = [5,4,3,2],
                  columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['h','s','x','g'],
                  columns = ['a','b','c','d'])
print(df1)
print(df1.sort_index())
print(df2)
print(df2.sort_index())

