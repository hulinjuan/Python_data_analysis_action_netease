# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:06:33 2019

@author: lindsay.hu
"""

'''

【课程2.6】分布数据可视化 - 分类散点图

stripplot() /swarmplot() 

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("paper")
#设置风格、尺度

import warnings
warnings.filterwarnings('ignore')
#不发出警告

#1.stripplot()
#按照不同类别对样本数据进行分布散点图绘制

tips = sns.load_dataset("tips")
print(tips.head())
print(tips['day'].value_counts())
#加载数据

sns.stripplot(x='day',  # x -> 设置分组统计字段
              y='total_bill', # y -> 数据分布统计字段
              data = tips, #data -> 对应数据
              jitter = True, #jitter -> 当点数据重合较多时，用该参数做一些调整，也可以设置间距如：jitter=0.1
              size = 5,edgecolor='w',linewidth=1,marker='o' #设置点的大小，描边颜色或宽度，点样式              
            )

#1.stripplot()
#通过hue参数再分类
sns.stripplot(x='sex',y='total_bill',hue='day',
              data=tips,jitter=True)

#1.stripplot()
#设置调色盘
sns.stripplot(x='sex',y='total_bill',hue='day',
              data=tips,jitter=True,
              palette='Set2', #设置调色盘
              dodge=True #是否拆分
              )

#1.stripplot()
#筛选分类类别
print(tips['day'].value_counts())
#查看day字段的唯一值

sns.stripplot(x='day',y='total_bill',
              data=tips,jitter=True,
              order = ['Sat','Sun'])
#order ->筛选类别

#2.swarmplot() 
#分簇散点图

sns.swarmplot(x='total_bill',y='day',data=tips,
              size=5,edgecolor='w',linewidth=1,marker='o',
              palette='Reds')
#用法和stripplot类似


