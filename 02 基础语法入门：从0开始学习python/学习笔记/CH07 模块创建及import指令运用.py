# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:57:57 2019

@author: lindsay.hu
"""
'''
python概念层级

1.表达式 -> 创建/处理对象
2.语句 —> 包含表达式
3.逻辑单元 —> 函数或类，有语句组成
4.模块 —> .py代码文件组成模块
5.包 —> 定义一组有关系的文件，或者模块
（包是文件夹，模块是其中的文件，且文件夹中包括一个__init__.py文件)
6.程序 —> 若干个包+若干个文件
'''

'''导入自己创建的模块testmodel2，模块的.py文件该存放在哪'''
#查看现有包所在的路径，将自己创建的包存入该路径
import  pandas
print(pandas.__file__)
#import testmodel2
#添加一个路径，比如把桌面添加过去
import sys
sys.path.append('C:\\Users\\lindsay.hu\\Desktop\\')
import testmodel1

#调用testmodel2
testmodel1.f1()
testmodel1.f2(2,3)

'''创建一个模块，包含一个阶乘函数f1(n),一个列表删值函数,一个等差数列求和函数'''
##创建模块testmodel2,包括以下3个函数
#创建阶乘函数f1
def f1(n):
    y  = 1
    for i in range(1,n+1):
        y =y * i
    return y

#创建列表删值函数f2
def f2(lst,x):
    while x in lst:
        lst.remove(x)
    return lst

#创建等差数列求和函数
def f3(a,d,n):
    an = a
    s = 0
    for i in range(n-1):
        an =an + d
        s = s + an
    return s

##模块路径问题
#查看现有包所在的路径，将自己创建的包存入该路径
import  pandas
print(pandas.__file__)

import testmodel2
print(testmodel2.f1(10))
print(testmodel2.f2([1,2,3,3,3,3,3,4,5,6,7,7,7],3))
print(testmodel2.f3(10,5,5))

#import .. as ..
import testmodel2 as tm

print(tm.f1(10))
print(tm.f2([1,2,3,3,3,3,3,4,5,6,7,7,7],3))
print(tm.f3(10,5,5))

#调用部分模块语句: from..import..
from testmodel2 import f3
f3(10,5,5)
f1(10) #报错

#python标准模块 --random随机数
import random
x =random.random()
y =random.random()
print(x,y*100)

m = random.randint(0,100)
print(m)

#有序类型，按索引取
lst = list(range(20))
s = random.choice(lst)
print(s)

sli =random.sample(lst,5)
print(sli)

random.shuffle(lst)
print(lst)

#python标准模块 --time

#time.sleep()
import time
for i in range(5):
    print('hello')
    time.sleep(0.1)

#将当前的时间打印为1个字符串
print(time.ctime())
print(type(time.ctime()))

#将当前时间转化为当前时区的struct_time
#wday 0-6表示周日到周六
#yday 1-366表示1年中的第几天
#isdst 是否为夏令时，默认为-1
print(time.localtime())
print(type(time.localtime()))

#time.strftime(a,b)
#a为格式化字符串格式
#b为时间戳，一般用localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

