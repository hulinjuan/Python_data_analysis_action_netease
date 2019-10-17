# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:47:18 2019

@author: lindsay.hu
"""

'''
【课程1.6】 Numpy数据的输入输出

numpy读取/写入数组数据，文本数据

'''
import numpy as np

#存储数组数据，npy文件
import os
os.chdir('C:\\Users\\lindsay.hu\\Desktop')
ar = np.random.rand(5,5)
print(ar)
np.save('test.npy',ar)
print('finished!')

#读取数组数据，npy文件
ar_load = np.load('test.npy')
print(ar_load)

#存成文本文件
ar = np.random.rand(5,5)
print(ar)
np.savetxt('savetxt_test.txt',ar,delimiter=',',fmt='%.2f')
print('finished!')
ar_loadtxt = np.loadtxt('savetxt_test.txt',delimiter=',')
print(ar_loadtxt) #读取被省略后的结果，因为fmt='%.2f'

