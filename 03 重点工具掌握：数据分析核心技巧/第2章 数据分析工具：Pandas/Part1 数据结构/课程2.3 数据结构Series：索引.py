# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:35:43 2019

@author: lindsay.hu
"""

'''
【课程2.3】 数据结构Series：索引

位置下标/标签索引/切片索引/布尔型索引

'''
import numpy as np
import pandas as pd

###位置下标索引
s = pd.Series(np.random.rand(10))
print(s)
print(s[5],type(s[6]),s[7].dtype)

###标签索引
#方法类似下标索引，用[]表示，内写上index,注意index是字符串
#如果需要选择多个标签的值，用[[]]来表示(相当于[]中包含一个列表)
#多标签索引结果是新的数据
s = pd.Series(np.random.rand(5),index=['a','b','c','d','e'])
print(s)
print(s['a'],type(s['a']),s['a'].dtype)
print(s[['b','a','c']])

###切片索引
s1 = pd.Series(np.random.rand(10))
s2 = pd.Series(np.random.rand(5),index=['a','b','c','d','e'])
print(s1[1:4],s1[4])#下标
print(s2['a':'c'],s2['c']) #标签注意：用index做切片是末端包含
print(s2[0:3],s2[3])
print('------')
#下标索引做切片，和list写法一样
print(s2[:-1])
print(s2[::2])

###布尔型索引

#数组做判断之后，返回的是一个由布尔值组成的新的数组
#.isnull()/.notnull()判断是否为空值（None代表空值，NaN代表有问题的值，两个都会识别为空值）
s = pd.Series(np.random.rand(3)*100)
s[4] = None #添加一个空值
print(s)
bs1 = s>50
bs2 = s.isnull()
bs3 = s.notnull()
print(bs1,type(bs1),bs1.dtype)
print(bs2,type(bs2),bs2.dtype)
print(bs3,type(bs3),bs3.dtype)
#布尔型索引方法；用[判断条件]表示，其中判断条件可以是一个语句，或者是一个布尔型数组
print(s[s>50])
print(s[bs3])
print(s[bs2])

