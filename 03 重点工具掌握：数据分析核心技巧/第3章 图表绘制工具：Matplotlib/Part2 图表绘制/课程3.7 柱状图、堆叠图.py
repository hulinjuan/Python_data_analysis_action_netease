# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:46:23 2019

@author: lindsay.hu
"""

'''
【课程3.7】  柱状图、堆叠图

plt.plot(kind='bar/barh') , plt.bar()
 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 柱状图与堆叠图
fig,axes = plt.subplots(4,1,figsize=(10,10))
s = pd.Series(np.random.randint(0,10,16),index=list('abcdefghijklmnop'))
df = pd.DataFrame(np.random.rand(10,3),columns=['a','b','c'])

s.plot(kind='bar',color='k',grid=True,alpha=0.5,ax=axes[0]) # ax参数 → 选择第几个子图
# 单系列柱状图方法一：plt.plot(kind='bar/barh')

df.plot(kind='bar',ax=axes[1],grid=True,colormap='Reds_r')
# 多系列柱状图

df.plot(kind='bar',ax=axes[2],grid=True,colormap='Blues_r',stacked=True)
# 多系列堆叠图
# stacked → 堆叠

df.plot.barh(ax=axes[3],grid=True,stacked=True,colormap='BuGn_r')
# 新版本plt.plot.<kind>

# 柱状图 plt.bar()
plt.figure(figsize=(10,4))
x = np.arange(10)
y1 = np.random.rand(10)
y2 = -np.random.rand(10)

plt.bar(x,y1,width = 1,facecolor = 'yellowgreen',edgecolor='white',yerr = y1*0.1)
plt.bar(x,y2,width = 1,facecolor = 'lightskyblue',edgecolor = 'white',yerr = y2*0.1)
# x,y参数：x，y值
# width：宽度比例
# facecolor柱状图里填充的颜色、edgecolor是边框的颜色
# left-每个柱x轴左边界,bottom-每个柱y轴下边界 → bottom扩展即可化为甘特图 Gantt Chart
# align：决定整个bar图分布，默认left表示默认从左边界开始绘制,center会将图绘制在中间位置
# xerr/yerr ：x/y方向error bar

for i,j in zip(x,y1):
    plt.text(i+0.01,j-0.15,'%.2f' % -j,color='white')
    
for i,j in zip(x,y2):
    plt.text(i+0.01,j+0.05,'%.2f' % -j,color='white')
# 给图添加text
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    
# 外嵌图表plt.table()
# table(cellText=None, cellColours=None,cellLoc='right', colWidths=None,rowLabels=None, rowColours=None, rowLoc='left',
# colLabels=None, colColours=None, colLoc='center',loc='bottom', bbox=None)

data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]
columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
df = pd.DataFrame(data,columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail'),
                 index = ['%d year' % x for x in (100, 50, 20, 10, 5)])
print(df)

df.plot(kind='bar',grid = True,colormap='Blues_r',stacked=True,figsize=(8,3))
# 创建堆叠图

plt.table(cellText = data,
          cellLoc = 'center',
          cellColours = None,
          rowLabels = rows,
          rowColours = plt.cm.BuPu(np.linspace(0,0.5,5))[::-1],# BuPu可替换成其他colormap,有10列的话，5改成10
          colLabels = columns,
          colColours = plt.cm.Reds(np.linspace(0, 0.5,5))[::-1],
          rowLoc = 'right',
          loc = 'bottom')
# cellText：表格文本
# cellLoc：cell内文本对齐位置
# rowLabels：行标签
# colLabels：列标签
# rowLoc：行标签对齐位置
# loc：表格位置 → left，right，top，bottom

plt.xticks([])
# 不显示x轴标注