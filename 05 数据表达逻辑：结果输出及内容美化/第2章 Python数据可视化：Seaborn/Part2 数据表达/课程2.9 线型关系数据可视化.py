# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:50:47 2019

@author: lindsay.hu
"""

'''

【课程2.7】分布数据可视化 - 统计图

lmplot()

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("paper")
#设置风格、尺度

import warnings
warnings.filterwarnings('ignore')
#不发出警告

#基本用法
tips = sns.load_dataset("tips")
print(tips.head())
#加载数据

sns.lmplot(x="total_bill",y='tip',
           data=tips,
           hue='smoker',
           palette='Set1',
           ci=70, #误差值
           size= 5, #图表大小
           markers=['+','o'],#点样式
           )

#拆分多个表格,做按照smoker分类个数作回归分析图
sns.lmplot(x="total_bill",y='tip',
           col='smoker',
           data=tips)

#多图表1
sns.lmplot(x='size',y='total_bill',hue='smoker',col='day',data=tips,
           aspect=0.6,#长宽比
           x_jitter=.30,#给x或者y轴随机增加噪音点,可以不设置
           col_wrap=2,#每行的列数
           )
#多图表2
sns.lmplot(x='total_bill',y='tip',row='sex',col='time',data=tips,size=4)
#行为sex字段,列为time字段
#x轴total_bill,y轴tip

#非线性回归
#order = 2 ,二次方回归
#order = 3,3次方回归
sns.lmplot(x='total_bill',y='tip',data=tips,
           order = 3
           )



  