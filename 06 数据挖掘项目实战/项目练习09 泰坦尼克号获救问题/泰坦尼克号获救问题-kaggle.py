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
os.chdir('E:\\learning\\program\\pycode\\Titanic\\')
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = [train_df,test_df]

'''
【描述性数据分析】

'''

'''
研究数据本身
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
train_df.describe() #default，结果包含所有数值型的列
#Total samples are 891 or 40% of the actual number of passengers on board the Titanic (2,224).
#Survived是一个分类变量，0：死亡，1：生存
#Around 38% samples survived representative of the actual survival rate at 32%.
#样本存活率约38%，实际存活率为32%。
#Most passengers (> 75%) did not travel with parents or children
#Nearly 30% of the passengers had siblings and/or spouse aboard
#Fares varied significantly with few passengers (<1%) paying as high as $512.
#年龄在65-80岁之间的老年乘客很少(<1%)

train_df.describe(include=['O']) #include=['O'])，结果包含所有分类列
#Names are unique across the dataset (count=unique=891)
#Sex variable as two possible values with 65% male (top=male, freq=577/count=891).
#Cabin values have several dupicates across samples. Alternatively several passengers shared a cabin.
#Embarked takes three possible values. S port used by most passengers (top=S)
#Ticket feature has high ratio (22%) of duplicate values (unique=681)

'''
研究数据之间的关系
'''
#通过数据透视表分析
train_df[['Pclass','Survived']].groupby(['Pclass'],as_index=False).mean().sort_values(by='Survived',ascending=False)
train_df[['Sex','Survived']].groupby(['Sex'],as_index=False).mean().sort_values(by='Survived',ascending=False)
train_df[['SibSp','Survived']].groupby(['SibSp'],as_index=False).mean().sort_values(by='Survived',ascending=False)
train_df[['Parch','Survived']].groupby(['Parch'],as_index=False).mean().sort_values(by='Survived',ascending=False)

#通过可视化图表分析

#关联数值特征
#1.Age与Survived的关系
g = sns.FacetGrid(train_df,col='Survived')
g.map(plt.hist,'Age',bins=20)

#2.Pclass与Survived的关系
grid = sns.FacetGrid(train_df,col='Survived',row='Pclass',size=2.2,aspect=1.6)
grid.map(plt.hist,'Age',alpha=0.5,bins=20)
grid.add_legend()

#关联分类特征
#3.Embarked与Survived的关系
grid= sns.FacetGrid(train_df,row='Embarked',size=2.2,aspect=1.6)
grid.map(sns.pointplot,'Pclass','Survived','Sex',palette='deep')
grid.add_legend()

#同时关联分类和数值特征
grid = sns.FacetGrid(train_df,row='Embarked',col='Survived',size=2.2,aspect=1.6)
grid.map(sns.barplot,'Sex','Fare',alpha=0.5,ci=None)
grid.add_legend()


#特征工程
#删除没有用的特征
print("Before",train_df.shape,test_df.shape,combine[0].shape,combine[1].shape)

train_df = train_df.drop(['Ticket','Cabin'],axis=1)
test_df = test_df.drop(['Ticket','Cabin'],axis=1)
combine = [train_df,test_df]

print("Before",train_df.shape,test_df.shape,combine[0].shape,combine[1].shape)

#从现有的特征中构造新的特征
#1.从Name中提取新特征
for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)
pd.crosstab(train_df['Title'],train_df['Sex'])

for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady','Countess','Capt','Col','Don',
           'Dr','Major','Rev','Sir','Jonkheer','Dona'],'Rare')
    
    dataset['Title'] = dataset['Title'].replace('Mlle','Miss')
    dataset['Title'] = dataset['Title'].replace('Ms','Miss')
    dataset['Title'] = dataset['Title'].replace('Mme','Mrs')
    
train_df[['Title','Survived']].groupby(['Title'],as_index=False).mean()

title_mapping = {'Mr':1,'Miss':2,'Mrs':3,'Master':4,'Rare':5}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)
train_df.head()

train_df = train_df.drop(['Name','PassengerId'],axis=1)
test_df = test_df.drop(['Name'],axis=1)
combine = [train_df,test_df]
train_df.shape,test_df.shape

#转换分类特征
for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map({'female':1,'male':0}).astype(int)
train_df.head()

#连续型数值特征缺失值补充
grid = sns.FacetGrid(train_df,row='Pclass',col='Sex',size=2.2,aspect=1.6)
grid.map(plt.hist,'Age',alpha=0.5,bins=20)
grid.add_legend()

#1.根据Pclass x Gender猜测年龄
guess_ages = np.zeros((2,3))
guess_ages

for dataset in combine:
    for i in range(0,2):
        for j in range(0,3):
            guess_df = dataset[(dataset['Sex'] == i)&
                               (dataset['Pclass'] == j+1)]['Age'].dropna()
            age_guess = guess_df.median()
            #随机转换年龄在0.5岁附近
            guess_ages[i,j] = int(age_guess/0.5 + 0.5)*0.5

    for i in range(0,2):
        for j in range(0,3):
            dataset.loc[(dataset.Age.isnull()) & (dataset.Sex == i)
                        & (dataset.Pclass == j+1),'Age'] = guess_ages[i,j]
    dataset['Age'] = dataset['Age'].astype(int)

train_df.head()
    
train_df['AgeBand'] = pd.cut(train_df['Age'],5)
train_df[['AgeBand','Survived']].groupby(['AgeBand'],as_index=False
        ).mean().sort_values(by='AgeBand')

for dataset in combine:
    dataset.loc[dataset['Age'] <= 16,'Age'] = 0
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 32),'Age'] = 1
    dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48),'Age'] = 2
    dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64),'Age'] = 3
    dataset.loc[(dataset['Age'] > 64),'Age'] 

train_df.head()

train_df = train_df.drop(['AgeBand'],axis=1)
combine = [train_df,test_df]
train_df.head()

#结合现有的某些特征构造新的特征
for dataset in combine:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

train_df[['FamilySize','Survived']].groupby(['FamilySize'],
        as_index=False).mean().sort_values(by='Survived',ascending=False)

for dataset in combine:
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1,'IsAlone'] = 1

train_df[['IsAlone','Survived']].groupby(['IsAlone'],as_index=False).mean()

train_df = train_df.drop(['Parch','SibSp','FamilySize'],axis=1)
test_df = test_df.drop(['Parch','SibSp','FamilySize'],axis=1)
combine = [train_df,test_df]

train_df.head()

for dataset in combine:
    dataset['Age*Class'] = dataset.Age * dataset.Pclass

train_df.loc[:,['Age*Class','Age','Pclass']].head(10)

#完善补充分类特征的缺失值
freq_port = train_df.Embarked.dropna().mode()[0]
freq_port

for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].fillna(freq_port)

train_df[['Embarked','Survived']].groupby(['Embarked'],as_index=False).mean().sort_values(by='Survived',ascending=False)

for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].map({'S':0,'C':1,'Q':2}).astype(int)
train_df.head()

#快速完善补充数值特征的缺失值
test_df['Fare'].fillna(test_df['Fare'].dropna().median(),inplace=True)
test_df.head()

train_df['FareBand'] = pd.qcut(train_df['Fare'],4)
train_df[['FareBand','Survived']].groupby(['FareBand'],as_index=False).mean().sort_values(by='FareBand',ascending=True)

for dataset in combine:
    dataset.loc[dataset['Fare'] <= 7.91,'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 7.9) & (dataset['Fare'] <= 14.454),'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31),'Fare'] = 2
    dataset.loc[dataset['Fare'] > 31,'Fare'] = 3
    dataset['Fare'] = dataset['Fare'].astype(int)

train_df =train_df.drop(['FareBand'],axis=1)
combine = [train_df,test_df]

train_df.head(10)
    
test_df.head(10)    

'''建模、预测、解决问题'''

    