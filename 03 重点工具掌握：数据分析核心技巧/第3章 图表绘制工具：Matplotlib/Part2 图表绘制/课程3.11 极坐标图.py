# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:38:31 2019

@author: lindsay.hu
"""

'''
【课程3.11】  极坐标图

调用subplot()创建子图时通过设置projection='polar',便可创建一个极坐标子图，然后调用plot()在极坐标子图中绘图
 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(np.arange(20))
theta=np.arange(0,2*np.pi,0.02)
print(s.head())
print(theta[:10])
# 创建数据

fig = plt.figure(figsize=(8,4))
ax1 = plt.subplot(121,projection = 'polar')
ax2 = plt.subplot(122)
# 创建极坐标子图
# 还可以写：ax = fig.add_subplot(111,polar=True)

ax1.plot(theta,theta*3,linestyle = '--',lw=1)
ax1.plot(s,linestyle='--',marker='.',lw=2)
ax2.plot(theta,theta*3,linestyle = '--',lw=1)
ax2.plot(s)
plt.grid()
# 创建极坐标图，参数1为角度（弧度制），参数2为value
# lw → 线宽

#极坐标参数设置
theta=np.arange(0,2*np.pi,0.02)
plt.figure(figsize=(8,4))
ax1= plt.subplot(121, projection='polar')
ax2= plt.subplot(122, projection='polar')
ax1.plot(theta,theta/6,'--',lw=2)
ax2.plot(theta,theta/6,'--',lw=2)
# 创建极坐标子图ax
ax2.set_theta_direction(-1)
# set_theta_direction()：坐标轴正方向，默认逆时针

ax2.set_thetagrids(np.arange(0.0, 360.0, 90),['a','b','c','d'])
ax2.set_rgrids(np.arange(0.2,2,0.4))
# set_thetagrids()：设置极坐标角度网格线显示及标签 → 网格和标签数量一致
# set_rgrids()：设置极径网格线显示，其中参数必须是正数

ax2.set_theta_offset(np.pi/2)
# set_theta_offset()：设置角度偏移，逆时针，弧度制

ax2.set_rlim(0.2,1.2)
ax2.set_rmax(2)
ax2.set_rticks(np.arange(0.1, 1.5, 0.2))
# set_rlim()：设置显示的极径范围
# set_rmax()：设置显示的极径最大值
# set_rticks()：设置极径网格线的显示范围

# 雷达图1 - 极坐标的折线图/填图 - plt.plot()

plt.figure(figsize=(8,4))

ax1= plt.subplot(111, projection='polar')
ax1.set_title('radar map\n')  # 创建标题
ax1.set_rlim(0,12)

data1 = np.random.randint(1,10,10)
data2 = np.random.randint(1,10,10)
data3 = np.random.randint(1,10,10)
theta=np.arange(0,2*np.pi,2*np.pi/10)
# 创建数据

ax1.plot(theta,data1,'.--',label='data1')
ax1.fill(theta,data1,alpha=0.2)
ax1.plot(theta,data2,'.--',label='data2')
ax1.fill(theta,data2,alpha=0.2)
ax1.plot(theta,data3,'.--',label='data3')
ax1.fill(theta,data3,alpha=0.2)
# 绘制雷达线

# 雷达图2 - 极坐标的折线图/填图 - plt.polar()
# 首尾闭合

labels = np.array(['a','b','c','d','e','f']) # 标签
dataLenth = 6 # 数据长度
data1 = np.random.randint(0,10,6) 
data2 = np.random.randint(0,10,6) # 数据

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False) # 分割圆周长
data1 = np.concatenate((data1, [data1[0]])) # 闭合
data2 = np.concatenate((data2, [data2[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

plt.polar(angles, data1, 'o-', linewidth=1) #做极坐标系
plt.fill(angles, data1, alpha=0.25)# 填充
plt.polar(angles, data2, 'o-', linewidth=1) #做极坐标系
plt.fill(angles, data2, alpha=0.25)# 填充

plt.thetagrids(angles * 180/np.pi, labels) # 设置网格、标签
plt.ylim(0,10)  # polar的极值设置为ylim

# 极轴图 - 极坐标的柱状图

plt.figure(figsize=(8,4))

ax1= plt.subplot(111, projection='polar')
ax1.set_title('radar map\n')  # 创建标题
ax1.set_rlim(0,12)

data = np.random.randint(1,10,10)
theta=np.arange(0,2*np.pi,2*np.pi/10)
# 创建数据

bar = ax1.bar(theta,data,alpha=0.5)
for r,bar in zip(data, bar):
    bar.set_facecolor(plt.cm.jet(r/10.))  # 设置颜色
plt.thetagrids(np.arange(0.0, 360.0, 90), []) # 设置网格、标签（这里是空标签，则不显示内容）

