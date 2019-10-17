# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:01:03 2019

@author: lindsay.hu
"""

'''
【课程1.3】 Numpy通用函数
基本操作
'''

import numpy as np

##数组形状：.T/.reshape()/.resize()

#.T方法：转置，
#例如原shape为(3,4)/(2,3,4),转置结果为(4,3)/(4,3,2) 
#->所以1维数组转置后结果不变
ar1 = np.arange(10)
ar2 = np.zeros((2,5))
print(ar1,'\n',ar1.T)
print(ar2,'\n',ar2.T)
print('-------')

#np.reshape,元素要一样多
ar3 = ar1.reshape(2,5) #用法1：直接将已有数据改变形状
ar4 = np.zeros((4,6)).reshape(3,8) #用法2：生成数组后直接改变形状
ar5 = np.reshape(np.arange(12),(3,4)) #用法3：参数内添加数组，目标形状
print(ar1,'\n',ar3)
print(ar4)
print(ar5)
print('-------')

##np.resize,不管是多还是少，都会依次排出来
print(np.resize(np.arange(5),(3,4)))

##数组的复制
ar1 = np.arange(10)
ar2 = ar1  #指向同一个数组
print(ar1 is ar2)
ar1[2] = 100
print(ar1,ar2)
ar3 = ar1.copy()  #新生成了一个数组
ar1[3] = 1000
print(ar1,ar3)
s = np.arange(10)
print(np.resize(s,(2,6))) #np.resize会生成新数组
print(s.resize(2,6)) #结果为None,因为数组.resize改变数组本身
print(s)

##数组类型转换：.astype()
ar1 = np.arange(10,dtype= float)
ar2 = ar1.astype(np.int64)
print(ar1,ar1.dtype)
print(ar2,ar2.dtype)

##数组堆叠
a = np.arange(5)
b = np.arange(5,9)
print(a)
print(b)
print(np.hstack((a,b))) #横向连接
print('------')

a = np.array([[1],[2],[3]])
b = np.array([['a'],['b'],['c']])
print(a)
print(b)
print(np.vstack((a,b))) #纵向连接，保证连接的两个数组的列的数量一样

a = np.arange(5)
b = np.arange(5,10)
print(np.stack((a,b),axis=1)) #轴参数默认是0：纵向连接，axis=1:横向连接

##数组拆分
ar = np.arange(16).reshape(4,4)
print(ar)
print(np.hsplit(ar,2)) #拆成2列
print(np.hsplit(ar,2)[0]) #拆成2列的第一列
print(np.vsplit(ar,2)) #拆成2列

##数组的简单运算
#与标量的运算
ar = np.arange(6).reshape(2,3)
print(ar + 10) #加法
print(ar * 2) #乘法
print(ar/(ar+1)) #除法
print(ar ** 0.5) #幂
#常用函数
print(ar.mean()) #平均值
print(ar.max()) #最大值
print(ar.min()) #最小值
print(ar.std()) #标准差
print(ar.var()) #方差
print(ar.sum(),np.sum(ar,axis = 0)) #求和，np.sum()->axis=0，按列求和；axis为1，按行求和
print(np.sort(np.array([1,4,3,2,5,6]))) #排序
