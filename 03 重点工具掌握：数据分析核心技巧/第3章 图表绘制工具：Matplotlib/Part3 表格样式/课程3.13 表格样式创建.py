# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:56:34 2019

@author: lindsay.hu
"""

'''
【课程3.13】  表格样式创建

表格视觉样式：Dataframe.style → 返回pandas.Styler对象的属性，具有格式化和显示Dataframe的有用方法

样式创建：
① Styler.applymap：elementwise → 按元素方式处理Dataframe
② Styler.apply：column- / row- / table-wise → 按行/列处理Dataframe
 
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline #jupyter 运行

##以下代码需要在交互式下才可以使用

# 样式

df = pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
sty = df.style
print(sty,type(sty))
# 查看样式类型

sty
# 显示样式

# 按元素处理样式：style.applymap()

def color_neg_red(val):
    if val < 0:
        color = 'red'
    else:
        color = 'black'
    return('color:%s' % color)
df.style.applymap(color_neg_red)
# 创建样式方法，使得小于0的数变成红色
# style.applymap() → 自动调用其中的函数

# 按行/列处理样式：style.apply()

def highlight_max(s):
    is_max = s == s.max()
    #print(is_max)
    lst = []
    for v in is_max:
        if v:
            lst.append('background-color: yellow')
        else:
            lst.append('')
    return(lst)
df.style.apply(highlight_max, axis = 0, subset = ['b','c'])
# 创建样式方法，每列最大值填充黄色
# axis：0为列，1为行，默认为0
# subset：索引

# 样式索引、切片

df.style.apply(highlight_max, axis = 1, 
               subset = pd.IndexSlice[2:5,['b', 'd']])
# 通过pd.IndexSlice[]调用切片
# 也可：df[2:5].style.apply(highlight_max, subset = ['b', 'd']) → 先索引行再做样式

