# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:37:03 2019

@author: lindsay.hu
"""


'''
【课程2.5】 数据结构Dataframe：基本概念及创建
"二维数组"DataFrame：是一个表格型的数据结构，包含一组有序的列，
其他列的值类型可以是数值、字符串、布尔值等。

DataFrame中的数据以一个或多个二维快存放，不是列表，字典或一维数据结构。

'''

import numpy as np
import pandas as pd

#DataFrame数据结构
#DataFrame是一个表格型数据结构，“带有标签的二维数组”
#DataFrame带有index（行标签）和columns（列标签）

data = {'name':['Jack','Tom','Mary'],
        'age':[18,19,20],
        'gender':['m','m','w']}

frame = pd.DataFrame(data)
print(frame)
print(type(frame))
#.index查看行标签
#.columns查看列标签
#.values查看值，数据类型为ndarray
print(frame.index,'\n该数据类型为：',type(frame.index))
print(frame.columns,'\n该数据类型为：',type(frame.columns))
print(frame.values,'\n该数据类型为：',type(frame.values))

#DataFrame 创建方法一：由数组/list组成的字典
#创建方法：pandas.DataFrame()
#由数组/list组成的字典创建DataFrame，columns为字典key，index为默认数据标签
#字典的值的长度必须保持一致！
data1 = {'a':[1,2,3],
         'b':[3,4,5],
         'c':[5,6,7],     
        }
data2 = {'one':np.random.rand(3),
         'two':np.random.rand(3)
        }
print(data1)
print(data2)
d1 = pd.DataFrame(data1)
d2 = pd.DataFrame(data2)
print(d1)
print(d2)
#index参数：重新定义index，格式为list,长度必须保持一致
#columns参数：可重新指定列的顺序，格式为list，如果现有数据中没有该列，则产生NaN值
#如果columns重新指定时候，列的数量可以少于原数据
d3 = pd.DataFrame(data1,index=['f1','f2','f3'])
print(d3)
d4 = pd.DataFrame(data1,columns=['a','b','c','d'])#多一列
print(d4)
d5 = pd.DataFrame(data1,columns=['b','c'])#少一列
print(d5)

#DataFrame 创建方法二：由Series组成的字典
#由Series组成的字典创建DataFrame,columns为字典key，index为Series的标签（如果Series没有指定标签，则是默认的数字标签）
#Series可以长度不一样，生成的DataFrame会出现NaN值
data1 = {'one':pd.Series(np.random.rand(2)),
         'two':pd.Series(np.random.rand(3))
        } #没有设置index的Series
data2 = {'one':pd.Series(np.random.rand(2),index=['a','b']),
         'two':pd.Series(np.random.rand(3),index=['a','b','c'])
        }
print(data1)
print(data2)
d1 = pd.DataFrame(data1)
d2 = pd.DataFrame(data2)
print(d1)
print(d2)

#DataFrame 创建方法三：通过二维数组直接创建
#得到一样形状的结果数据，如果不指定index和columns，两者均返回默认数字格式
#index和columns指定长度与原数组保持一致
ar = np.random.rand(9).reshape(3,3)
print(ar)
df1 = pd.DataFrame(ar)
df2 = pd.DataFrame(ar,index = ['a','b','c'],
                   columns = ['one','two','three'])
print(df1)
print(df2)
 
#DataFrame 创建方法四：由字典组成的列表，每一个字典就是一行
#columns为字典的key,index不做指定则为默认数组标签
#columns和index参数分别重新指定相应列及标签
data = [{'one':1,'two':2},{'one':5,'two':10,'three':20}]
print(data)
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data,index=['a','b'])
df3 = pd.DataFrame(data,columns=['one','two'])
print(df1)
print(df2)
print(df3)

#DataFrame 创建方法五：由字典组成的字典（嵌套字典）
#columns为字典的key,index为子字典的key
#columns可以增加或减少现有列
#index在这里和之前不同，并不能改变原有index，如果指向新的标签，值为NaN(非常重要)
data = {'Jack':{'math':90,'english':89,'art':78},
        'Marry':{'math':82,'english':95,'art':92},
        'Tom':{'math':78,'english':67}
        }
df1 = pd.DataFrame(data)
print(df1)

df2 = pd.DataFrame(data,columns = ['Jack','Tom','Bob'])
df3 = pd.DataFrame(data,index = pd.Series(['a','b','c']))
print(df2)
print(df3)

