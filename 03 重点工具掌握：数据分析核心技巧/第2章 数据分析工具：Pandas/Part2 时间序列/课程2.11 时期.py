# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:16:20 2019

@author: lindsay.hu
"""

'''
【课程2.11】  Pandas时期：Period

核心：pd.Period()

'''

import numpy as np
import pandas as pd
import datetime

# pd.Period()创建时期
# 生成一个以2017-01开始，月为频率的时间构造器
# pd.Period()参数：一个时间戳 + freq 参数 → freq 用于指明该 period 的长度，时间戳则说明该 period 在时间轴上的位置
p = pd.Period('2017', freq = 'M')
t = pd.DatetimeIndex(['2017-1-1'])
print(p, type(p))
print(t, type(t))

# 通过加减整数，将周期整体移动
# 这里是按照 月、年 移动
print(p + 1)
print(p - 2)
print(pd.Period('2012', freq = 'A-DEC') - 1)

#pd.period_range()创建时期范围
#数据格式为PeriodIndex,单个数值为Period
prng = pd.period_range('1/1/2011','1/1/2012',freq='M')
rng = pd.date_range('1/1/2011','1/1/2012',freq='M')
print(prng,type(prng))
print(rng,type(rng))
print(prng[0],type(prng[0]))

ts1 = pd.Series(np.random.rand(len(prng)),index=prng)
ts2 = pd.Series(np.random.rand(len(rng)),index=rng)
print(ts1)
print(ts2)

#asfreq：频率转换
#通过.asfreq(freq,method=None,how=None)方法转换成别的频率
p = pd.Period('2017','A-DEC')
print(p)
print(p.asfreq('M',how='start')) #也可写how='s'
print(p.asfreq('D',how='end')) #也可写how='e'
#asfreq也可以转换TIMESeries的index
prng = pd.period_range('2017','2018',freq='M')
ts1 = pd.Series(np.random.rand(len(prng)),index=prng)
ts2 = pd.Series(np.random.rand(len(prng)),index=prng.asfreq('D',how='start'))
print(ts1.head(),len(ts1))
print(ts2.head(),len(ts2))

#时间戳与时期之间的转换：pd.to_period()、pd.to_timestamp()
rng = pd.date_range('2017/1/1',periods=10,freq='M')
prng = pd.period_range('2017','2018',freq='M')

#每月最后一日，转化为每月
ts1 = pd.Series(np.random.rand(len(rng)),index=rng)
print(ts1.head())
print(ts1.to_period().head())

#每月，转化为每月第一天
ts2 = pd.Series(np.random.rand(len(prng)),index=prng)
print(ts2.head())
print(ts2.to_timestamp().head())



