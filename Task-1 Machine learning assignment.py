#machine learning assignment
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("RealEstate-USA1.csv", na_filter=False)
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
df.plot.scatter(x='Assessed_value', y='Sale_amount')
plt.show()

#reshaping
X=df['Assessed_value'].values.reshape(-1,1)
y=df['Sale_amount'].values.reshape(-1,1)

print(X)
print(y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 50)

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

price = calc(regressor.coef_, regressor.intercept_, 50000 )
print(price)
price = regressor.predict([[50000]])
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







