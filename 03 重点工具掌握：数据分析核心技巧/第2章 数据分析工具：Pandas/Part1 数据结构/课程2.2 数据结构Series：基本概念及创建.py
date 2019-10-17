# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:00:54 2019

@author: lindsay.hu
"""

'''
【课程2.2】 数据结构Series：基本概念及创建

numpy读取/写入数组数据，文本数据

'''
import numpy as np
import pandas as pd

###Series 数据结构
#Series是带有标签的一维数组，
#可以保存任何数据类型(整数，字符串，浮点数，Python对象等)，
#轴标签统称为索引

#.index查看Series索引,类型为rangeindex
#.values查看Series值，类型是ndarray

#核心：series相比于ndarray，是一个自带索引index的数组 ->一维数组，对应索引
#所以当只看Series的值的时候，就是一个ndarray
#series和ndarray较相似，索引切片功能差别不大
#series和dict相比,series更像是一个有序字典(dict本身不存在顺序)，其索引原理与字典相似（一个用key,一个用index）

ar = np.random.rand(5)
s = pd.Series(ar)
print(ar)
print(s)
print(type(s))
print('-----')
print(list(s.index))
print(s.values)

y = pd.Series(ar,index=list('abcde'))
print(y)

#Series创建方法一：由字典创建，字典的key就是index，values就是values
dic = {'a':1,'b':2,'c':3,4:3,5:50}
s = pd.Series(dic)
print(s)
#Series创建方法二：由一维数组创建
arr = np.random.rand(10)
s = pd.Series(arr)
print(s)

#Series创建方法三：通过标量创建
s = pd.Series(100,index=range(4))
print(s)

#pd.Series([data, index, dtype, name, copy, …])参数
#index参数：设置index,长度保持一致
#dtype参数：设置数值类型
#name参数：名称属性，创建一个数组的名称，类似于表名
#name方法：输出数组的名称，输出格式为str，如果没用定义输出名称，输出为None
#.rename()重命名一个数组的名称，并且新指向一个数组，原数组不变
arr = np.random.rand(10)*100
s = pd.Series(arr,index=list('abcdefghij'),dtype=np.object)
print(s)

s1 =  pd.Series(np.random.rand(5))
print(s1)
print('------')
s2 = pd.Series(np.random.rand(5),name='test')
print(s2)
print(s1.name,s2.name,type(s2.name))
s3 = s2.rename('hehehe')
print(s3.name,s2.name)