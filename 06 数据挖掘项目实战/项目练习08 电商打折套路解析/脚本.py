import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from bokeh.plotting import figure,show,output_file
from bokeh.models import ColumnDataSource

'''
（1）导入数据
'''
#工作路径
import os 
os.chdir('C:\\Users\\lindsay.hu\\Desktop\\项目08电商打折套路解析')

#加载数据，提取销售日期
df = pd.read_excel('双十一淘宝美妆数据.xlsx',sheetname = 0)
df.fillna(0,inplace=True)
df.index = df['update_time']
df['date'] = df.index.day

'''
（2）双11当天在售的商品占比情况
'''
data1 = df['id','title','店名','date']


print('finished!')