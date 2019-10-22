# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:21:42 2019

@author: lindsay.hu
"""


'''
【课程2.9】 pandas时间戳索引：DatetimeIndex

核心：pd.date_range()

'''
import numpy as np
import pandas as pd
import datetime

#pd.DatetimeIndex()与TimeSeries()时间序列
rng = pd.DatetimeIndex(['12/1/2017','12/2/2017','12/3/2017','12/4/2017','12/5/2017'])
print(rng,type(rng))
print(rng[0],type(rng[0]))
#以DatetimeIndex为index的Series为TimeSeries
st = pd.Series(np.random.rand(5),index =rng )
print(st,type(st))
print(st.index)

#pd.date_range(start=None,end=None,periods=None,freq='D',nomalize=False,name=None,closed=None,**kwargs) 
#日期范围，：生成日期范围
#2种生成方式：（1）start+end;（2）start/end +periods
#start:开始时间
#end：结束时间
#periods：偏移量
#freq:频率，默认频率为日历日：day，pd.bdate_range()默认频率为工作日
#tz:时区
#normalize = True的话把时间归到凌晨0点
rng1 = pd.date_range('1/1/2017','1/10/2017',normalize=True)
rng2 = pd.date_range(start = '1/1/2017',periods=10)
rng3 = pd.date_range(end = '1/30/2017 15:00:00',periods=10) #增加了时、分、秒
print(rng1,type(rng1))
print(rng2,type(rng2))
print(rng3,type(rng3))
#normalize ：时间参数值正则化到午夜时间戳（这里直接变成0:00:00，并不是15:30:00）
#name 索引对象名称
rng4 = pd.date_range(start = '1/1/2017 15:30:00',periods=10,name='hello world!',normalize=True)
print(rng4)

print(pd.date_range('20170101','20170104'))#左闭右闭
print(pd.date_range('20170101','20170104',closed='right')) #左开右闭
print(pd.date_range('20170101','20170104',closed='left')) #左闭右开

print(pd.bdate_range('20170101','20170107'))#工作日
 
#pd.date_range() - 日期范围：频率（1）
print(pd.date_range('20170101','20170104')) #默认freq = 'D':每日历日
print(pd.date_range('20170101','20170104',freq = 'B')) #B：每工作日
print(pd.date_range('20170101','20170102',freq = 'H')) #H：每小时
print(pd.date_range('2017/1/1 12:00','2017/1/1 12:10',freq = 'T')) #T/MIN：每分
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10',freq = 'S')) #S：每秒
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10',freq = 'L')) #S：每毫秒
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10',freq = 'U')) #S：每微秒
# W-MON：从指定星期几开始算起，每周
# 星期几缩写：MON/TUE/WED/THU/FRI/SAT/SUN
print(pd.date_range('2017/1/1','2017/2/1', freq = 'W-MON'))  
# WOM-2MON：每月的第几个星期几开始算，这里是每月第二个星期一
print(pd.date_range('2017/1/1','2017/5/1', freq = 'WOM-2MON'))  

# pd.date_range()-日期范围：频率(2)

# M：每月最后一个日历日
# Q-月：指定月为季度末，每个季度末最后一月的最后一个日历日
# A-月：每年指定月份的最后一个日历日
# 月缩写：JAN/FEB/MAR/APR/MAY/JUN/JUL/AUG/SEP/OCT/NOV/DEC
# 所以Q-月只有三种情况：1-4-7-10,2-5-8-11,3-6-9-12
print(pd.date_range('2017','2018', freq = 'M'))  
print(pd.date_range('2017','2020', freq = 'Q-DEC'))  
print(pd.date_range('2017','2020', freq = 'A-DEC')) 
print('------')

# BM：每月最后一个工作日
# BQ-月：指定月为季度末，每个季度末最后一月的最后一个工作日
# BA-月：每年指定月份的最后一个工作日
print(pd.date_range('2017','2018', freq = 'BM'))  
print(pd.date_range('2017','2020', freq = 'BQ-DEC'))  
print(pd.date_range('2017','2020', freq = 'BA-DEC')) 
print('------')

# M：每月第一个日历日
# Q-月：指定月为季度末，每个季度末最后一月的第一个日历日
# A-月：每年指定月份的第一个日历日
print(pd.date_range('2017','2018', freq = 'MS'))  
print(pd.date_range('2017','2020', freq = 'QS-DEC'))  
print(pd.date_range('2017','2020', freq = 'AS-DEC')) 
print('------')

# BM：每月第一个工作日
# BQ-月：指定月为季度末，每个季度末最后一月的第一个工作日
# BA-月：每年指定月份的第一个工作日
print(pd.date_range('2017','2018', freq = 'BMS'))  
print(pd.date_range('2017','2020', freq = 'BQS-DEC'))  
print(pd.date_range('2017','2020', freq = 'BAS-DEC')) 
print('------')

# pd.date_range()-日期范围：复合频率

print(pd.date_range('2017/1/1','2017/2/1', freq = '7D'))  # 7天
print(pd.date_range('2017/1/1','2017/1/2', freq = '2h30min'))  # 2小时30分钟
print(pd.date_range('2017','2018', freq = '2M'))  # 2月，每月最后一个日历日

# asfreq：时期频率转换
# 改变频率，这里是D改为4H
# method：插值模式，None不插值，ffill用之前值填充，bfill用之后值填充
ts = pd.Series(np.random.rand(4),
              index = pd.date_range('20170101','20170104'))
print(ts)
print(ts.asfreq('4H',method = 'ffill'))

# pd.date_range()-日期范围：超前/滞后数据

ts = pd.Series(np.random.rand(4),
              index = pd.date_range('20170101','20170104'))
print(ts)
# 正数：数值后移（滞后）；负数：数值前移（超前）
print(ts.shift(2))
print(ts.shift(-2))
print('------')

# 计算变化百分比，这里计算：该时间戳与上一个时间戳相比，变化百分比
per = ts/ts.shift(1) - 1
print(per)
print('------')
# 加上freq参数：对时间戳进行位移，而不是对数值进行位移
print(ts.shift(2, freq = 'D'))
print(ts.shift(2, freq = 'T'))


