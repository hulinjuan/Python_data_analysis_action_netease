# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:24:02 2020

@author: lindsay.hu
"""

'''
【课程1.6】 正态性检验（下）

Kolmogorov–Smirnov 是比较一个频率分布f(x)与理论分布g(x)或者连个观测值分布的是否不同的检验方法
以样本数据的累计频率分布与特定的理论分布比较（比如正态分布），如果两者差距小，则推论样本分布取自某特定分布

假设检验问题：
H0：样本的总体分布 服从 某特定分布
H1：样本的总体分布 不服从 某特定分布

Fn(x) -> 样本的累计分布函数
F0(x) -> 理论分布的分布函数
D -> F0(x)与Fn(x)差值的绝对值最大值
D = max|Fn(x)-F0(x)|

D > D(n,a) 相比较 ->
p>0.05则接受H0,P<0.05则拒绝H0，接受H1

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from scipy import stats
#scipy包是一个高级的科学计算库，它和numpy联系很密切，scipy一般是操控Numpy数组来进行科学计算

data = [87,77,92,68,80,78,84,77,81,80,80,77,92,86,
       76,80,81,75,77,72,81,72,84,86,80,68,77,87,
       76,77,78,92,75,80,78]
#样本数据，35位健康男性在未进食之前的血糖浓度

df = pd.DataFrame(data,columns=['value'])
u = df['value'].mean()
std = df['value'].std()
print('样本均值为：%.2f，样本标准差为：%.2f' % (u,std))
print('-------')

s = df['value'].value_counts().sort_index()
df_s = pd.DataFrame({'血糖浓度':s.index,'次数':s.values})
df_s['累计次数'] = df_s['次数'].cumsum()
df_s['累计频率'] = df_s['累计次数']/len(data)
df_s['标准化取值'] = (df_s['血糖浓度']-u)/std
df_s['理论分布'] = [0.0244,0.0968,0.2148,0.2643,0.3228,0.3859,0.5160,0.5832,0.7611,0.8531,0.8888,0.9803]#通过查阅正态分布表
#要通过标准化取值去查对应正态表中的值
df_s['D'] = np.abs(df_s['累计频率'] - df_s['理论分布'])
dmax = df_s['D'].max()
print('实际观测D值为:%.4f' % dmax)
#D值序列计算结果表格
#通过dmax查阅正态分布表，找到对应的a区间，
#如果大于0.05，表示接收原假设，累计分布是服从正态分布的
df_s['累计频率'].plot(style='--k') 
df_s['理论分布'].plot(style='--r')
plt.legend(loc='upper left')
plt.grid()
#密度图表示

#直接用算法做K-S检验
stats.kstest(df['value'],'norm',(u,std))
#.kstest方法，KS检验，
#参数分别是：待检验的数据，检验方法（这里设置成normz正态分布），均值与标准差
#结果返回两个值：statistic->D值，pvalue->P值
#p值大于0.05，为正态分布

