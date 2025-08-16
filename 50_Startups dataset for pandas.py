#PANDAS

import pandas as pd
df=pd.read_csv("50_Startups.csv", delimiter=',' )
print(df)

#print datatypes
print("dtype", df.dtypes)

#print data info
print("df.info", df.info())

#print statics operations
print("statics operations", df.describe())

#printing no of rows and coloumns
print("no of rows and coloumns", df.shape)

#display the first 7 rows
print("first 7 rows:")
print(df.head(7))

#display the last 9 rows
print("last 9 rows:")
print(df.tail(9))

#access a coloumn
spend=df['R&D_Spend']
print(spend)

#access another coloumn
admin=df['Administration']
print(admin)

#access multiple coloumns
spend_admin=df[['R&D_Spend','Administration']]
print(spend_admin)

#.loc cases
#selectig a row using .loc
b= df.loc[34]
print(b)

#selecting multiple row using .loc
row= df.loc[[12,38]]
print(row)

#selecting a slice of coloumns
j= df.loc[12:16]
print(j)

#conditional selection of rows
i=df.loc[df['State']== 'New York']
print(i)

#conditional selection using loc
m=df.loc[df['State']=='Florida']
print(m)

#Selecting a single column using .loc 
a = df.loc[:7,'Profit']
print(a)

c=df.loc[:7,'Administration']
print(c)

d=df.loc[:7,'State']
print(d)

e=df.loc[:7,'Marketing_Spend']
print(e)

f=df.loc[:7,'R&D_Spend']
print(f)

#selecting a slice of coloumn
g=df.loc[:7,'R&D_Spend':'State']
print(g)

#combined row and coloumn selection usimg .loc
h= df.loc[df['State']=='New York','R&D_Spend':'Administration']
print(h)

#.iloc cases
#selecting a single row using .iloc
k= df.iloc[42]
print(k)

#selecting multiple coloumns using .iloc
l= df.iloc[[5,27]]
print(l)

#selecting a slice of coloumns using .iloc
n= df.iloc[5:10]
print(n)

#selecting single coloumn using .iloc
o= df.iloc[:,3]
print(o)

#selecting multiple coloums using .iloc
p= df.iloc[:,[2,4]]
print(p)

#selecting a slice of coloumn using .iloc
q= df.iloc[:,2:4]
print(q)

#combined rows and coloumsd using .iloc
s= df.iloc[[2,6],2:4]
print(s)

#deleting a row fom dataframe
df.drop(8, axis=0, inplace=True)
#deleting rows from one index to another
df.drop([6,9], axis=0, inplace=True)
print(df)

#deleting a coloumn from dataframe
df.drop('Profit', axis=1, inplace=True)
#deleting multiple coloumns from dataframe
df.drop(['Administration','R&D_Spend'], axis=1, inplace=True)
print(df)

#rename coloumn
df.rename({'State':'State_Changed'}, inplace=True)
print(df)

#rename label
df.rename({3:5}, inplace=True)
print(df)

#query to select data
df.query('State != \'Florida\' or Marketing_Spend == 471784.1 ')
print(df)

#sort data in ascending order
df.sort_values('Marketing_Spend')
print(df.to_string(index=False))

#grouping dataframe by state
df.groupby('State')['State'].sum()
print(df.to_string())
print('df:', len(df))

#using dropna() to remove rows with mising values
t=df.dropna()
print("Cleaned Data:\n", t)

#filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)