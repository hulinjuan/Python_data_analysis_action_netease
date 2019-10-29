# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:34:18 2019

@author: lindsay.hu
"""

'''
【课程2.22】  数据读取

核心：read_table, read_csv, read_excel
 
'''
import numpy as np
import pandas as pd

# 读取普通分隔数据：read_table
# 可以读取txt，csv
import os
os.chdir('C:\\Users\\lindsay.hu\\Desktop\\')

data1 = pd.read_table('data1.txt', delimiter=',',header = 0, index_col=1)
print(data1)
# delimiter：用于拆分的字符，也可以用sep：sep = ','
# header：用做列名的序号，默认为0（第一行）
# index_col：指定某列为行索引，否则自动索引0, 1, .....

# read_table主要用于读取简单的数据，txt/csv

# 读取csv数据：read_csv
# 先熟悉一下excel怎么导出csv

data2 = pd.read_csv('data2.csv',engine = 'python')
print(data2.head())
# engine：使用的分析引擎。可以选择C或者是python。C引擎快但是Python引擎功能更加完备。
# encoding：指定字符集类型，即编码，通常指定为'utf-8'

# 大多数情况先将excel导出csv，再读取

# 读取excel数据：read_excel

data3 = pd.read_excel('地市级党委书记数据库（2000-10）.xlsx',sheetname='中国人民共和国地市级党委书记数据库（2000-10）',header=0)
print(data3)
# io ：文件路径。
# sheetname：返回多表使用sheetname=[0,1],若sheetname=None是返回全表 → ① int/string 返回的是dataframe ②而none和list返回的是dict
# header：指定列名行，默认0，即取第一行
# index_col：指定列为索引列，也可以使用u”strings”
