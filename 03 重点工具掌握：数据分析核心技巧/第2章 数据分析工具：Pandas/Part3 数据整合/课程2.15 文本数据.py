# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:50:29 2019

@author: lindsay.hu
"""

'''
【课程2.15】  文本数据

Pandas针对字符串配备的一套方法，使其易于对数组的每个元素进行操作
 
'''

import numpy as np
import pandas as pd
from datetime import datetime

# 通过str访问，且自动排除丢失/ NA值
s = pd.Series(['A','b','C','bbhello','123',np.nan,'hj'])
df = pd.DataFrame({'key1':list('abcdef'),
                  'key2':['hee','fv','w','hija','123',np.nan]})
print(s)
print(df)
print('-----')
# 直接通过.str调用字符串方法
# 可以对Series、Dataframe使用
# 自动过滤NaN值
print(s.str.count('b'))
print(df['key2'].str.upper())
print('-----')

# df.columns是一个Index对象，也可使用.str
df.columns = df.columns.str.upper() #把列名转换成大写，key1,key2
print(df)

# 字符串常用方法（1） - lower，upper，len，startswith，endswith
s = pd.Series(['A','b','bbhello','123',np.nan])

print(s.str.lower(),'→ lower小写\n')
print(s.str.upper(),'→ upper大写\n')
print(s.str.len(),'→ len字符长度\n')
print(s.str.startswith('b'),'→ 判断起始是否为a\n')
print(s.str.endswith('3'),'→ 判断结束是否为3\n')

# 字符串常用方法（2） - strip
s = pd.Series([' jack', 'jill ', ' jesse ', 'frank'])
df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '],
                  index=range(3))
print(s)
print(df)
print('-----')

# 这里去掉了columns的前后空格，但没有去掉中间空格
print(s.str.strip())  # 去除字符串中的空格
print(s.str.lstrip().values)  # 去除字符串中的左空格,.vlaues可以明显看到左边的空格是否去除
print(s.str.rstrip())  # 去除字符串中的右空格

df.columns = df.columns.str.strip()
print(df)

# 字符串常用方法（3） - replace
df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '],
                  index=range(3))
df.columns = df.columns.str.replace(' ','-') #只对列名中的空格做替换
print(df)
# 替换

df.columns = df.columns.str.replace('-','hehe',n=1)
print(df)
# n：替换个数

# 字符串常用方法（4） - split、rsplit
# 类似字符串的split,只用于字符串不用于列表，所以['a,,,c']不能被分列

s = pd.Series(['a,b,c','1,2,3',['a,,,c'],np.nan])
print(s.str.split(','))
print('-----')

# 直接索引得到一个list
print(s.str.split(',')[0]) #是一个Series
print('-----')

# 可以使用get或[]符号访问拆分列表中的元素
print(s.str.split(',').str[0])
print(s.str.split(',').str.get(1))
print('-----')

# 可以使用expand可以轻松扩展此操作以返回DataFrame
# n参数限制分割数
# rsplit类似于split，反向工作，即从字符串的末尾到字符串的开头
print(s.str.split(',', expand=True))
print(s.str.split(',', expand=True, n = 1))
print(s.str.rsplit(',', expand=True, n = 1))
print('-----')

df = pd.DataFrame({'key1':['a,b,c','1,2,3',[':,., ']],
                  'key2':['a-b-c','1-2-3',[':-.- ']]})
print(df['key2'].str.split('-')) #先选中列，得到一个Series,再分列
# Dataframe使用split

# 字符串索引
s = pd.Series(['A','b','C','bbhello','123',np.nan,'hj'])
df = pd.DataFrame({'key1':list('abcdef'),
                  'key2':['hee','fv','w','hija','123',np.nan]})

print(s.str[0])  # 取第一个字符串,选择一列中的第一个字符
print(s.str[:2])  # 取前两个字符串,选择一列中的前一个字符
print(df['key2'].str[0]) 
# str之后和字符串本身索引方式相同
