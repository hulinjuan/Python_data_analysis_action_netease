# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:57:00 2019

@author: lindsay.hu
"""

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

'''
1.整体来看，存活比例如何？
要求：
① 读取已知生存数据train.csv
② 查看已知存活数据中，存活比例如何？
提示：
① 注意过程中筛选掉缺失值之后再分析
② 这里用seaborn制图辅助研究
'''
os.chdir('C:\\Users\\lindsay.hu\\Desktop\\py\\pynet\\Titanic\\')
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

sns.set_style('ticks')
plt.axis('equal')
train_data['Survived'].value_counts().plot.pie(autopct = '%.2f%%')
#print('存活比例为38.38%')

'''
2、结合性别和年龄数据，分析幸存下来的人是哪些人？
要求：
① 年龄数据的分布情况
② 男性和女性存活情况
③ 老人和小孩存活情况
'''
#年龄数据的分布情况
sns.set()
sns.set_style('ticks')

#剔除年龄缺失的数据
train_data_age = train_data[train_data['Age'].notnull()]
plt.figure(figsize = (12,5))
plt.subplot(121)
train_data_age['Age'].hist(bins = 80)
plt.xlabel('Age')
plt.ylabel('Num')

plt.subplot(122)
train_data_age.boxplot(column = 'Age',showfliers = False)

train_data_age['Age'].describe()
#print('总体年龄分布: 去掉缺失值后样本有714，平均年龄约为30岁，标准差14岁，最小年龄0.42，最大年龄80.')

#男性和女性存活情况
train_data[['Sex','Survived']].groupby('Sex').mean().plot.bar()
survive_sex = train_data.groupby(['Sex','Survived'])['Survived'].count()
print('女性存活率%.2f%%,男性存活率%.2f%%' %
      (survive_sex.loc['female',1]/survive_sex.loc['female'].sum()*100,
       survive_sex.loc['male',1]/survive_sex.loc['male'].sum()*100))

#年龄与存活关系
fix,ax = plt.subplots(1,2,figsize = (18,8))

sns.violinplot('Pclass','Age',hue='Survived',data = train_data_age,split=True,ax = ax[0])      
ax[0].set_title('Pclass and Age vs Survived')
#ax[0].set_yticks(range(0,110,10))
#print('按照不同船舱等级划分 → 船舱等级越高，存活者年龄越大，船舱等级1存活年龄集中在20-40岁，船舱等级2/3中有较多低龄乘客存活')

sns.violinplot("Sex","Age",hue="Survived",data=train_data_age,split=True,ax=ax[1])
ax[1].set_title('Sex and Age vs Survived')
#ax[1].set_yticks(range(0,110,10))
#print('按照性别划分 → 男性女性存活者年龄主要分布在20-40岁，且均有较多低龄乘客，其中女性存活更多')

#老人和小孩存活情况
plt.figure(figsize = (18,4))
train_data_age['Age_int'] = train_data_age['Age'].astype(np.int)
average_age = train_data_age[['Age_int','Survived']].groupby('Age_int',as_index = False).mean()
sns.barplot(x = 'Age_int',y = 'Survived',data = train_data_age,palette = 'BuPu')
plt.grid(linestyle = '--',alpha = 0.5) 
#print('灾难中，老人和小孩存活率较高')

'''
3、结合 SibSp、Parch字段，研究亲人多少与存活的关系
要求：
① 有无兄弟姐妹/父母子女和存活与否的关系
② 亲戚多少与存活与否的关系
'''
#筛选有无兄弟姐妹
sibsp_df = train_data[train_data['SibSp'] != 0] 
no_sibsp_df = train_data[train_data['SibSp'] == 0]

#筛选有无父母子女
parch_df = train_data[train_data['Parch'] != 0] 
no_parch_df = train_data[train_data['Parch'] == 0]

plt.figure(figsize = (12,3))
plt.subplot(141)
plt.axis('equal')
sibsp_df['Survived'].value_counts().plot.pie(labels = ['No Survived','Survived'],
        autopct = '%.1f%%',colormap = 'summer')

plt.subplot(142)
plt.axis('equal')
no_sibsp_df['Survived'].value_counts().plot.pie(labels = ['No Survived','Survived'],
        autopct = '%.1f%%',colormap = 'summer')

plt.subplot(143)
plt.axis('equal')
parch_df['Survived'].value_counts().plot.pie(labels = ['No Survived','Survived'],
        autopct = '%.1f%%',colormap = 'summer')

plt.subplot(144)
plt.axis('equal')
no_parch_df['Survived'].value_counts().plot.pie(labels = ['No Survived','Survived'],
        autopct = '%.1f%%',colormap = 'summer')
#print('有兄弟姐妹、父母子女的乘客存活率更大')

#亲戚多少与存活与否的关系
fig,ax = plt.subplots(1,2,figsize = (15,4))
train_data[['Parch','Survived']].groupby('Parch').mean().plot.bar(ax=ax[0])
train_data[['SibSp','Survived']].groupby('SibSp').mean().plot.bar(ax=ax[1])

train_data['family_size'] = train_data['Parch'] + train_data['SibSp'] + 1
train_data[['family_size','Survived']].groupby('family_size').mean().plot.bar(figsize = (15,4))
#print('若独自一人，那么其存活率比较低；但是如果亲友太多的话，存活率也会很低')

'''
4、结合票的费用情况，研究票价和存活与否的关系
要求：
① 票价分布和存活与否的关系
② 比较研究生还者和未生还者的票价情况
'''
#票价分布和存活与否的关系
fig,ax = plt.subplots(1,2,figsize = (15,4))
train_data['Fare'].hist(bins = 70,ax = ax[0])
train_data.boxplot(column = 'Fare',by = 'Pclass',showfliers = False,ax=ax[1])

fare_not_survived = train_data['Fare'][train_data['Survived'] == 0]
fare_survived = train_data['Fare'][train_data['Survived'] == 1]

#筛选数据
average_fare = pd.DataFrame([fare_not_survived.mean(),fare_survived.mean()])
std_fare = pd.DataFrame([fare_not_survived.std(),fare_survived.std()])
average_fare.plot(yerr = std_fare,kind = 'bar',figsize = (15,4),grid = True)
#print('生还者的平均票价要大于未生还者的平均票价')

'''
5、利用KNN分类模型，对结果进行预测
要求：
① 模型训练字段：'Survived','Pclass','Sex','Age','Fare','Family_Size'
② 模型预测test.csv样本数据的生还率
提示：
① 训练数据集中，性别改为数字表示 → 1代表男性，0代表女性
'''
'''
# 数据清洗，提取训练字段
knn_train = train_data[['Survived','Pclass','Sex','Age','Fare','family_size']].dropna()
knn_train['Sex'][train_data['Sex'] == 'male'] = 1
knn_train['Sex'][train_data['Sex'] == 'female'] = 0

test_data['family_size'] = test_data['Parch'] + test_data['SibSp'] + 1
knn_test = test_data[['Pclass','Sex','Age','Fare','family_size']].dropna()
knn_test['Sex'][test_data['Sex'] == 'male'] = 1
knn_test['Sex'][test_data['Sex'] == 'female'] = 0

from sklearn import neighbors

knn = neighbors.KNeighborsClassifier()
knn.fit(knn_train[['Pclass','Sex','Age','Fare','family_size']],knn_train['Survived'])

knn_test['predict'] = knn.predict(knn_test)
pre_survived = knn_test[knn_test['predict'] == 1].reset_index()
del pre_survived['index']

'''

###############################################################
#建模预测，输出结果


knn_train = train_data[['PassengerId','Survived','Pclass','Sex','Fare','family_size']].dropna()
knn_train['Sex'][train_data['Sex'] == 'male'] = 1
knn_train['Sex'][train_data['Sex'] == 'female'] = 0

x_train =  knn_train[['Pclass','Sex','Fare','family_size']]
y_train = knn_train['Survived']

#不丢失passengerid
test_data['family_size'] = test_data['Parch'] + test_data['SibSp'] + 1
knn_test = test_data[['PassengerId','Pclass','Sex','Fare','family_size']]
knn_test['Sex'][test_data['Sex'] == 'male'] = 1
knn_test['Sex'][test_data['Sex'] == 'female'] = 0
knn_test['Fare'].fillna(0,inplace=True)

x_test = knn_test[['Pclass','Sex','Fare','family_size']]


from sklearn import neighbors

knn = neighbors.KNeighborsClassifier()
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)
#accuracy评估
print(round(100*knn.score(x_train,y_train)),2)

out_put = pd.DataFrame({'PassengerId': knn_test.PassengerId, 'Survived':  y_pred})

out_put.to_csv('my_submission.csv', index=False)
print("Your submission was successfully saved!")