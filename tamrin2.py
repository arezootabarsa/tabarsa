import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
df = pd.read_csv("C:/Users/TBS/Desktop/survey lung cancer.csv")
plt.style.use('fivethirtyeight')
from sklearn.preprocessing import LabelEncoder
# colors=['#011f4b','#03396c','#005b96','#6497b1','#b3cde0']
# sns.set_palette(sns.color_palette(colors))
# pd.set_option('display.max_columns', None)
# # print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# gender = df['GENDER'].value_counts()
# print(gender.values)
# print(gender.index)
# con_col = ['AGE']
# cat_col=[]
# for i in df.columns:
#     if i!='AGE':
#         cat_col.append(i)
# fig,ax = plt.subplots(1,3,figsize=(20,6))
# sns.histplot(df['AGE'],ax=ax[0])
# sns.histplot(data =df,x='AGE',ax=ax[1],hue='LUNG_CANCER',kde=True)
# sns.boxplot(x=df['LUNG_CANCER'],y=df['AGE'],ax=ax[2])
# plt.suptitle("Visualizing AGE column",size=20)
# plt.show()
# fig,ax = plt.subplots(15,3,figsize=(30,90))
# for index,i in enumerate(cat_col):
#     sns.boxplot(x=df[i],y=df['AGE'],ax=ax[index,0])
#     sns.boxplot(x=df[i],y=df['AGE'],ax=ax[index,1],hue=df['LUNG_CANCER'])
#     sns.violinplot(x=df[i],y=df['AGE'],ax=ax[index,2])
# fig.tight_layout()
# fig.subplots_adjust(top=0.95)
# plt.suptitle("Visualizing AGE vs Categorical Columns",fontsize=50)
# plt.savefig('plot3')

encoder = LabelEncoder()
df['LUNG_CANCER']=encoder.fit_transform(df['LUNG_CANCER'])
df['GENDER']=encoder.fit_transform(df['GENDER'])
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(),annot=True,linewidth=0.5,fmt='0.2f')
plt.savefig('plot4')
