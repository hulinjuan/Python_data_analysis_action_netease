# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:27:52 2019

@author: lindsay.hu
"""
'''

【课程2.5】分布数据可视化 - 散点图

joinplot() /pairplot() 

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

#1.综合散点图-joinplot()
#散点图+分布图

rs = np.random.RandomState(2) #设定随机数种子
df = pd.DataFrame(rs.randn(200,2),columns=['A','B'])
#创建数据

sns.jointplot(x=df['A'],y=df['B'],#设置x,y轴，显示columns名称
              data = df,#设置数据
              color = 'k',#设置颜色
              s = 50,edgecolor="w",linewidth=1,#设置散点大小，边缘线颜色及宽度（只针对scatter)
              kind = 'scatter' ,#设置类型："scatter","reg","resid","kde","hex"
              space = 0.2, #设置散点图和布局图的间距
              size =5, #图表大小（自动调整为正方形）
              ratio = 5,#散点图与布局图高度比，整型
              marginal_kws = dict(bins=15,rug=True) #设置柱状图箱数，是否设置rug;若果上面设置了kde，这个参数不要
              )

#1.综合散点图-joinplot()
#散点图+分布图
#密度图
rs = np.random.RandomState(15) #设定随机数种子
df = pd.DataFrame(rs.randn(300,2),columns=['A','B'])
#创建数据

g = sns.jointplot(x=df['A'],y=df['B'],data=df,
                      kind="kde",color="k",
                      shade_lowest=False)
#创建密度图

g.plot_joint(plt.scatter,c="w",s=30,linewidth=1,marker="+")
#添加散点图

#1.综合散点图 - JointGrid()
#可拆分绘制的散点图
#plot_joint() + ax_marg_x.hist() + ax_marg_y.hist()

sns.set_style("white")
#设置风格

tips = sns.load_dataset("tips")
print(tips.head())
#导入数据

g = sns.JointGrid(x="total_bill",y="tip",data=tips)
#创建一个绘图表格区域，设置好x,y对应数据

g.plot_joint(plt.scatter,color='m',edgecolor='white') #设置框内图表，scatter
g.ax_marg_x.hist(tips["total_bill"],color='b',alpha=0.6,
                 bins=np.arange(0,60,3)) #设置x轴直方图，注意bins是数组

g.ax_marg_y.hist(tips["tip"],color='r',alpha=0.6,
                 orientation = "horizontal",
                 bins=np.arange(0,12,1)) #设置y轴直方图，注意需要 orientation参数 


from scipy import stats
g.annotate(stats.pearsonr)
#设置标注，可以为pearsonr,spearmanr

plt.grid(linestyle= '--')



#1.综合散点图 - JointGrid()
#可拆分绘制的散点图
#plot_joint() + plot_marginals()

g = sns.JointGrid(x='total_bill',y='tip',data=tips)
#创建一个绘图表格区域，设置好x,y对应数据

g = g.plot_joint(plt.scatter,color='g',s=40,edgecolor='white') #绘制散点图
plt.grid(linestyle='--')

g.plot_marginals(sns.distplot,kde=True,color='g')#绘制x轴，y轴

#1.综合散点图 - JointGrid()
#可拆分绘制的散点图
#plot_joint() + plot_marginals()
#kde密度图
g1 = sns.JointGrid(x='total_bill',y='tip',data=tips)
g1 = g.plot_joint(sns.kdeplot,cmap='Reds_r') #绘制密度图
g1.plot_marginals(sns.kdeplot,shade=True,color='r')#绘制x轴，y轴

#2.矩阵散点图 --pairplot()

sns.set_style('white')
#设置风格

iris = sns.load_dataset('iris')
print(iris.head())
#读取数据

sns.pairplot(iris,
             kind = 'scatter',#散点图/回归分布图（'scatter','reg'）
             diag_kind='hist',#直方图/密度图（'hist','kde'）
             hue = 'species', #按照某一字段进行分类
             palette = 'husl', #设置调色板
             markers = ['o','s','D'], #设置不同系列的点样式（这里根据参考分类个数）
             size = 2 #图表大小
            )

#2.矩阵散点图 --pairplot()
#只提取局部变量进行对比

sns.pairplot(iris,
             vars=['sepal_width','sepal_length'],
             kind='reg',
             diag_kind='kde',
             hue='species',
             palette='husl')


#2.矩阵散点图 --pairplot()
#其他参数设置
sns.pairplot(iris,
             diag_kind='kde',
             markers='+',
             plot_kws=dict(s=50,edgecolor="b",linewidth=1),
             #设置点样式
             diag_kws=dict(shade=True)
             #设置密度图样式
             )

#2.矩阵散点图 - PairGrid()
#可拆分绘制的散点图
#map_diag() + map_offdiag()
g = sns.PairGrid(iris,hue='species',palette='hls',
                 vars=['sepal_length','sepal_width','petal_length','petal_width'], #可筛选
                 )
#创建一个绘图表格区域，设置好x，y对应数据，按照species分类

g.map_diag(plt.hist,
           histtype='barstacked', #可选：'bar'，'barstacked'，'step'，'stepfill'
           linewidth=1,edgecolor='w')
#对角线图表，plt.hist/sns.kdeplot

g.map_offdiag(plt.scatter,
              edgecolor='w',s=40,linewidth=1,#设置点颜色，大小，描边宽度
              )
#其他图表，plt.scatter/plt.bar..

g.add_legend()
#添加图例

#2.矩阵散点图 - PairGrid()
#可拆分绘制的散点图
#map_diag() + map_lower() + map_upper()
g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot,lw=1) #设置对角线图表
g.map_upper(plt.scatter,color='r') #设置对角线上端图表
g.map_lower(sns.kdeplot,cmap='Blues_d') #设置对角线下端图表
