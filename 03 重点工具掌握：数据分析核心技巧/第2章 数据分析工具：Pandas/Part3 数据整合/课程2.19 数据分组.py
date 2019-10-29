# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:44:39 2019

@author: lindsay.hu
"""

'''
【课程2.19】  数据分组

分组统计 - groupby功能

① 根据某些条件将数据拆分成组
② 对每个组独立应用函数
③ 将结果合并到一个数据结构中

Dataframe在行（axis=0）或列（axis=1）上进行分组，将一个函数应用到各个分组并产生一个新值，然后函数执行结果被合并到最终的结果对象中。

df.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs)
 
'''

import numpy as np
import pandas as pd

# 分组
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print(df)
print('------')
# 直接分组得到一个groupby对象，是一个中间数据，没有进行计算
print(df.groupby('A'),type(df.groupby('A')))

# 通过分组后的计算，得到一个新的dataframe
# 默认axis = 0，以行来分组
# 可单个或多个（[]）列分组
print(df.groupby('A').sum())
a = df.groupby('A').mean()
b = df.groupby(['A','B']).mean()
c = df.groupby(['A'])['D'].mean()  # 以A分组，算D的平均值
print(a,type(a),'\n',a.columns)
print(b,type(b),'\n',b.columns)
print(c,type(c))

# 分组 - 可迭代对象
df = pd.DataFrame({'X' : ['A', 'B', 'A', 'B'], 'Y' : [1, 4, 3, 2]})
print(df)
print(df.groupby('X'), type(df.groupby('X')))
print('-----')

print(list(df.groupby('X')), '→ 可迭代对象，直接生成list\n')
print(list(df.groupby('X'))[0], '→ 以元祖形式显示\n')
# n是组名，g是分组后的Dataframe
for n,g in df.groupby('X'):
    print(n)
    print(g)
    print('###')
# .get_group()提取分组后的组        
print(df.groupby(['X']).get_group('A'),'\n')
print(df.groupby(['X']).get_group('B'),'\n')
print('-----')

# .groups：将分组后的groups转为dict
# 可以字典索引方法来查看groups里的元素
grouped = df.groupby(['X'])
print(grouped.groups)
print(grouped.groups['A'])  # 也可写：df.groupby('X').groups['A']
print('-----')
# .size()：查看分组后的长度
sz = grouped.size()
print(sz,type(sz))
print('-----')
#按照两个列进行分组
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
grouped = df.groupby(['A','B']).groups
print(df)
print(grouped)
print(grouped[('foo','three')])

# 其他轴上的分组

df = pd.DataFrame({'data1':np.random.rand(2),
                  'data2':np.random.rand(2),
                  'key1':['a','b'],
                  'key2':['one','two']})
print(df)
print(df.dtypes)
print('-----')
# 按照值类型分列
for n,p in df.groupby(df.dtypes, axis=1):
    print(n)
    print(p)
    print('##')


# 通过字典或者Series分组

df = pd.DataFrame(np.arange(16).reshape(4,4),
                  columns = ['a','b','c','d'])
print(df)
print('-----')   
# mapping中，a、b列对应的为one，c、d列对应的为two，以字典来分组
mapping = {'a':'one','b':'one','c':'two','d':'two','e':'three'}
by_column = df.groupby(mapping,axis = 1)
print(by_column.sum())
# s中，index中a、b对应的为one，c、d对应的为two，以Series来分组
s = pd.Series(mapping)
print(s,'\n')
print(s.groupby(s).count())

# 通过函数分组

df = pd.DataFrame(np.arange(16).reshape(4,4),
                  columns = ['a','b','c','d'],
                 index = ['abc','bcd','aa','b'])
print(df,'\n')
print(df.groupby(len).sum())
# 按照字母长度分组

# 分组计算函数方法

s = pd.Series([1, 2, 3, 10, 20, 30], index = [1, 2, 3, 1, 2, 3])
grouped = s.groupby(level=0)  # 唯一索引用.groupby(level=0)，将同一个index的分为一组
print(grouped)
print(grouped.first(),'→ first：非NaN的第一个值\n')
print(grouped.last(),'→ last：非NaN的最后一个值\n')
print(grouped.sum(),'→ sum：非NaN的和\n')
print(grouped.mean(),'→ mean：非NaN的平均值\n')
print(grouped.median(),'→ median：非NaN的算术中位数\n')
print(grouped.count(),'→ count：非NaN的值\n')
print(grouped.min(),'→ min、max：非NaN的最小值、最大值\n')
print(grouped.std(),'→ std，var：非NaN的标准差和方差\n')
print(grouped.prod(),'→ prod：非NaN的积\n')

# 多函数计算：agg()

df = pd.DataFrame({'a':[1,1,2,2],
                  'b':np.random.rand(4),
                  'c':np.random.rand(4),
                  'd':np.random.rand(4),})
print(df)
print(df.groupby('a').agg(['mean',np.sum]))
print(df.groupby('a')['b'].agg({'result1':np.mean,
                               'result2':np.sum}))
# 函数写法可以用str，或者np.方法
# 可以通过list，dict传入，当用dict时，key名为columns
    
