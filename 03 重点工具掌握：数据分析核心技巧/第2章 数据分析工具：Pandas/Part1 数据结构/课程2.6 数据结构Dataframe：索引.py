# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:57:53 2019

@author: lindsay.hu
"""


'''
【课程2.5】 数据结构Dataframe：索引

DataFrame：既有行索引，又有列索引，可以被看做由Series组成的字典（共用一个索引）

选择列/选择行/切片/布尔判断

'''

import numpy as np
import pandas as pd

###选择行与列
df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                  index = ['one','two','three'],
                  columns = ['a','b','c','d'])
print(df)
#df[]选择列
#一般用于选择列df[col]，[]中写列名，也可以选择行
#按照列名进行选择， 只选择一列输出Series,选择多列输出DataFrame
data1 = df['a'] #选a列
data2 = df[['b','c']] #选择b列和c列
print(data1,type(data1))
print(data2,type(data2))
#df[]中为数字时，默认选择行，且只能进行切片的选择，不能单独选择（df[0]）
#输出结果为DataFrame，即便只选择一行
#df[]不能通过索引标签名来选择行（df['one'])
data3 = df[:2]
print(data3)

#df.loc[label]选择行,主要针对index选择行，同时支持指定index,及默认数字index
#按照index选择行，只选择一行输出Series,选择多行输出DataFrame
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
print(df1)
print(df2)
print('------')
 #单个索引标签，返回Series
data1 = df1.loc['three'] 
print(data1,type(data1))
#多个索引标签,顺序可变,如果索引不存在，则返回NaN
data2 = df2.loc[[3,2,1]] 
data3 = df1.loc[['three','four','five']]
print(data2)
print(data3)
#可以做切片对象，末端包含
data5 = df1.loc['one':'three']
data6 = df2.loc[1:3]
print(data5)
print(data6)
print('切片索引')

#df.iloc[] ——按照整数位置（从轴的0到length-1）选择行
#类似list的索引，其顺序就是dataframe的整数位置，从0开始
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
#单位置索引，和loc索引不同，不能索引超出数据行数的整数位置
print(df.iloc[0])
print(df.iloc[-1])
#print(df.iloc[4]) #报错，不可以超出行数
print('单位置索引\n-------')
#多位置索引，顺序可变
print(df.iloc[[0,2]])
print(df.iloc[[3,2,1]])
print('多位置索引\n-------')
#切片索引，末端不包含
print(df.iloc[1:3])
print(df.iloc[::2])
print('切片索引\n-------')

#布尔型索引
#和Series原理相同
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
print('-----')
#不做索引会对每个值进行判断
#索引保留所有数据：True返回原数据，False返回值为NaN
b1 = df < 20
print(b1,type(b1))
print(df[b1]) #也可以写为df[df<20]
print('-------')
#单列做判断
#索引结果保留 单列判断为True的行数据，包括其他列
b2 = df['a'] > 50
print(b2,type(b2))
print(df[b2]) #也可以写为df[df['a']>50]
print('-------')
#多列做判断
#索引结果保留所有数据：True返回原数据，False返回NaN
b3 = df[['a','b']] > 50
print(b3,type(b3))
print(df[b3]) #也可以写为df[df['a']>50]
print('-------')
#多行做判断
#索引结果保留所有数据：True返回数据，False返回值为NaN
b4 = df.loc[['one','three']] < 50
print(b4,type(b4))
print(df[b4]) #也可以写为df[df['a']>50]
print('-------')

#多重索引：比如同时索引行和列
#先选择列再选择行——相当于对于一个数据，先筛选字段，再选择数据量
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
print('------')
print(df['a'].loc[['three','four']])
print('------')
print(df[['b','c','d']].iloc[::2])
print('------')
print(df[df<50].loc[['one','two']])