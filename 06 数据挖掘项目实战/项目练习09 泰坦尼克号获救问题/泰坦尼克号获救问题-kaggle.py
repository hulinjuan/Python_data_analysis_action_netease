# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:43:32 2019

@author: lindsay.hu
"""
'''https://www.kaggle.com/startupsci/titanic-data-science-s'''

#数据整理与分析
import numpy as np
import pandas as pd
import random as rnd

#可视化
import matplotlib.pyplot as plt
import seaborn as sns

import os
import time

#不发出警告
import warnings
warnings.filterwarnings('ignore')

## machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

#获取数据
os.chdir('C:\\Users\\lindsay.hu\\Desktop\\py\\pynet\\Titanic\\')
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = [train_df,test_df]

'''
【描述性数据分析】

'''

#数据集中有哪些可用的特征？
print(train_df.columns.values)

#特征（变量）的类型，和是否包含缺失值。可以帮助我们选择合适的可视化图表：

 #分类变量（标称，有序，比率，区间）
 #Categorical: Survived, Sex, and Embarked. Ordinal: Pclass.

 #数值型变量（连续、离散，基于时间序列的）
 #Continous: Age, Fare. Discrete: SibSp, Parch
 
 #混合数据类型的
 #Ticket：数字，数字字母混合. Cabin :数字字母
 
 #那些特征包含错误或拼写错误（大数据集难检查，小数据集可以，这些特征可能需要更正）
  
#预览数据
train_df.head()
train_df.tail()

train_df.info()
print('-'*40)
test_df.info()
train_df.describe()

