# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:46:16 2020

@author: lindsay.hu
"""

'''
【课程1.6】 正态性检验（上）

利用观测数据判断总体是否服从正态分布的检验称为正态性检验，
它是统计判决中重要的一种特殊的拟合优度假设检验

直方图初判/QQ图判断/K-S检验

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#直方图初判

s = pd.DataFrame(np.random.randn(1000)+10,columns=['value'])
print(s.head())
#创建随机数据

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(2,1,1) #创建子图1
ax1.scatter(s.index,s.value)
plt.grid() #加上了灰色的网格线
#绘制数据分布图

ax2 = fig.add_subplot(2,1,2)#创建子图2
s.hist(bins=30,alpha=0.5,ax = ax2)
s.plot(kind='kde',secondary_y=True,ax = ax2)
plt.grid()
#绘制直方图
#呈现较明显的正态性


#QQ图判断
#QQ图通过把测试样本数据的分位数与已知分布相比较，从而来检验数据的分布情况

#QQ图是一种散点图，对应于正态分布的QQ图，就是由标准正态分布的分位数为横坐标，样本值为纵坐标的散点图
#参考直线：四分之一分位点和四分之三分位点这两点确定，看散点是否落在这条线的附近

#绘制思路
#（1）在做好数据清洗后，对数据进行排序（次序统计量：x(1)<x(2)<....<x(n)）
#（2）排序后，计算出每个数据对应的百分位p(i)，即第i个数据x(i)为p(i)分位数，其中p(i)=(i-0.5)/n （p(i)有多重算法，这里以最常用算法为主）
#（3）绘制直方图+qq图，直方图作为参考

s = pd.DataFrame(np.random.randn(1000)+10,columns=['value'])
print(s.head())
#创建随机数据

mean = s['value'].mean()
std = s['value'].std()
print("均值为：%.2f,标准差为：%.2f" % (mean,std))
print('--------')
#计算均值，标准差

s.sort_values(by = 'value',inplace=True) #重新排序
s_r = s.reset_index(drop=False) #重新排序后，更新index
s_r['p'] = (s_r.index-0.5)/len(s_r)
s_r['q'] = (s_r['value']-mean)/std #标准化，可用可不用
print(s_r.head())
print('----------')
#计算百分位数p(i)
#计算q值

st = s['value'].describe()
x1,y1=0.25,st['25%']
x2,y2=0.75,st['75%']
print('四分之一位数为：%.2f,四分之三位数为：%.2f' % (y1,y2))
print('----------')
#计算四分之一位数，四分之三位数

fig = plt.figure(figsize = (10,9))
ax1 = fig.add_subplot(3,1,1) #创建子图1
ax1.scatter(s.index,s.value)
plt.grid()
#绘制数据分布图

ax2 = fig.add_subplot(3,1,2) #创建子图2
s.hist(bins=30,alpha=0.5,ax=ax2)
s.plot(kind='kde',secondary_y=True,ax=ax2)
plt.grid()
#绘制直方图

ax3 = fig.add_subplot(3,1,3)#创建子图3
ax3.plot(s_r['p'],s_r['value'],'k.',alpha=0.1)
ax3.plot([x1,x2],[y1,y2],'-r')
plt.grid()
#绘制QQ图，直线为四分之一位数，四分之三位数的连线，基本符合正态分布






