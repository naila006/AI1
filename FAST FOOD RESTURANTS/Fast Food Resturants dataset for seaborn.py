# seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("FastFoodResturants.csv", delimiter=',' )
df = df.reset_index(drop=True)
df.fillna(0, inplace=True)
print(df)

#print datatypes
print("dtype", df.dtypes)

#print data info
print("df.info", df.info())

#print statics operations
print("statics operations", df.describe())

#printing no of rows and coloumns
print("no of rows and coloumns", df.shape)

#line graph
sns.set_theme(style='darkgrid')
sns.lineplot(x='city', y='latitude', data=df)
plt.show()

#categorial graph
sns.set_theme(style='whitegrid')
sns.catplot(x='city',y='latitude',data=df)
plt.show()

#kernel graph
sns.set_theme(style='ticks')
sns.kdeplot(x='postalCode', y='latitude', data=df)
plt.show()

#scatter graph
sns.set_theme(style='dark')
sns.scatterplot(x='city', y='latitude', data=df)
plt.show()

#bar graph
sns.set_theme(style='white')
sns.barplot(x='city', y='latitude', data=df)
plt.show()

#line plot
sns.set_theme(style='white')
sns.lineplot(x='city', y='longitude', data=df)
plt.show()

#categorial plot
sns.set_theme(style='dark')
sns.catplot(x='city', y='longitude', data=df)
plt.show()

#kernel plot
sns.set_theme(style='darkgrid')
sns.kdeplot(x='latitude', y='longitude', data=df)
plt.show()

#scstter plot
sns.set_theme(style='ticks')
sns.scatterplot(x='city', y='longitude', data=df)
plt.show()

#bar plot
sns.set_theme(style='white')
sns.barplot(x='city', y='longitude', data=df)
plt.show()