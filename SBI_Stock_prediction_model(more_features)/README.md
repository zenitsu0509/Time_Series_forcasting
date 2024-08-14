# SBI Stock Prediction Model

This repository contains a model for predicting SBI (State Bank of India) stock prices using a bidirectional LSTM neural network.

## Model Performance

- **R-squared:** 0.9837298304944812
- **Mean Squared Error (MSE):** 187.26126920685456

These metrics indicate that the model performs very well in predicting SBI stock prices.

## Files in the Repository

- **SBIN.NS (1).csv:** The dataset used for training and testing the model.
- **SBI_stock_prediction_model(bidirectional_lstm).ipynb:** The Jupyter notebook containing the code for the model.
- **sbi_stock_prediction_model(bidirectional_lstm):** The trained model file (if applicable).

## Visualizations

### Moving Average of 50, 100, and 200 Days

![Moving Average of 50, 100, and 200 Days](https://github.com/zenitsu0509/Time_Series_forcasting/blob/f0336084df33d6a09b14858dba74b989a62a6880/IRFC_stock_prediction_model/assets/Screenshot%202024-08-14%20133622.png)

### Predicted Model

![Predicted Model](https://github.com/zenitsu0509/Time_Series_forcasting/blob/f0336084df33d6a09b14858dba74b989a62a6880/IRFC_stock_prediction_model/assets/Screenshot%202024-08-14%20133645.png)

### Epochs vs Training Loss

![Epochs vs Training Loss](https://github.com/zenitsu0509/Time_Series_forcasting/blob/f0336084df33d6a09b14858dba74b989a62a6880/IRFC_stock_prediction_model/assets/Screenshot%202024-08-14%20133700.png)

## How to Use

1. Clone the repository.
2. Open the Jupyter notebook `SBI_stock_prediction_model(bidirectional_lstm).ipynb`.
3. Ensure that all dependencies are installed.
4. Run the notebook to train the model or load the pre-trained model.

## Dependencies

- Python 3.x
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib

## Conclusion

This model offers high accuracy in predicting the stock prices of SBI using historical data. The use of bidirectional GRU enhances the prediction capabilities by considering both past and future states in the sequence of data.
<br>
Happy Coding.😊 Go and play with code
