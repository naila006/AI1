#pandas

import pandas as pd
df=pd.read_csv("FastFoodResturants.csv", delimiter=',' )
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
city=df['city']
print(city)

#access another coloumn
country=df['country']
print(country)

#access multiple coloumns
city_country=df[['city','country']]
print(city_country)

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
i=df.loc[df['city']== 'Minot']
print(i)

#conditional selection using loc
m=df.loc[df['country']=='US']
print(m)

#Selecting a single column using .loc 
a = df.loc[:7,'city']
print(a)

c=df.loc[:7,'country']
print(c)

d=df.loc[:7,'longitude']
print(d)

e=df.loc[:7,'latitude']
print(e)

f=df.loc[:7,'name']
print(f)

#selecting a slice of coloumn
g=df.loc[:7,'city':'name']
print(g)

#combined row and coloumn selection usimg .loc
h= df.loc[df['city']=='Minot','city':'longitude']
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
p= df.iloc[:,[2,4,7]]
print(p)

#selecting a slice of coloumn using .iloc
q= df.iloc[:,2:5]
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
df.drop('longitude', axis=1, inplace=True)
#deleting multiple coloumns from dataframe
df.drop(['latitude','name'], axis=1, inplace=True)
print(df)

#rename coloumn
df.rename({'name':'name_Changed'}, inplace=True)
print(df)

#rename label
df.rename({3:5}, inplace=True)
print(df)

#query to select data
df.query('city != \'Minot\' or postalCode == 45011')
print(df)

#sort data in ascending order
df.sort_values('postalCode')
print(df.to_string(index=False))

#grouping dataframe by city
df.groupby('city')['city'].sum()
print(df.to_string())
print('df:', len(df))

#using dropna() to remove rows with mising values
t=df.dropna()
print("Cleaned Data:\n", t)

#filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)