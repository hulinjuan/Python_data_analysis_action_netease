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
              kind = 'scatter' #设置类型："scatter","reg","resid","kde","hex"
              )