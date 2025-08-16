#machine learning program

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('medical_industry.csv')
df.set_index("Years")
print(df)

#print datatypes
print("dtype", df.dtypes)

#print data info
print("df.info", df.info())

#print statics operations
print("statics operations", df.describe())

#printing no of rows and coloumns
print("no of rows and coloumns", df.shape)

#making graph using matplot
df.plot.scatter(x='Female_Doctors', y='Female_Dentists')
plt.show()

#reshaping
x=df['Female_Doctors'].values.reshape(-1,1)
y=df['Female_Dentists'].values.reshape(-1,1)

print(x)
print(y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 20)

print(X_train) 
print(y_train)


#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

print(regressor.intercept_)

print(regressor.coef_)

def calc(slope, intercept, hours):
    return slope*hours+intercept

price = calc(regressor.coef_, regressor.intercept_, 3146)
print(price)
price = regressor.predict([[3146]])
print(price)
y_perd = regressor.predict(X_test)

df_pred = pd.DataFrame({"Actual": y_test.squeeze() , "predicted": y_perd.squeeze()})

print(df_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test,y_perd)
mse = mean_squared_error(y_test,y_perd)
rmse= np.sqrt(mse)
r2 = r2_score(y_test,y_perd)

print(mae)
print(mse)
print(rmse)
print(r2)