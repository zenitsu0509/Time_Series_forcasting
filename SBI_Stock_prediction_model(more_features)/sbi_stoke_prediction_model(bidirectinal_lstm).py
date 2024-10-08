import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM,Dropout, BatchNormalization,GRU,Bidirectional
from sklearn.metrics import mean_squared_error
from tensorflow.keras.optimizers import Adam
plt.style.use('ggplot')

df = pd.read_csv("/content/SBIN.NS (1).csv")

df.head()

df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Volume'])
plt.xlabel('Date')
plt.ylabel('Volume')
_ = plt.title('Trading Volume Over Time')

plt.figure(figsize=(16,8))
plt.plot(df['Date'], df['Close'], label='Close Price history')

moving_50 = df['Close'].rolling(window =50).mean()
moving_100 = df['Close'].rolling(window =100).mean()
moving_200 = df['Close'].rolling(window =200).mean()

plt.figure(figsize = (16,8))
plt.title("Close Price Visualization")
plt.plot(df['Close'])
plt.plot(moving_100, 'r')
plt.plot(moving_200, 'g')
plt.plot(moving_50, 'b')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()

train = df[0:int(len(df)*0.8)]
valid = df[int(len(df)*0.8):]

scaler = MinMaxScaler(feature_range=(0,1))

training_scalled_data = scaler.fit_transform(train['Close'].values.reshape(-1,1))
valid_scalled_data = scaler.fit_transform(valid['Close'].values.reshape(-1,1))

x_train = []
y_train = []
steps = 100
for i in range(steps, len(training_scalled_data)):
  x_train.append(training_scalled_data[i-steps:i])
  y_train.append(training_scalled_data[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)

x_train.shape

model = Sequential()
model.add(Bidirectional(GRU(units=100, activation='tanh', return_sequences=True), input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Bidirectional(GRU(units=120, activation='tanh', return_sequences=True)))
model.add(Dropout(0.3))
model.add(BatchNormalization())

model.add(GRU(units=120, activation='tanh'))
model.add(Dropout(0.5))


model.add(Dense(units=1))

model.compile(optimizer = Adam(learning_rate = 0.001), loss = 'mean_squared_error', metrics = ['MAE'])
history = model.fit(x_train, y_train ,epochs = 50)

test_close = valid['Close']
train_close = train['Close']
past_30_days = pd.DataFrame(train_close[-100:])
test_df = pd.DataFrame(test_close)
final_df = pd.concat([past_30_days, test_df], ignore_index=True)
test_data = scaler.fit_transform(final_df)

x_test = []
y_test = []
for i in range(100, test_data.shape[0]):
   x_test.append(test_data[i-100: i])
   y_test.append(test_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)
print(x_test.shape)
print(y_test.shape)

y_pred = model.predict(x_test)

scale_factor = 1/scaler.scale_[0]
y_pred = y_pred * scale_factor
y_test = y_test * scale_factor

plt.figure(figsize = (12,6))
plt.plot(y_test, 'b', label = "Original Price")
plt.plot(y_pred, 'r', label = "Predicted Price")
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper left')
plt.show()

from sklearn.metrics import r2_score, mean_squared_error

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print('R-squared:', r2)
print('MSE:', mse)

model.save('SBIN.keras')
