# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:40:22 2020

@author: lindsay.hu
"""

'''
【课程1.7】 相关性分析

相关性分析是指对两个或多个具备相关性的变量元素进行分析，从而衡量两个变量因素的相关密切程度
相关性的元素之间需要存在一定的联系或概率才可以进行相关性分析

1.图示初判
2.Pearson相关系数（皮尔逊相关系数）
3.Sperman秩相关系数（斯皮尔曼相关系数）

0<|r|<1 表示存在不同程度线性相关

|r|<=0.3 -> 不存在线性相关
0.3<|r|<=0.5 -> 低度线性相关
0.5<|r|<=0.8 -> 显著线性相关
|r|>0.8 -> 高度线性相关

#2.Pearson相关系数
是一种线性相关系数
衡量向量相似度的一种方法。输出范围为-1到+1,0代表无相关性，负值为负相关，正值为正相关
前提条件 -> 正态分布
公式自行百度、推导。(或者见下面代码中的计算步骤)

#3.Speraman秩相关系数
Pearson相关系数主要用于服从正态分布的连续变量，不服从正态分布的变量，分类的关联性可采用
Spearman秩相关系数，也称等级相关系数。

计算逻辑：
(1)对两个变量成对的取值按照从小到大的顺序编秩，Rx代表Xi的秩次，Ry代表Yi的秩次
**如果两个值大小一样，则秩次为（index1 + index2）/2
(2)di = Rx-Ry
(3)Spearman系数和Pearson系数在效率上等价
公式自行百度、推导。(或者见下面代码中的计算步骤)
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#图示初判
#（1）变量之间的线性相关性
data1 = pd.Series(np.random.rand(50)*100).sort_values()
data2 = pd.Series(np.random.rand(50)*50).sort_values()
data3 = pd.Series(np.random.rand(50)*500).sort_values(ascending=False)
#创建三个数据：data1为0-100的随机数并从小到大排列，
#data2为0-50的随机数数并从小到大排列，
#data2为0-500的随机数数并从大到小排列

fig = plt.figure(figsize = (10,4))
ax1 = fig.add_subplot(1,2,1)
ax1.scatter(data1,data2)
plt.grid()
#正线性相关

ax2 = fig.add_subplot(1,2,2)
ax2.scatter(data1,data3)
plt.grid()
#负线性相关

#图示初判
#（1）散点图矩阵初判多变量之间的关系
data = pd.DataFrame(np.random.randn(200,4)*100,columns=['A','B','C','D'])
pd.scatter_matrix(data,figsize=(8,8),
                  c = 'k',
                  marker='+',
                  diagonal='hist',
                  alpha=0.8,
                  range_padding=0.1)

#Pearson相关系数
data1 = pd.Series(np.random.rand(100)*100).sort_values()
data2 = pd.Series(np.random.rand(100)*50).sort_values()
data = pd.DataFrame({'value1':data1.values,
                     'value2':data2.values})
print(data.head())
print('------------')
#创建样本数据

u1,u2 = data['value1'].mean(),data['value2'].mean() #计算均值
std1,std2 = data['value1'].std(),data['value2'].std() #计算标准差
print('value1正态性检验：\n',stats.kstest(data['value1'],'norm',(u1,std1)))
print('value2正态性检验：\n',stats.kstest(data['value2'],'norm',(u2,std2)))
print('---------------')
#正态性检验 -> pvalue>0.05

data['(x-u1)*(y-u2)'] = (data['value1']-u1)*(data['value2']-u2)
data['(x-u1)**2'] = (data['value1'] - u1)**2
data['(y-u2)**2'] = (data['value2'] - u2)**2
print(data.head())
print('------------')
#根据公式计算，制作Pearson相关系数求值表

r = data['(x-u1)*(y-u2)'].sum()/(np.sqrt(data['(x-u1)**2'].sum()*data['(y-u2)**2'].sum()))
print('Pearson相关系数为：%.4f' % r)
#求出r
#|r|>0.8 -> 高度线性相关

#Pearson相关系数（直接调用pandas中的corr函数）
data1 = pd.Series(np.random.rand(100)*100).sort_values()
data2 = pd.Series(np.random.rand(100)*50).sort_values()
data = pd.DataFrame({'value1':data1.values,
                     'value2':data2.values})
data.corr()
#pandas相关性方法：data.corr(method='pearson',min_periods=1)->直接给出数据字段的相关系数矩阵
#method默认pearson

#Spearman秩相关系数
data = pd.DataFrame({'智商':[106,86,100,101,99,103,97,113,112,110],
                     '每周看电视小时数':[7,0,27,50,28,29,20,12,6,17]})
#print(data)
#print('---------')
#创建样本数据

data.sort_values('智商',inplace=True)
data['range1'] = np.arange(1,len(data)+1)
data.sort_values('每周看电视小时数',inplace=True)
data['range2'] = np.arange(1,len(data)+1)
#print(data)
#print('-------------')
#'智商'、'每周看电视小时数'重新按照从小到大排序，并设定秩次index

data['d'] = data['range1'] - data['range2']
data['d2'] = data['d']**2
#print(data)
#print('---------------')
#求出di,di2

n = len(data)
rs = 1-6*(data['d2'].sum())/(n*(n**2-1))
print('Sperman相关系数为：%.4f' % rs)
#求出rs

#Spearman相关系数（直接调用pandas中的corr函数）
data = pd.DataFrame({'智商':[106,86,100,101,99,103,97,113,112,110],
                     '每周看电视小时数':[7,0,27,50,28,29,20,12,6,17]})
data.corr(method='spearman')
#pandas相关性方法：data.corr(method='pearson',min_periods=1)->直接给出数据字段的相关系数矩阵
#method默认pearson

