import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to generate buy and sell signal alerts based on stock data including overbought and oversold signals
def generate_buy_sell_signals(data, window, rsi_window):
    signals = pd.DataFrame(index=data.index)
    signals['SMA'] = data['Close'].rolling(window=window).mean()
    
    # Calculate RSI
    rsi = RSIIndicator(data['Close'], window=rsi_window).rsi()

    # Generate buy and sell signals based on SMA
    signals['Buy_Signal'] = data['Close'] > signals['SMA']
    signals['Sell_Signal'] = data['Close'] < signals['SMA']
    
    # Generate overbought and oversold signals based on RSI
    overbought = 70
    oversold = 30
    signals['Overbought'] = (rsi > overbought) & (rsi.shift(1) <= overbought)
    signals['Oversold'] = (rsi < oversold) & (rsi.shift(1) >= oversold)
    
    return signals

# Function to fetch real stock data using the provided ticker symbol
def get_stock_data(symbol, start_date, end_date):
    try:
        stock = yf.download(symbol, start=start_date, end=end_date)
        if stock.empty:
            raise ValueError("No data found for the given ticker and date range.")
        return stock
    except Exception as e:
        logger.error(f"Error fetching stock data: {e}")
        return None

# Function to forecast using ARIMA
def forecast_with_arima(data, order, steps):
    model = ARIMA(data, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast, model_fit

# Function to generate stock prediction code
def generate_stock_prediction_code(symbol, start_date, end_date, window, rsi_window, selected_indicators, forecast_steps, arima_order):
    # Get stock data
    stock_data = get_stock_data(symbol, start_date, end_date)
    if stock_data is None:
        st.error("Failed to fetch stock data. Please check the provided ticker symbol and date range.")
        return

    st.write("Stock Data:")
    st.write(stock_data)

    try:
        # Generate buy and sell signal alerts
        signals = generate_buy_sell_signals(stock_data, window, rsi_window)
        st.write("Buy and Sell Signal Alerts:")

        # Display overbought and oversold signals
        if any(signals['Overbought']):
            st.info("Overbought Signal Detected!")
        if any(signals['Oversold']):
            st.info("Oversold Signal Detected!")
        
        # Plot candlestick chart with buy and sell signals
        fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                             open=stock_data['Open'],
                                             high=stock_data['High'],
                                             low=stock_data['Low'],
                                             close=stock_data['Close'],
                                             name='Candlestick')])

        # Add buy signals to the graph
        for buy_signal in signals.index[signals['Buy_Signal']]:
            fig.add_trace(go.Scatter(x=[buy_signal],
                                     y=[stock_data.loc[buy_signal, 'Low']],
                                     mode='markers',
                                     marker=dict(color='green', symbol='triangle-up', size=10),
                                     name='Buy Signal',
                                     hoverinfo='text',
                                     hovertext=f"Buy Signal: {buy_signal}"))

        # Add sell signals to the graph
        for sell_signal in signals.index[signals['Sell_Signal']]:
            fig.add_trace(go.Scatter(x=[sell_signal],
                                     y=[stock_data.loc[sell_signal, 'High']],
                                     mode='markers',
                                     marker=dict(color='red', symbol='triangle-down', size=10),
                                     name='Sell Signal',
                                     hoverinfo='text',
                                     hovertext=f"Sell Signal: {sell_signal}"))

        # Add selected indicators to the graph
        for indicator in selected_indicators:
            if indicator == 'SMA':
                sma = SMAIndicator(stock_data['Close'], window)
                stock_data['SMA'] = sma.sma_indicator()
                fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA'], mode='lines', name='SMA'))
            elif indicator == 'RSI':
                stock_data['RSI'] = RSIIndicator(stock_data['Close'], window=rsi_window).rsi()
                fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['RSI'], mode='lines', name='RSI'))

        # Update layout
        fig.update_layout(title='Stock Price Chart with Buy/Sell Signals and Selected Indicators',
                          xaxis_title='Date',
                          yaxis_title='Price')

        st.plotly_chart(fig)

        # Forecast future prices
        forecast, model_fit = forecast_with_arima(stock_data['Close'], arima_order, forecast_steps)
        future_index = pd.date_range(start=stock_data.index[-1], periods=forecast_steps + 1, freq='B')[1:]
        forecast_series = pd.Series(forecast, index=future_index)

        # Plot future predictions
        fig_forecast = go.Figure()
        fig_forecast.add_trace(go.Scatter(x=forecast_series.index, y=forecast_series.values, mode='lines', name='Predicted Price'))
        fig_forecast.update_layout(title='Future Stock Price Prediction',
                                   xaxis_title='Date',
                                   yaxis_title='Price')
        st.plotly_chart(fig_forecast)

        # Calculate and display model performance
        mse = mean_squared_error(stock_data['Close'].tail(forecast_steps), forecast)
        rmse = np.sqrt(mse)
        st.write(f'Model Performance - MSE: {mse}, RMSE: {rmse}')

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Setting up Streamlit app layout
st.markdown(
    """
<style>
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        padding: 10px;
        border-bottom: 2px solid #ccc;
    }
    .code {
        border: 2px solid #ff5733;
        padding: 10px;
        background-color: #f0f0f0;
        margin-top: 10px;
    }
</style>
""",
    unsafe_allow_html=True
)

# Header and introduction
st.markdown("<h1 class='header'>Predictions and Recommendations</h1>", unsafe_allow_html=True)
st.markdown("Welcome to the Predictions and Recommendations app. This app allows you to visualize stock data and generate buy/sell signals based on different indicators, as well as predict future stock prices using the ARIMA model.", unsafe_allow_html=True)
st.write("--------------------------------------------------------")

# Option selection
option = st.selectbox("Select an option:", ["Stock Prediction Buy and Selling Signals"])

# Displaying code based on selected option
if option == "Stock Prediction Buy and Selling Signals":
    st.write("You've selected the Stock Prediction Buy and Selling Signals option.")
    st.write("Please provide the following information:")

    # User input for stock prediction
    symbol = st.text_input("Enter the ticker symbol of the stock (e.g., AAPL):").upper()
    start_date = st.date_input("Enter the start date:")
    end_date = st.date_input("Enter the end date:")
    window = st.number_input("Enter the window size for SMA:", min_value=1)
    rsi_window = st.number_input("Enter the window size for RSI calculation:", min_value=1)
    forecast_steps = st.number_input("Enter the number of days to forecast:", min_value=1, max_value=30)
    arima_order = (
        st.slider("ARIMA Model - Autoregressive (p):", 0, 5, 1),
        st.slider("ARIMA Model - Integrated (d):", 0, 2, 1),
        st.slider("ARIMA Model - Moving Average (q):", 0, 5, 1)
    )

    # Checkbox for selecting indicators
    st.write("Select Indicators:")
    selected_indicators = []
    if st.checkbox("SMA"):
        selected_indicators.append("SMA")
    if st.checkbox("RSI"):
        selected_indicators.append("RSI")

    # Generate code and signals
    generate_stock_prediction_code(symbol, start_date, end_date, window, rsi_window, selected_indicators, forecast_steps, arima_order)
