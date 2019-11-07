# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:20:57 2019

@author: lindsay.hu
"""

'''

【课程2.7】分布数据可视化 - 分布图

boxplot() /violinplot() / lvplot()

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

#1.boxplot() 
#箱型图
tips = sns.load_dataset("tips")

sns.boxplot(x='day',y='total_bill',data=tips,
            linewidth=2,#线宽
            width=0.8,#箱之间的间隔比例
            fliersize=3,#异常点大小
            palette = 'hls',#设置调色版
            whis = 1.5,#设置IQR
            notch = True, # 设置是否以中值做凹槽
            order = ['Thur','Fri','Sat','Sun'] #筛选类别
            )
#绘制箱型图

sns.swarmplot(x='day',y='total_bill',data=tips,
              color='k',size=3,alpha=0.8)
#可以添加散点图

#1.boxplot() 
#通过hue参数再分类

sns.boxplot(x='day',y='total_bill',data=tips,
            hue='smoker',palette='Reds')
#绘制箱型图

#2.violinplot()
#小提琴图，和箱型图类似。显示了分布，小提琴两边对称

sns.violinplot(x='day',y='total_bill',data=tips,
               linewidth=2,#线宽
               width=0.8,#箱之间的间隔比例
               palette = 'hls',#设置调色版
               order = ['Thur','Fri','Sat','Sun'], #筛选类别
               scale = 'count',#测度小提琴图的宽度：area-面积相同，count-按照样本数量决定宽度，width-宽度一样
               #gridsize = 10,#设置小提琴图边线的平滑度，越高越平滑
               inner = 'box',#设置内部显示类型->'box','quartile','point','stick',None
               bw=0.8 #控制拟合程度，一般可以不设置
               )

#2.violinplot()
#通过hue参数再分类

sns.violinplot(x='day',y='total_bill',data=tips,
               hue = 'smoker',palette='muted',
               split=True,#设置是否拆分小提琴图
               inner='quartile'
        )

#2.violinplot()
#结合散点图

sns.violinplot(x='day',y='total_bill',data=tips,palette='hls',inner=None)
sns.swarmplot(x='day',y='total_bill',data=tips,color='w',alpha=.5)

#3.lvplot()
#LV图表

sns.lvplot(x='day',y='total_bill',data=tips,palette='mako',
        #hue = 'smoker',
        width = 0.8, #箱之间间隔比例
        linewidth = 12,
        scale = 'area', #设置框的大小 -> 'linear','exonential','area'
        k_depth = 'proportion', #设置框的数量 -> 'proportion','tukey','trustworthy'
        )
#绘制LV图

sns.swarmplot(x='day',y='total_bill',data=tips,color='k',alpha=0.8)
#可以添加散点图


