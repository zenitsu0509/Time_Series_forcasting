# IRFC Stock Prediction Model

This project focuses on predicting the stock prices of IRFC (Indian Railway Finance Corporation) using time series forecasting techniques. The model has been evaluated using R-squared and Mean Squared Error (MSE) metrics.

## Project Structure

- `assets/`
  - `Screenshot 2024-08-12 200550.png`: Moving average of 15 and 30 days.
  - `Screenshot 2024-08-12 200638.png`: Predicted model visualization.

- `IRFC.NS.csv`: The dataset containing historical stock prices of IRFC.

- `IRFC_stock_prediction_model.ipynb`: Jupyter Notebook containing the implementation of the stock prediction model.

- `irfc_stock_prediction_model.py`: Python script for the stock prediction model.

- `README.md`: Project documentation.

## Model Performance

- **R-squared**: 0.8633
- **MSE**: 65.399

These metrics indicate the model's performance in predicting the stock prices of IRFC.

## Visualizations

![Moving average of 15 and 30 days](assets/Screenshot%202024-08-12%20200550.png)

The moving average of 15 and 30 days helps to smooth out the stock prices and better understand the trend.

![Predicted model](assets/Screenshot%202024-08-12%20200638.png)

The above image shows the predicted stock prices using the model.

## How to Run

1. Clone this repository.
2. Install the necessary dependencies (e.g., pandas, numpy, scikit-learn, matplotlib).
3. Run the Jupyter Notebook `IRFC_stock_prediction_model.ipynb` or the Python script `irfc_stock_prediction_model.py`.

## Conclusion

This project demonstrates a basic approach to predicting stock prices using time series forecasting methods. The model performs well with an R-squared of 0.8633 and an MSE of 65.399.

