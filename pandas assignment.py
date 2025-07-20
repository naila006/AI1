#Week2 Assignment no 1 part 2
import  pandas as pd

df=pd.read_csv("RealEstate-USA.csv", delimiter=',' )
df.set_index("brokered_by")
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
street=df['street']
print(street)

#access multiple coloumns
city_street=df[['city','street']]
print(city_street)

#.loc cases
#selectig a row using .loc
b= df.loc[52707]
print(b)

#selecting multiple row using .loc
row= df.loc[[103378,1205]]
print(row)

#selecting a slice of coloumns
j= df.loc[1205:52707]
print(j)

#conditional selection of rows
i=df.loc[df['city']== 'Ajuntas']
print(i)

#conditional selection using loc
m=df.loc[df['price']=='100000']
print(m)

#Selecting a single column using .loc 
a = df.loc[:52707,'city']
print(a)

c=df.loc[:52707,'price']
print(c)

d=df.loc[:52707,'street']
print(d)

e=df.loc[:52707,'zip_code']
print(e)

f=df.loc[:52707,'acre_lot']
print(f)

#selecting a slice of coloumn
g=df.loc[:52707,'city':'zip_code']
print(g)

#combined row and coloumn selection usimg .loc
h= df.loc[df['city']=='Ajuntas','city':'zip_code']
print(h)

#.iloc cases
#selecting a single row using .iloc
k= df.iloc[52707]
print(k)

#selecting multiple coloumns using .iloc
l= df.iloc[[1205,52707]]
print(l)

#selecting a slice of coloumns using .iloc
n= df.iloc[1205:52707]
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

#combined row and coloumn using .iloc
r= df.iloc[[7,9,15],2,4]
print(r)

#combined rows and coloumsd using .iloc
s= df.iloc[[2,6],2:4]
print(s)

#adding a new row to dataframe
df.loc[len(df)]=[1208,"for_sale",112300,4,9,0.09,6710,"Moca","Puerto Rico",769,1500]
print(df)

#deleting a row fom dataframe
df.drop(52707, axis=0, inplace=True)
#deleting rows from one index to another
df.drop([1205,52707], axis=0, inplace=True)
print(df)

#deleting a coloumn from dataframe
df.drop('house_size', axis=1, inplace=True)
#deleting multiple coloumns from dataframe
df.drop(['house_size','status'], axis=1, inplace=True)
print(df)

#rename coloumn
df.rename({'state':'state_Changed'}, inplace=True)
print(df)

#rename label
df.rename({3:5}, inplace=True)
print(df)

#query to select data
df.query('city != \'Ajuntas\' or price < 127400')
print(df)

#sort data in ascending order
df.sort_values('price')
print(df.to_string(index=False))

#grouping dataframe by city
df.groupby('city')['price'].sum()
print(df.to_string())
print('df:', len(df))

#using dropna() to remove rows with mising values
t=df.dropna()
print("Cleaned Data:\n", t)

#filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)