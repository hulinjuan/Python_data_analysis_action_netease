# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:46:18 2019

@author: lindsay.hu
"""

'''

【课程2.2】整体风格设置

对图表整体颜色、比例等进行风格设置，包括颜色色板
调用系统风格进行数据可视化

set() / set_style() / axes_style() /set_content()

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#创建正弦函数及图表
def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*5)*(7-i)*flip)
sinplot()
#创建正弦函数，及出图

#1.set()
sns.set() #默认，暗色风格，网格显示
sinplot()
plt.grid(linestyle='--')

#2.set_style()
#切换seaborn图表风格
#风格选择包括："white","dark","whitegrid","darkgrid","ticks"

fig = plt.figure(figsize=(6,6))

ax1 = fig.add_subplot(2,1,1)
sns.set_style("whitegrid")
data = np.random.normal(size=(20,6)) + np.arange(6)/2
sns.boxplot(data=data)
plt.title('style -whitegrid')
#仍然可以使用matplotlib的参数

ax2 = fig.add_subplot(2,1,2)
#sns.set_style("dark")
sinplot()
#子图显示

#3.despine（
#设置图表坐标轴
#seaborn.despine(fig=None,ax=None,top=True,right=True,left=False,
#bottom=False,offset=None,trim=False)

sns.set_style("ticks")
#设置风格

fig = plt.figure(figsize=(6,9))
plt.subplots_adjust(hspace=0.3)
#创建图表

ax1 = fig.add_subplot(3,1,1)
sinplot()
sns.despine()
#删除了上，右坐标轴

ax2 = fig.add_subplot(3,1,2)
sns.violinplot(data=data)
#sns.despine(offset=10,trim=True)
#offset:与周标准之间的偏移
#trim:为True时，将坐标轴限制在数据最大最小值

ax3 = fig.add_subplot(3,1,3)
sns.boxplot(data=data,palette="deep")
#sns.despine(left=True,right=False)
#top,right,left,bottom:布尔型，为True时不显示

#4.axes_style()
#设置局部图表风格，可学习和with配合的用法
with sns.axes_style("darkgrid"):
    plt.subplot(211)
    sinplot()
#设置局部图表风格，用with做代码块区分

sns.set_style("whitegrid")
plt.subplot(212)  
sinplot()
#外部表格风格

#5.set_content()
#设置显示比例尺度
#选择包括：'paper','notebook','talk','poster'

sns.set_context("paper")
sinplot()
#默认为notebook

