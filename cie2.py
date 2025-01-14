# -*- coding: utf-8 -*-
"""cie2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QqpS-WgP5bUPNJxOoWBEXUNZm3xH41HQ
"""

import pandas as pd
data=pd.read_csv("titanic.csv")
data

data.info()

data.shape

data.duplicated()

data.head(10)

data.isnull().sum()

data.describe()

data['Pclass'].unique()

data.dtypes

import matplotlib.pyplot as plt
data['Survived']=data['Survived'].replace({1:'survived',0:'not survived'})
group_data=data.groupby(['Survived','Pclass'])['PassengerId'].count().unstack()
group_data.plot(kind='bar',figsize=(10,6))
plt.title("Survivel by counts in bar chart")
plt.xlabel("Survivel")
plt.ylabel("counts")
plt.xticks(ticks=(0,1),label=['Not Survived','survived'],rotation=0)
plt.legend(title='Pclass')
plt.show()

null_val=data['Age'].isnull().sum()
filled_data=data['Age'].fillna(data['Age'].mean(numeric_only=True))
null_val,filled_data.head(20)

import numpy as np
mean=np.mean(data['Age'])
std=np.std(data['Age'])
print("Mean is=",mean)
print("Standard deviation is=",std)

threshold=3
outlier=[]
for i in data['Age']:
  z=(i-mean)/std
  if z > threshold:
    outlier.append(i)
print("Outlier is=",outlier)

import seaborn as sns
sns.boxplot(data['Age'])