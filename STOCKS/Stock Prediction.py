#stock prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1) Load data
df = pd.read_csv('AABA_2006-01-01_TO_2018-01-01.csv')
close_prices= df['Close'].values.reshape(-1,1)
print(df)

# 2) Scale data between 0 and 1
scaler = MinMaxScaler()
scaled = scaler.fit_transform(close_prices)
print(scaled)

# 3) Prepare sequences (last 10 days → next day)
X, y = [], []
for i in range(10, len(scaled)):
    X.append(scaled[i-10:i, 0])  # last 10 closes
    y.append(scaled[i, 0])       # next close
X, y = np.array(X), np.array(y)

# Reshape for LSTM: (samples, timesteps, features)
X = X.reshape(X.shape[0], X.shape[1], 1)
print(X)

# 4) Build simple LSTM model


model = Sequential([
    # First LSTM layer (returns sequences to feed next LSTM)
    LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
    
    # Second LSTM layer
    LSTM(50, return_sequences=True),
    
    # Third LSTM layer
    LSTM(50),
    
    # Dense layers (fully connected)
    Dense(25, activation="relu"),  
    Dense(1)                    
])

model.compile(optimizer="adam", loss="mse")
model.summary()

# 5) Train
model.fit(X, y, epochs=50, batch_size=8, verbose=0)

# 6) Predict last window
last_10 = scaled[-10:].reshape(1,10,1)
pred_scaled = model.predict(last_10)
pred_price = scaler.inverse_transform(pred_scaled)[0,0]

print(pred_price)

# 7) Plot actual vs. model fitted
pred_all = model.predict(X)
pred_all = scaler.inverse_transform(pred_all)
actual = scaler.inverse_transform(y.reshape(-1,1))

print(actual)

plt.plot(actual, label="Actual")
plt.plot(pred_all, label="Predicted")
plt.legend()
plt.title("Stocks Prediction")
plt.show()