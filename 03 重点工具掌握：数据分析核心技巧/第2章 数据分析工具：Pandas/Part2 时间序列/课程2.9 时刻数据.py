# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:25:45 2019

@author: lindsay.hu
"""

'''
【课程2.9】 pandas 时刻数据：Timestamp

时刻数据代表时间点，是pandas的数据类型，
是将值与时间点相关联的最基本类型的时间序列数据
pandas.Timestamp()

'''
import numpy as np
import pandas as pd
import datetime

#pd.Timestamp()
date1 = '20170101'
date2 = datetime.datetime(2016,10,1,15,0)
date3 = '2017-01-01 12:0:0'
t1 = pd.Timestamp(date1)
t2 = pd.Timestamp(date2)
t3 = pd.Timestamp(date3)
print(t1,type(1))
print(t2,type(2))
print(date2,type(date2))
print(t3,type(t3))

#pd.to_datetime
date2 = datetime.datetime(2016,10,1,15,0)
date1 = '2017-01-01 12:0:0'
t1 = pd.to_datetime(date1)
t2 = pd.to_datetime(date2)
print(t1,type(1))
print(t2,type(2))
#多个时间啊数据将会转换为时间戳索引DatetimeIndex
lst_date = ['2019-12-21','2019-12-22','2019-12-23']
t3 = pd.to_datetime(lst_date)
print(t3,type(t3))

date3 = ['2019-12-21','2019-12-22','hahaha','2019-12-23']
print(pd.to_datetime(date3,errors='ignore'))
print(pd.to_datetime(date3,errors='coerce'))
