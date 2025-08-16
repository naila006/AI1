#multiple regression

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("50_Startups(1).csv", na_filter=False)
print(df)

#print datatypes
print("dtype", df.dtypes)

#print data info
print("df.info", df.info())

#print statics operations
print("statics operations", df.describe())

#printing no of rows and coloumns
print("no of rows and coloumns", df.shape)

import seaborn as sns # Convention alias for Seaborn

variables = ['R&D_Spend', 'Administration', 'Marketing_Spend']

for var in variables:
    plt.figure() # Creating a rectangle (figure) for each plot
    
    sns.regplot(x=var, y='Profit', data=df).set(title=f'Regression plot of {var} and Profit');
    plt.show()

a= input("wait, \n")    

plt.figure()

correlations= print(df.corr())

y = df['Profit']
X = df[['R&D_Spend', 'Administration',
       'Marketing_Spend']]
print(y)
print(X)

#After setting our X and y sets, we can divide our data into train and test sets. We will be using the same seed and 10% of our data for training:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.1, 
                                                    random_state= 90)

print(X.shape)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

#After fitting the model and finding our optimal solution, we can also look at the intercept:
print(regressor.intercept_)

#And at the coefficients of the features
print(regressor.coef_)






