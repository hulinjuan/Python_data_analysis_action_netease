# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:53:26 2019

@author: lindsay.hu
"""

'''
【课程2.4】 数据结构Series：基本技巧

数据查看/重新索引/对齐/添加、修改、删除值

'''
import numpy as np
import pandas as pd

###数据查看
s = pd.Series(np.random.rand(15))
print(s.head(2)) #查看前2行
print(s.tail()) #查看最后5行，默认5

###重新索引 reindex
#根据新的索引重新排序，如果索引不存在，引入缺失值
s = pd.Series(np.random.rand(5),index=['a','b','c','d','e'])
s1 = s.reindex(['c','d','a','f'])
print(s)
print(s1)
print(s.reindex(['c','d','a','f']))
s2 = s.reindex(['c','d','a','f','aaaa'],fill_value=0)
print(s2)

###Series对齐
#按标签对齐，无标签可对齐引入缺失值
s1 = pd.Series(np.random.rand(3),index=['Jzck','Marry','Tom'])
s2 = pd.Series(np.random.rand(3),index=['Wang','Jzck','Marry'])
print(s1)
print(s2)
print(s1+s2)

###删除:drop
#drop删除元素之后返回副本(inplace=False)
s = pd.Series(np.random.rand(5),index=list('ngjur'))
print(s)
s1 = s.drop('n')
s2 = s.drop(['g','j'])
print(s1)
print(s2)
print(s)
s3 = s.drop('n',inplace=True) #直接作用到原Series了
print(s3) #s3打印出来为None
print(s)

###添加
s1 = pd.Series(np.random.rand(5))
s2 = pd.Series(np.random.rand(5),index=list('ngjur'))
print(s1)
print(s2)
#直接通过下标索引/标签索引添加值
s1[5] = 100
s2['a'] = 100
print(s1)
print(s2)
#通过append方法，直接添加一个数组
#.append方法生成一个新的数组，不改变之前的数组
s3 = s1.append(s2)
print(s3)
print(s1)


