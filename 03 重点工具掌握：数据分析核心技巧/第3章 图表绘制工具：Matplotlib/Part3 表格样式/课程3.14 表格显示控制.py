# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:13:01 2019

@author: lindsay.hu
"""

'''
【课程3.14】  表格显示控制

df.style.format()
 
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline #jupyter 运行

##以下代码需要在交互式下才可以使用
# 按照百分数显示

df = pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
print(df.head())
df.head().style.format("{:.2%}") 

# 显示小数点数

df.head().style.format("{:.4f}")

# 显示正负数

df.head().style.format("{:+.2f}")

# 分列显示

df.head().style.format({'b':"{:.2%}", 'c':"{:+.3f}", 'd':"{:.3f}"})