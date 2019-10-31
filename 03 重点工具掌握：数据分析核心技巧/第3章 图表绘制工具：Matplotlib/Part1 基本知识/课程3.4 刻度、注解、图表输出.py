# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:12:54 2019

@author: lindsay.hu
"""

'''
【课程3.4】  刻度、注解、图表输出

主刻度、次刻度
 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#刻度

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

t = np.arange(0.0, 100.0, 1)
s = np.sin(0.1*np.pi*t)*np.exp(-t*0.01)
ax = plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置
plt.plot(t,s,'--*')
plt.grid(True, linestyle = "--",color = "gray", linewidth = 0.5,axis = 'both')  
# 网格
#plt.legend()  # 图例

xmajorLocator = MultipleLocator(10) # 将x主刻度标签设置为10的倍数
xmajorFormatter = FormatStrFormatter('%.0f') # 设置x轴标签文本的格式
xminorLocator   = MultipleLocator(5) # 将x轴次刻度标签设置为5的倍数  
ymajorLocator = MultipleLocator(0.5) # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%.1f') # 设置y轴标签文本的格式
yminorLocator   = MultipleLocator(0.1) # 将此y轴次刻度标签设置为0.1的倍数  

ax.xaxis.set_major_locator(xmajorLocator)  # 设置x轴主刻度
ax.xaxis.set_major_formatter(xmajorFormatter)  # 设置x轴标签文本格式
ax.xaxis.set_minor_locator(xminorLocator)  # 设置x轴次刻度

ax.yaxis.set_major_locator(ymajorLocator)  # 设置y轴主刻度
ax.yaxis.set_major_formatter(ymajorFormatter)  # 设置y轴标签文本格式
ax.yaxis.set_minor_locator(yminorLocator)  # 设置y轴次刻度

ax.xaxis.grid(True, which='both') #x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度
# which：格网显示

#删除坐标轴的刻度显示
#ax.yaxis.set_major_locator(plt.NullLocator()) 
#ax.xaxis.set_major_formatter(plt.NullFormatter()) 

# 注解

df = pd.DataFrame(np.random.randn(10,2))
df.plot(style='--o')
plt.text(5,0.5,'hahah',fontsize=10)
# 注解 → 横坐标，纵坐标，注解字符串

# 图表输出

df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
df = df.cumsum()
df.plot(style = '--.',alpha = 0.5)
plt.legend(loc = 'upper left')
plt.savefig('C:/Users/lindsay.hu/Desktop/pic.png',
            dpi=400,
            bbox_inches = 'tight',
            facecolor = 'g',
            edgecolor = 'b')
# 可支持png，pdf，svg，ps，eps…等，以后缀名来指定
# dpi是分辨率
# bbox_inches：图表需要保存的部分。如果设置为‘tight’，则尝试剪除图表周围的空白部分。
# facecolor，edgecolor： 图像的背景色，默认为‘w’（白色）
