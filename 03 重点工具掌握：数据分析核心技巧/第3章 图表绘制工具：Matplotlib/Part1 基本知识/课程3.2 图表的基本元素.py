# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:06:56 2019

@author: lindsay.hu
"""

'''
【课程3.2】  图表的基本元素

图表内基本参数设置
 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#图名，图例，轴标签，轴边界，轴刻度，轴刻度标签等

df = pd.DataFrame(np.random.rand(10,2),columns=['A','B'])
fig = df.plot(figsize=(6,4))
#figsize：创建图表窗口，设置窗口大小
#创建图表对象，并赋值与fig
print(fig,type(fig))

plt.title('Interesting Graph - Check it out')  # 图名
plt.xlabel('Plot Number')  # x轴标签
plt.ylabel('Important var') # y轴标签

plt.legend(loc = 'upper right')  
# 显示图例，loc表示位置
# 'best'         : 0, (only implemented for axes legends)(自适应方式)
# 'upper right'  : 1,
# 'upper left'   : 2,
# 'lower left'   : 3,
# 'lower right'  : 4,
# 'right'        : 5,
# 'center left'  : 6,
# 'center right' : 7,
# 'lower center' : 8,
# 'upper center' : 9,
# 'center'       : 10,

plt.xlim([0,12])  # x轴边界
plt.ylim([0,1.5])  # y轴边界
plt.xticks(range(10))  # 设置x刻度
plt.yticks([0,0.2,0.4,0.6,0.8,1.0,1.2])  # 设置y刻度
fig.set_xticklabels("%.1f" %i for i in range(10)) # x轴刻度标签
fig.set_yticklabels("%.2f" %i for i in [0,0.2,0.4,0.6,0.8,1.0,1.2])  # y轴刻度标签
# 范围只限定图表的长度，刻度则是决定显示的标尺 → 这里x轴范围是0-12，但刻度只是0-9，刻度标签使得其显示1位小数
# 轴标签则是显示刻度的标签

print(fig,type(fig))
# 查看表格本身的显示方式，以及类别

# 其他元素可视性

x = np.linspace(-np.pi,np.pi,256,endpoint = True)
c, s = np.cos(x), np.sin(x)
plt.plot(x, c)
plt.plot(x, s)
# 通过ndarry创建图表

#plt.grid()
plt.grid(True, linestyle = "--",color = "gray", linewidth = 0.5,axis = 'x')  
# 显示网格
# linestyle：线型
# color：颜色
# linewidth：宽度
# axis：x，y，both，显示x/y/两者的格网

plt.tick_params(bottom='on',top='off',left='on',right='off')  
# 刻度显示

import matplotlib
matplotlib.rcParams['xtick.direction'] = 'out' 
matplotlib.rcParams['ytick.direction'] = 'inout' 
# 设置刻度的方向，in,out,inout
# 这里需要导入matploltib，而不仅仅导入matplotlib.pyplot

#通过plt.gca()获得当前的Axes对象ax,Get Current Axes
frame = plt.gca()
plt.axis('off')
# 关闭坐标轴
frame.axes.get_xaxis().set_visible(False)
#frame.axes.get_yaxis().set_visible(False)
# x/y 轴不可见



