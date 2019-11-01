# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:27:02 2019

@author: lindsay.hu
"""

'''

【课程2.3】调色盘

对图表整体颜色、比例等进行风格设置，包括颜色色板
调用系统风格进行数据可视化

color_palette()

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1.color_palette()
#默认6种颜色：deep,muted,pastel,bright,dark,colorblind
#有10种，哈哈
#seaborn.color_palette(palette=None,n_colors=None,desat=None)

current_palette = sns.color_palette()
sns.palplot(current_palette)

sns.palplot(sns.color_palette("hls",8))
#这里的颜色风格为hls
#颜色色块个数为8个
#风格颜色反转（不是所有颜色都可以反转）：Blues/Blues_r

#分组颜色设置 -"Paired"
sns.palplot(sns.color_palette("Paired",8))

#2.设置亮度，饱和度
#可用方法：
#（1）husl_palette([n_colors,h,s,l])
#（2）hls_palette([n_colors,h,s,l])
sns.palplot(sns.hls_palette(8,l=.3,s=.8))
#h,s和l值应该在0和1之间
#n_colors ->调色版中的颜色数
#h ->第一个色调
#l ->亮度
#s ->饱和度

#3.cubehelix_palette()
#按照线性增长计算，设置颜色

sns.palplot(sns.cubehelix_palette(8,gamma=2))
sns.palplot(sns.cubehelix_palette(8,start=0.5,rot=-.75))
sns.palplot(sns.cubehelix_palette(8,start=2,rot=0,dark=0,light=.95,reverse=True))
#n_colors ->颜色个数
#start ->值区间在0-3，开始颜色
#rot ->颜色旋转角度
#gamma ->颜色伽马值，越大颜色越暗
#dark,light ->值区间0-1，颜色深浅
#reverse ->布尔值，默认值False,由浅到深

#4.dark_palette(color[,n_colors,reverse,...])/light_palette(color[,n_colors,reverse,...])
#颜色深浅

sns.palplot(sns.light_palette("green")) #按照green做浅色调色盘
#sns.palplot(sns.light_palette("Greens")) #cmap为Greens风格

sns.palplot(sns.dark_palette("red",reverse=True)) #按照green做浅色调色盘
#reverse ->转置颜色

#5.diverging_palette()
#创建分散颜色
#seaborn.diverging_palette(h_neg, h_pos, s=75, l=50, sep=10, n=6, center='light', as_cmap=False)

sns.palplot(sns.diverging_palette(145,280,s=85,l=25,n=7))
#h_neg, h_pos：float in [0, 359]
# ->起始/终止颜色值。图的正负范围的锚定色调
#s -> 值区间0-100，饱和度
#l -> 值区间0-100，亮度
#n -> 颜色个数
#center ->中心颜色为浅色还是绿色"light","dark",默认为light

plt.figure(figsize=(8,6))
x = np.arange(25).reshape(5,5)
cmap = sns.diverging_palette(200,20,sep=20,as_cmap=True)
sns.heatmap(x,cmap=cmap)
#as_cmap ->布尔值，如果为 true，返回一个 matplotlib colormap 而不是一个颜色列表

#设置调色版后，绘制创建图表
sns.set_style("whitegrid")
#设置风格

#创建正弦函数及图表
def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*5)*(7-i)*flip)
        
with sns.color_palette("PuBuGn_d"):
    plt.subplot(211)
    sinplot()
    
sns.set_palette("husl")
plt.subplot(212)
sinplot()
#绘制系列颜色


