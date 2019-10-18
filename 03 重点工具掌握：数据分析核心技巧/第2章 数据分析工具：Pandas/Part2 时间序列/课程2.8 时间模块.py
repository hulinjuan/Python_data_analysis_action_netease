# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:07:26 2019

@author: lindsay.hu
"""

'''
【课程2.8】 时间模块

datetime模块，主演datetime.date(),datetime.datetime(),datetime.timedelta()
日期解析方法：parser.parse

'''
import numpy as np
import pandas as pd
import datetime

#datetime.date:date对象
#datetime.date.today 返回今日
#输出格式为date类
today = datetime.date.today()
print(today,type(today))
print(str(today))
date = datetime.date(2015,10,1)
print(date,type(date))

#datetime.datetime()
now = datetime.datetime.now()
print(now,type(now))
t1 = datetime.datetime(2016,6,1)
t2 = datetime.datetime(2016,6,1,15,30,25)
print(t2-t1,type(t2-t1))

#datetime.timedelta 时间差
t1 = datetime.datetime(2000,10,1)
tx = datetime.timedelta(100) #100天
ty = datetime.timedelta(100,3600) #100天,3600秒
print(t1 + tx)
print(t1 - tx)

#字符串转换方法 parser.parse
#各种格式可以解析，但无法支持中文
from dateutil.parser import parse
date ='12-21-2017'
date2 ='21/12/2017'
print(parse(date),type(parse(date)))
print(parse(date2),type(parse(date2)))
print(parse('5/1/2014',dayfirst=True)) #国际通用格式中，日在月之前。可以通过dayfirst来设置
