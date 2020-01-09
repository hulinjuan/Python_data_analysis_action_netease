# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:49:59 2020

@author: lindsay.hu
"""


'''
【课程1.5】 帕累托分析

帕累托分析（贡献度分析）-> 帕累托法则：20/80定律

“原因和结果、投入和产出，努力和报酬之间本来存在这无法解释的不平衡。
一般来书，投入和努力可以分为两种不同的类型：
多数，它们只能造成少许的影响；少数，它们造成主要的、重大的影响”

-> 一个公司，80%的利润来自20%的畅销产品，而其他80%的产品只产生了20%的利润

一个思路：通过二八法则，去寻找关键的那20%的决定性因素！
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(10)*1200+3000,
                    index=list('ABCDEFGHIJ'))
#创建数据

data.sort_values(ascending=False,inplace=True)
print(data)

plt.figure(figsize =(10,4))
data.plot(kind='bar',color='g',alpha=0.8,width=0.6)

p = data.cumsum()/data.sum()
key = p[p>0.8].index[0]
key_num = data.index.tolist().index(key)
print('超过80%累计占比的节点值索引为：',key)
print('超过80%累计占比的节点值索引位置为：',key_num)
#找到累计占比超过80%时候的index
#找到key所对应的索引位置

p.plot(style='--ko',secondary_y=True)
plt.axvline(key_num,color='r',linestyle='--') #80%参考线
plt.text(key_num+0.2,p[key],'累计占比为：%.3f%%' % (p[key]*100),color='r') #累计占比超过80%的节点
plt.ylabel('营收_比例')
#绘制营收累计占比曲线

key_product = data.loc[:key]
print('核心产品为：')
print(key_product)
#输出决定性因素产品


