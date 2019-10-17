# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:39:07 2019

@author: lindsay.hu
"""

import numpy as np 

'''多维数组ndarray'''

#数组的基本属性
ar = np.array([1,2,3,4,5,6,7])
print(ar) #输出数组，注意数组的格式：中括号，元素之间没有逗号（和列表区分
print(ar.ndim) #输出数组维度的个数（轴数），或者说"秩"，维度的数量也成rank
print(ar.shape)#数组的维度，对于n行m列的数组，shape为(n,m)
print(ar.size)#数组的元素总数，对于n行m列的数组，size为n*m
print(ar.dtype) #数组中元素的类型，类似type()，但是type()是函数，dtype是方法
print(ar.itemsize)#数组中每个元素的字节大小，int32字节为4，float64字节为8
print(ar.data) #包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性
ar #交互方式下输出，会有array(数组)

#创建数组，array()函数,括号内可以是列表，元组，数组，生成器等
ar1 = np.array(range(10))
ar2 = np.arange(10)
ar3 = np.array([1,2,3,4,5])
ar4 = np.array([[1,2,3,4,5],[1,2,3,4,5]]) #嵌套列表
ar5 = np.array([[1,2,3,4,5],['a','b','c','d','e']])
ar6 = np.array([[1,2,3,4,5],['a','b','c','d','e','f']])
print(ar5.ndim) 
print(ar6.ndim)#元素 个数不一样会造成变成1位数组
print(ar1)
print(ar2)
print(ar3)
print(ar4)
print(ar5)
print(ar6)

print(np.arange(5,12,2)) #返回5-12，步长为2

#创建数组：linspace():返回在间隔[开始，停止]上计算的num个均匀间隔的样本
a = np.linspace(10,20,num = 21)
print(np.linspace(10,20,num = 21,endpoint = False)) #最后一个值不包含
s = np.linspace(10,20,num = 21,retstep = True) #最后一个值不包含
print(s)
print(type(s)) #s是元祖
print(s[0])
print(type(a)) #a是数组

#创建数组：zeros()/zeros_like()/ones()/ones_like()
print(np.zeros((3,5),dtype=np.int))

ar = np.array([list(range(10)),list(range(10,20))])
print(np.zeros_like(ar)) #创建一个和ar.shape一样的全0数组
print(np.ones_like(ar)) #创建一个和ar.shape一样的全1数组

#创建数组：eye(),创建一个正方的n*n的单位矩阵，对角是1，其余全是0
print(np.eye(5))