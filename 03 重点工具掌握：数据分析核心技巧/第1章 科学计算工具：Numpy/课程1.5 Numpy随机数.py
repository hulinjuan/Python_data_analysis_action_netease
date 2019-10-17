# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:51:30 2019

@author: lindsay.hu
"""

'''
【课程1.5】 Numpy随机数

numpy.random包含多种概率分布的随机样本，
是数据分析辅助的重点工具之一

'''
import numpy as np

#随机数生成
#numpy.random.normal(),标准正态分布
samples = np.random.normal(size=(4,4))
print(samples)
#numpy.random.rand(d0,d1,...dn)，均匀分布
#:生成一个[0,1)之间的随机浮点数或N维浮点数组 
a = np.random.rand()
print(a,type(a))
print(np.random.rand(4))
print(np.random.rand(2,4))
print(np.random.rand(2,4)*100)

data1 = np.random.rand(500)
data2 = np.random.rand(500)
data3 = np.random.randn(500)
data4 = np.random.randn(500)
import matplotlib.pyplot as plt
% matplotlib inline  ##只有jupter book才能用
plt.scatter(data1,data2)
plt.scatter(data3,data4)

#numpy.random.randint(low,high=None,size=None,dtypr='l'):生成1个整数或N维整数数组
#若high不为None时，取[low,high)之间的随机整数，否则取[0,low)之间随机整数，且high必须大于low
#dtype参数：只能是int类型
print(np.random.randint(2))
print(np.random.randint(2,10))
print(np.random.randint(2,size=10)) #生成10个[0,2之间的随机整数)
print(np.random.randint(10,size=(2,5)))
print(np.random.randint(10,50,size=(2,5)))
