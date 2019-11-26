# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:25:15 2019

@author: lindsay.hu
"""

'''
【课程1.2】 分布分析

分布分析 -> 研究数据的分布特征和分布类型，分定量数据，定性数据区分统计量

极差/频率分布情况/分组组距及组数
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#文件名中含有中文，如果直接用read_csv读取，会报错OSError: Initializing from file failed
f = open('C:\\Users\\lindsay.hu\\Desktop\\py\\pynet\\深圳罗湖二手房信息.csv')
data = pd.read_csv(f)
data.head()

plt.scatter(data['经度'],data['纬度'],
            s = data['房屋单价']/500,
            c = data['参考总价'],cmap='Reds',
            alpha = 0.4)
plt.grid()

#极差
def d_range(df,*cols):
    krange = []
    for col in cols:
        crange = df[col].max()-df[col].min()
        krange.append(crange)
    return(krange)

key1 = '参考总价'
key2 = '参考首付'

dr = d_range(data,key1,key2)
print('%s极差为：%.f \n%s极差为：%f'% (key1,dr[0],key2,dr[1]))

#频率分布情况

data[key1].hist(bins=8)
#频率分布情况,分组区间
gcut = pd.cut(data[key1],10,right=False)
gcut_count = gcut.value_counts(sort=False)
gcut_count
data['%s分组区间' %key1] = gcut.values
data.head()
#区间出现的频率
r_zj = pd.DataFrame(gcut_count)
r_zj.rename(columns = {gcut_count.name:'频数'},inplace = True)
r_zj['频率'] = r_zj['频数']/r_zj['频数'].sum()
r_zj['累计频率'] = r_zj['频率'].cumsum()
r_zj['频率%'] = r_zj['频率'].apply(lambda x:'%.2f%%' % (x*100))
r_zj['累计频率%'] = r_zj['累计频率'].apply(lambda x:'%.2f%%' % (x*100))
r_zj.style.bar(subset=['频率','累计频率']) #在jupyter Notebook中执行
#类似于excel条件格式中的数据条

#直方图
r_zj['频率'].plot(kind='bar',
            figsize=(12,2),
            grid=True,
            color='k',
            alpha=0.4)
x = len(r_zj)
y = r_zj['频率']
m = r_zj['频数']
for i,j,k in zip(range(x),y,m):
    plt.text(i-0.1,j+0.01,'%i' % k, color='k')
#添加数据标签

#频率分布，定性字段
    
cx_g = data['朝向'].value_counts(sort=True)
cx_g

r_zj = pd.DataFrame(cx_g)
r_zj.rename(columns = {cx_g.name:'频数'},inplace = True)
r_zj['频率'] = r_zj['频数']/r_zj['频数'].sum()
r_zj['累计频率'] = r_zj['频率'].cumsum()
r_zj['频率%'] = r_zj['频率'].apply(lambda x:'%.2f%%' % (x*100))
r_zj['累计频率%'] = r_zj['累计频率'].apply(lambda x:'%.2f%%' % (x*100))
r_zj.style.bar(subset=['频率','累计频率'],color='#51eaea',width=100) #在jupyter Notebook中执行
#类似于excel条件格式中的数据条
#直方图
r_zj['频率'].plot(kind='bar',
            figsize=(12,2),
            grid=True,
            color='k',
            alpha=0.4)
x = len(r_zj)
y = r_zj['频率']
m = r_zj['频数']
for i,j,k in zip(range(x),y,m):
    plt.text(i-0.1,j+0.01,'%i' % k, color='k')
    
plt.pie(r_zj['频数'],
        labels=r_zj.index,
        autopct='%.2f%%',
        shadow=True)
plt.axis('equal')
#绘制饼图

