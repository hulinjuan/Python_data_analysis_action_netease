# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:25:59 2019

@author: lindsay.hu
"""

'''
【课程1.4】 Numpy索引及切片

核心：基本索引及切片、布尔型索引及切片
'''

import numpy as np

##基本索引及切片
#一维数组索引类似list
ar = np.arange(20)
print(ar)
print(ar[5])
print(ar[5:7])
print(ar[:3])
print(ar[::2])
#二维数组索引
ar2 =np.arange(16).reshape(4,4)
print(ar2)
print(ar2[2]) #指第二个元素,
print(ar2[2][3]) #二维数组的第三行的第4分元素
print(ar2[1:3]) #第二行到第三行
print(ar2[2,2]) #逗号，列；第二行第二列
print(ar2[:2,2:])
#三维数组索引
ar3 =np.arange(12).reshape(3,2,2) #3个二维数组,由高往低，这里最多有3个索引级别
print(ar3)
print(ar3[2])
print(ar3[2][1])
print(ar3[2][1][1])

##布尔型索引及切片:以布尔型的矩阵去做筛选
ar =np.arange(12).reshape(3,4)
print(ar)
i = np.array([True,False,True])
j = np.array([True,True,False,False])
print(i)
print(j)
print(ar[i])
print(ar[i,:2])
print(ar[:,j])

print(ar>5)
print(ar[ar>5])

##数组索引及切片的值更改、复制
#一个标量赋值给一个索引或切片时，会自动改变/传播原始数组
ar = np.arange(10)
print(ar)
ar[5] = 100
ar[7:9] = 200
print(ar)

ar = np.arange(10)
b = ar.copy()
b[7:9] = 200
print(ar)
print(b)

