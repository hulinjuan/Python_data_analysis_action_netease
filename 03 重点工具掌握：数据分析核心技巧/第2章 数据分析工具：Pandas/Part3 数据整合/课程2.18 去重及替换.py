# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:19:14 2019

@author: lindsay.hu
"""

'''
【课程2.18】  去重及替换

.duplicated / .replace
 
'''
import numpy as np
import pandas as pd

# 去重 .duplicated

s = pd.Series([1,1,1,1,2,2,2,3,4,5,5,5,5])
# 判断是否重复
# 通过布尔判断，得到不重复的值
print(s.duplicated()) #生成布尔值
print(s[s.duplicated()==False]) #保留第一个值，非重复的

# drop.duplicates移除重复
# inplace参数：是否替换原值，默认False
s_re = s.drop_duplicates()
print(s_re)

# Dataframe中使用duplicated
df = pd.DataFrame({'key1':['a','a',3,4,5],
                  'key2':['a','a','b','b','c']})
print(df.duplicated())
print(df['key2'].duplicated())

# 替换 .replace
# 可一次性替换一个值或多个值
# 可传入列表或字典
s = pd.Series(list('ascaazsd'))
print(s.replace('a',np.nan))
print(s.replace(['a','s'] ,np.nan))
print(s.replace({'a':'hello world!','s':123}))


