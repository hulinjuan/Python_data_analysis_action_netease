# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:36:08 2019

@author: lindsay.hu
"""

'''

【课程2.11】结构化图表可视化

FacetGrid

类似于matplotlib里面做子图，也类似于JointGrid,PairGrid
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("paper")
#设置风格、尺度

import warnings
warnings.filterwarnings("ignore")
#不发出警告

#1.基本设置
#绘制直方图

tips = sns.load_dataset("tips")
print(tips.head())
#导入数据

g = sns.FacetGrid(tips,col="time",row="smoker")
#创建一个绘制图表区域，设置号row，col分组

g.map(plt.hist,"total_bill",alpha=0.5,color='k',bins=10)
#以total_bill字段数据分别做直方图统计

#1.基本设置
#绘制直方图

g = sns.FacetGrid(tips,col="day",
                  size=4, #图表大小
                  aspect=5 #图表长宽比
                  )
g.map(plt.hist,"total_bill",bins=10,
      histtype="step", #"bar","harstacked","step","stepfilled"
      color='k')

#1.基本设置
#绘制散点图
g = sns.FacetGrid(tips,col="time",row="smoker")
#创建一个绘制图表区域，设置号row，col分组

g.map(plt.scatter,
      "total_bill","tip", #share(x,y) ->设置x，y数据
      edgecolor="b",s=40,linewidth=1 #设置点大小，描边宽度及颜色
      )
g.add_legend()
#添加图例

#1.基本设置
#分类
g = sns.FacetGrid(tips,col="time",hue="smoker")
#创建一个绘制图表区域，设置好col并分组，按hue分类

g.map(plt.scatter,
      "total_bill","tip", #share(x,y) ->设置x，y数据
      edgecolor="b",s=40,linewidth=1 #设置点大小，描边宽度及颜色
      )
g.add_legend()
#添加图例

#2、图表矩阵
attend = sns.load_dataset("attention")
print(attend.head())
#加载数据

g = sns.FacetGrid(attend,col="subject",col_wrap=5, #设置每行的图表数量
                  size=5)
g.map(plt.plot,"solutions","score",
      marker="o",color="gray",linewidth=2)
#绘制图表矩阵

g.set(xlim=(0,4),
      ylim=(0,10),
      xticks=[0,1,2,3,4],
      yticks=[0,2,4,6,8,10])
#s设置x轴、y轴刻度


