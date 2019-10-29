# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:41:58 2019

@author: lindsay.hu
"""

'''
【课程2.20】  分组转换及一般性“拆分-应用-合并”

transform / apply
 
'''

import numpy as np
import pandas as pd

# 数据分组转换,transform

df = pd.DataFrame({'data1':np.random.rand(5),
                  'data2':np.random.rand(5),
                  'key1':list('aabba'),
                  'key2':['one','two','one','two','one']})
k_mean = df.groupby('key1').mean()
print(df)
print(k_mean)
# 通过分组、合并，得到一个包含均值的Dataframe
print(pd.merge(df,k_mean,left_on = 'key1',right_index=True).add_prefix('mean_'))
print('-----')
# data1、data2每个位置元素取对应分组列的均值
# 字符串不能进行计算
print(df.groupby('key2').mean())# 按照key2分组求均值
print(df.groupby('key2').transform(np.mean))

# 一般化Groupby方法：apply

df = pd.DataFrame({'data1':np.random.rand(5),
                  'data2':np.random.rand(5),
                  'key1':list('aabba'),
                  'key2':['one','two','one','two','one']})
print(df)
# apply直接运行其中的函数
# 这里为匿名函数，直接描述分组后的统计量
print(df.groupby('key1').apply(lambda x:x.describe()))

# f_df1函数：返回排序后的前n行数据
def f_df1(d,n):
    return(d.sort_index()[:n])
# f_df2函数：返回分组后表的k1列，结果为Series，层次化索引    
def f_df2(d,k1):
    return(d[k1])
    
print(df.groupby('key1').apply(f_df1,2),'\n')
print(df.groupby('key1').apply(f_df2,'data2'))
print(type(df.groupby('key1').apply(f_df2,'data2')))
# 直接运行f_df函数
# 参数直接写在后面，也可以为.apply(f_df,n = 2))
