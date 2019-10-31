# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:52:32 2019

@author: lindsay.hu
"""

'''
【课程3.1】  Matplotlib简介及图表窗口

Matplotlib → 一个python版的matlab绘图接口，以2D为主，支持python、numpy、pandas基本数据结构，运营高效且有较丰富的图表库
 
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 图表窗口1 → plt.show()

plt.plot(np.random.rand(10))
plt.show()
# 直接生成图表

# 图表窗口2 → 魔法函数，嵌入图表

% matplotlib inline    #spyder中不需要
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y)
# 直接嵌入图表，不用plt.show()
# <matplotlib.collections.PathCollection at ...> 代表该图表对象

# 图表窗口3 → 魔法函数，弹出可交互的matplotlib窗口

% matplotlib notebook #spyder中不需要
s = pd.Series(np.random.randn(100))
s.plot(style = 'k--o',figsize=(10,5))
# 可交互的matplotlib窗口，不用plt.show()
# 可做一定调整

# 图表窗口4 → 魔法函数，弹出matplotlib控制台

% matplotlib qt5
df = pd.DataFrame(np.random.rand(50,2),columns=['A','B'])
df.hist(figsize=(12,5),color='g',alpha=0.8)
# 可交互性控制台
# 如果已经设置了显示方式（比如notebook），需要重启然后再运行魔法函数
# 网页嵌入的交互性窗口 和 控制台，只能显示一个

#plt.close()    
# 关闭窗口

#plt.gcf().clear()  
# 每次清空图表内内容



