#Task-4

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Step 1: Load dataset
df=pd.read_csv("US_Startups.csv")
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

X = df[['R&D_Spend', 'Administration', 'Marketing_Spend']]
y = df['Profit']

for var in X:
    plt.figure() # Creating a rectangle (figure) for each plot
    sns.regplot(x=var, y='Profit', data=df)
    plt.show()

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Step 3: Train Model

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step 4: Evaluation

y_pred = regressor.predict(X_test)

print(regressor.intercept_)
print(regressor.coef_)

# Step 5: printing reasult

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

# Step 6: calculationg errors

print(r2_score(y_test, y_pred))
mse= print(mean_squared_error(y_test, y_pred))
mae= print(mean_absolute_error(y_test, y_pred))
rmse= print(np.sqrt(mean_squared_error(y_test, y_pred)))

