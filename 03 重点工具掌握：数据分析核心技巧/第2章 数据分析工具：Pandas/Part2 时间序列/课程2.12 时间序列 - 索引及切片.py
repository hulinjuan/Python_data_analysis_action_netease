# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:10:07 2019

@author: lindsay.hu
"""

'''
【课程2.12】  时间序列-索引及切片

TimeSeries是Series的一个子类，所以Series索引及数据选取方面的方法基本一样

同时TimeSeries通过时间序列有更便捷的方法做索引和切片

'''

import numpy as np
import pandas as pd
from datetime import datetime

#索引
rng = pd.date_range('2017/1','2017/3')
ts = pd.Series(np.random.rand(len(rng)), index = rng)
print(ts.head())
#基本下标索引
print(ts[0])
print(ts[:2])
print('------')
# 时间序列标签索引，支持各种时间字符串，以及datetime.datetime
# 时间序列由于按照时间先后排序，故不用考虑顺序问题
# 索引方法同样适用于Dataframe
print(ts['20170102'])
print(ts.loc['20170102'])
print(ts['2017-1-2'])
print(ts['1/2/2017'])
print(ts[datetime(2017,1,2)])

#切片
print(ts.head())
print(ts[::2])
# 和Series按照index索引原理一样，也是末端包含
print(ts['20170101':'20170109'])
print(ts.loc['20170101':'20170109'])
print('--------')
print(ts['2017/1']) #传入月直接得到一个切片
print(ts['2017-1'])
print(ts['2017/1'][::2])

# 重复索引的时间序列

dates = pd.DatetimeIndex(['1/1/2015','1/2/2015','1/3/2015','1/4/2015','1/1/2015','1/2/2015'])
ts = pd.Series(np.random.rand(6), index = dates)
print(ts)
# index有重复，is_unique检查 → values唯一，index不唯一
print(ts.is_unique,ts.index.is_unique)
print('-----')
# index有重复的将返回多个值
print(ts['20150101'],type(ts['20150101']))
print(ts['20150104'],type(ts['20150104']))
print('-----')

# 通过groupby做分组，重复的值这里用平均值处理
print(ts.groupby(level = 0).mean())

