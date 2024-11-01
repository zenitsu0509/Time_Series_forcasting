import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.layers import Dropout, BatchNormalization

df = pd.read_csv('/content/IRFC.NS.csv')

df.head()

df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16,8))
plt.plot(df['Date'], df['Close'], label='Close Price history')

new_df = df[df['Date'] >= '2022-08-01']

plt.figure(figsize=(16,8))
plt.plot(new_df['Date'], new_df['Close'], label='Close Price history')

moving_15 = new_df['Close'].rolling(window =15).mean()
moving_30 = new_df['Close'].rolling(window =30).mean()

plt.figure(figsize = (16,8))
plt.title("Close Price Visualization")
plt.plot(df['Close'])
plt.plot(moving_15, 'r')
plt.plot(moving_30, 'g')
plt.show()

new_df.isnull().sum()

train = new_df[0:int(len(new_df)*0.8)]
valid = new_df[int(len(new_df)*0.8):]

scaler = MinMaxScaler(feature_range=(0,1))

testing_scalled_data = scaler.fit_transform(new_df['Close'].values.reshape(-1,1))
valid_scalled_data = scaler.fit_transform(valid['Close'].values.reshape(-1,1))

x_train = []
y_train = []
steps = 30
for i in range(steps, len(testing_scalled_data)):
  x_train.append(testing_scalled_data[i-steps:i])
  y_train.append(testing_scalled_data[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)

x_train.shape

model = Sequential()
model.add(LSTM(units = 30, activation = 'relu', return_sequences=True
              ,input_shape = (x_train.shape[1], 1)))
model.add(Dropout(0.2))


model.add(LSTM(units = 40, activation = 'relu', return_sequences=True))
model.add(Dropout(0.3))

model.add(Dense(units = 1))

model.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['MAE'])
model.fit(x_train, y_train ,epochs = 50,)

past_30_days = testing_scalled_data[-30:]
past_30_days_df = pd.DataFrame(past_30_days)

test_df = pd.DataFrame(valid['Close'])

# Use the concat function instead of append
final_df = pd.concat([past_30_days_df, test_df], ignore_index=True)

inputs = scaler.transform(final_df.values.reshape(-1,1))

inputs.shape

x_test = []
y_test = []
for i in range(steps, inputs.shape[0]):
  x_test.append(inputs[i-steps:i])
  y_test.append(inputs[i, 0])
x_test = np.array(x_test)

x_test, y_test = np.array(x_test), np.array(y_test)
print(x_test.shape)
print(y_test.shape)



y_pred = model.predict(x_test)

scaler.scale_

scale_factor = 1/0.01073192
y_pred = y_pred * scale_factor
y_test = y_test * scale_factor
