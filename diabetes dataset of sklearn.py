# deep learning

import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv('diabetes.csv')
print(df.shape)  
X = df.drop('Outcome', axis=1)  
y = df['Outcome']               

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,        
    random_state=42,      
    shuffle=True          
   )
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('diabetes.csv')

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    shuffle=True,
    stratify=y
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train class distribution:\n", y_train.value_counts(normalize=True))
print("y_test class distribution:\n", y_test.value_counts(normalize=True))