#Task-5

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Step 1: Load Dataset

df = pd.read_csv("California_housing.csv")  
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


# Step 2: Prepare Data

X = df[['housing_median_age','total_rooms','total_bedrooms']]
y = df['median_house_value']

for var in X:
    plt.figure() # Creating a rectangle (figure) for each plot
    sns.regplot(x=var, y='median_house_value', data=df)
    plt.show()

# Step 3: Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=98)

# Step 4: Model Training

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step 5: Predictions

y_pred = regressor.predict(X_test)

# Step 6: Evaluation

                  
