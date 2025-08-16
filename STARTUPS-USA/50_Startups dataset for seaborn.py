#seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("50_Startups.csv", delimiter=',' )
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
sns.lineplot(x='R&D_Spend', y='Administration', data=df)
plt.show()

#categorial graph
sns.set_theme(style='whitegrid')
sns.catplot(x='R&D_Spend',y='Administration',data=df)
plt.show()

#kernel graph
sns.set_theme(style='ticks')
sns.kdeplot(x='R&D_Spend', y='Administration', data=df)
plt.show()

#scatter graph
sns.set_theme(style='dark')
sns.scatterplot(x='R&D_Spend', y='Administration', data=df)
plt.show()

#bar graph
sns.set_theme(style='white')
sns.barplot(x='State', y='Profit', data=df)
plt.show()

#line plot
sns.set_theme(style='white')
sns.lineplot(x='State', y='Profit', data=df)
plt.show()

#categorial plot
sns.set_theme(style='dark')
sns.catplot(x='State', y='Profit', data=df)
plt.show()

#kernel plot
sns.set_theme(style='darkgrid')
sns.kdeplot(x='Marketing_Spend', y='Profit', data=df)
plt.show()

#scstter plot
sns.set_theme(style='ticks')
sns.scatterplot(x='State', y='Profit', data=df)
plt.show()

#bar plot
sns.set_theme(style='white')
sns.barplot(x='State', y='Profit', data=df)
plt.show()