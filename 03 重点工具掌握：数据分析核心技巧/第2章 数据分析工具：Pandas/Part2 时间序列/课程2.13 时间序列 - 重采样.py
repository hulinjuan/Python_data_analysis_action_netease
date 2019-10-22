# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:27:54 2019

@author: lindsay.hu
"""

'''
【课程2.13】  时间序列 - 重采样

将时间序列从一个频率转换为另一个频率的过程，且会有数据的结合

降采样：高频数据 → 低频数据，eg.以天为频率的数据转为以月为频率的数据
升采样：低频数据 → 高频数据，eg.以年为频率的数据转为以月为频率的数据
 
'''
import numpy as np
import pandas as pd
from datetime import datetime

#重采样：.resample()
#创建一个以天为频率的TimeSeries，重采样为按2天为频率
rng = pd.date_range('20170101', periods = 12)
ts = pd.Series(np.arange(12), index = rng)
print(ts)

#freq：重采样频率 ->ts.resample('5D')
#.sum()：聚合方法
ts_re = ts.resample('5D') #得到一个重采样构建器，频率改为5天
ts_re2 = ts.resample('5D').sum() #得到一个新的聚合后的Series，聚合方式为求和
print(ts_re,type(ts_re))
print(ts_re2,type(ts_re2))
print('-------')

print(ts.resample('5D').mean(),'→ 求平均值\n')
print(ts.resample('5D').max(),'→ 求最大值\n')
print(ts.resample('5D').min(),'→ 求最小值\n')
print(ts.resample('5D').median(),'→ 求中值\n')
print(ts.resample('5D').first(),'→ 返回第一个值\n')
print(ts.resample('5D').last(),'→ 返回最后一个值\n')
print(ts.resample('5D').ohlc(),'→ OHLC重采样\n')
# OHLC:金融领域的时间序列聚合方式 → open开盘、high最大值、low最小值、close收盘

#降采样
rng = pd.date_range('20170101', periods = 12)
ts = pd.Series(np.arange(1,13), index = rng)
print(ts)

print(ts.resample('5D').sum(),'→ 默认\n')
print(ts.resample('5D', closed = 'left').sum(),'→ left\n')
print(ts.resample('5D', closed = 'right').sum(),'→ right\n')
print('-----')
# closed：各时间段哪一端是闭合（即包含）的，默认 左闭右闭
# 详解：这里values为0-11，按照5D重采样 → [1,2,3,4,5],[6,7,8,9,10],[11,12]
# left指定间隔左边为结束 → [1,2,3,4,5],[6,7,8,9,10],[11,12]
# right指定间隔右边为结束 → [1],[2,3,4,5,6],[7,8,9,10,11],[12]

print(ts.resample('5D', label = 'left').sum(),'→ leftlabel\n')
print(ts.resample('5D', label = 'right').sum(),'→ rightlabel\n')
# label：聚合值的index，默认为取左
# 值采样认为默认（这里closed默认）

# 升采样及插值
rng = pd.date_range('2017/1/1 0:0:0', periods = 5, freq = 'H')
ts = pd.DataFrame(np.arange(15).reshape(5,3),
                  index = rng,
                  columns = ['a','b','c'])
print(ts)

print(ts.resample('15T').asfreq())
print(ts.resample('15T').ffill())
print(ts.resample('15T').bfill())
# 低频转高频，主要是如何插值
# .asfreq()：不做填充，返回Nan
# .ffill()：向上填充
# .bfill()：向下填充

# 时期重采样 - Period

prng = pd.period_range('2016','2017',freq = 'M')
ts = pd.Series(np.arange(len(prng)), index = prng)
print(ts)

print(ts.resample('Q-DEC').sum())  # 降采样 
print(ts.resample('15D').ffill())  # 升采样