# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:18:00 2019

@author: lindsay.hu
"""

'''
【课程3.15】  表格样式调用

Styler内置样式调用
 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline #jupyter 运行

##以下代码需要在交互式下才可以使用
# 按照百分数显示

# 定位空值

df = pd.DataFrame(np.random.rand(5,4),columns = list('ABCD'))
df['A'][2] = np.nan
df.style.highlight_null(null_color='red')

# 色彩映射

df = pd.DataFrame(np.random.rand(10,4),columns = list('ABCD'))
df.style.background_gradient(cmap='Greens',axis =1,low=0,high=1)
# cmap：颜色
# axis：映射参考，0为行，1以列

# 条形图

df = pd.DataFrame(np.random.rand(10,4),columns = list('ABCD'))
df.style.bar(subset=['A', 'B'], color='#d65f5f', width=100)
# width：最长长度在格子的占比

# 分段式构建样式

df = pd.DataFrame(np.random.rand(10,4),columns = list('ABCD'))
df['A'][[3,2]] = np.nan
df.style.\bar(subset=['A', 'B'], color='#d65f5f', width=100)
        .\highlight_null(null_color='yellow')

