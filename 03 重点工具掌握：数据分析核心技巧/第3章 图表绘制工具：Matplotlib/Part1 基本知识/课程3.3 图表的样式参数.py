# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:43:02 2019

@author: lindsay.hu
"""

'''
【课程3.3】  图表的样式参数

linestyle、style、color、marker
 
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#不打印警告信息
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#linestyle参数

plt.plot([i**2 for i in range(100)],linestyle = '-.')
# '-'       solid line style
# '--'      dashed line style
# '-.'      dash-dot line style
# ':'       dotted line style

# marker参数

s = pd.Series(np.random.randn(100).cumsum())
s.plot(linestyle='--',marker='2')
# '.'       point marker
# ','       pixel marker
# 'o'       circle marker
# 'v'       triangle_down marker
# '^'       triangle_up marker
# '<'       triangle_left marker
# '>'       triangle_right marker
# '1'       tri_down marker
# '2'       tri_up marker
# '3'       tri_left marker
# '4'       tri_right marker
# 's'       square marker
# 'p'       pentagon marker
# '*'       star marker
# 'h'       hexagon1 marker
# 'H'       hexagon2 marker
# '+'       plus marker
# 'x'       x marker
# 'D'       diamond marker
# 'd'       thin_diamond marker
# '|'       vline marker
# '_'       hline marker

# color参数

plt.hist(np.random.randn(100),color='g',alpha=0.8)
plt.hist(np.random.randn(100),color='#FFBBB4',alpha=0.8)#也可以自己找颜色参数
# alpha：0-1，透明度
# 常用颜色简写：red-r, green-g, black-k, blue-b, yellow-y

         
df = pd.DataFrame(np.random.randn(1000, 4),columns=list('ABCD'))
df = df.cumsum()
df.plot(style='--',alpha=0.8,colormap='GnBu')
# colormap：颜色板，包括：
# Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r,
# Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, 
# PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, 
# RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, 
# YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, 
# cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r,
# gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, 
# gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, 
# nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, 
# spectral_r ,spring, spring_r, summer, summer_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r

# 其他参数见“颜色参数.docx”

# style参数，可以包含linestyle，marker，color

ts = pd.Series(np.random.randn(1000).cumsum(), index=pd.date_range('1/1/2000', periods=1000))
ts.plot(style='--g.',grid=True)
# style → 风格字符串，这里包括了linestyle（-），marker（.），color（g）
# plot()内也有grid参数

#整体风格样式

import matplotlib.style as  psl
#查看样式表
print(plt.style.available)

# 一旦选用样式后，所有图表都会有样式，重启后才能关掉
psl.use('ggplot')

ts = pd.Series(np.random.randn(1000).cumsum(), index=pd.date_range('1/1/2000', periods=1000))
ts.plot(style = '--g.',grid = True,figsize=(10,6))


