# Finance Chatbot

The Finance Chatbot is an interactive web application designed to answer finance-related questions. It utilizes a collection of pre-defined Q&A pairs, which can be easily updated to reflect the latest financial information.

## Features

- **Random Question Generator**: Displays a random finance question from the dataset.
- **Custom Question Input**: Users can input their own questions and receive tailored responses.
- **External Links in Responses**: Recognizes URLs in responses and provides clickable links for further reading.
- **User-Friendly Interface**: Built with Streamlit, ensuring a smooth and engaging user experience.

## Screenshots

1. **Main Interface**: The primary user interface where users interact with the chatbot.
   ![Main Interface](path/to/screenshot1.png)

2. **Response Display**: Shows how answers are presented, including URL handling.
   ![Response Display](path/to/screenshot2.png)

3. **Question Input**: Interface for entering custom finance questions.
   ![Question Input](path/to/screenshot3.png)

## Getting Started

Follow these instructions to set up the Finance Chatbot on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Streamlit
- A JSON file containing finance-related Q&A pairs (`config.json`)

Install the necessary Python packages using pip:

pip install streamlit
# Financial News Sentiment Analysis App

This application fetches financial news articles based on a given stock ticker, analyzes the sentiment of these articles, and provides buy or sell recommendations based on the analysis.

## Features

- **Fetch Financial News**: Retrieve the latest financial news articles for any given stock ticker using the News API.
- **Sentiment Analysis**: Analyze the sentiment of each article's title and description to determine the overall sentiment polarity.
- **Dynamic Recommendations**: Provide real-time recommendations (BUY, SELL, or HOLD) based on the average sentiment of the news articles.
- **Data Visualization**: Visualize sentiment trends over time with interactive plots.
- **CSV Download**: Allow users to download the sentiment analysis results as a CSV file for further analysis.
- **User-Friendly Interface**: Streamlined interface built with Streamlit for easy interaction and accessibility.

## Functionalities

1. **Enter API Key and Ticker Symbol**: Users input their News API key and the ticker symbol of the stock they are interested in.
2. **Fetch News**: Upon entering the details and pressing the button, the application fetches the news articles related to the specified ticker.
3. **Sentiment Analysis**: The application analyzes the sentiment of each fetched article to determine its polarity.
4. **Recommendations**: Based on the analysis, the app provides recommendations to BUY, SELL, or HOLD the stock.
5. **Display and Download Data**: The application displays the news articles along with their sentiment scores and provides an option to download this data as a CSV file.
6. **Visual Sentiment Trends**: Interactive graphs show sentiment trends over time, helping users visualize the sentiment changes.

## Screenshots

### User Interface
![User Interface](path/to/user-interface-image.png)
*Figure 1: Main User Interface showing the input fields for API key and ticker symbol.*

### Sentiment Analysis Visualization
![Sentiment Analysis](path/to/sentiment-analysis-image.png)
*Figure 2: Visualization of sentiment analysis results and recommendation chart.*

## Getting Started

1. Clone the repository:
   git clone https://github.com/yourusername/financial-news-sentiment-analysis.git

# Personal Finance Management App

This application helps users manage their monthly budgets efficiently and provides investment recommendations based on their financial inputs. It also fetches real-time stock data and analyzes investment returns.

## Features

- **Monthly Budget Management**: Track and manage monthly expenses and income to ensure financial stability.
- **Expense Breakdown**: Visualize the breakdown of monthly expenses through a pie chart.
- **Savings Calculation**: Calculate monthly savings and suggest investment amounts.
- **Real-Time Stock Data**: Fetch and display real-time stock data for a given ticker symbol.
- **Investment Prediction**: Predict the amount of money returned from stock investments.
- **Moving Average Analysis**: Calculate and plot the 50-day moving average for stock prices.
- **Investment Returns Analysis**: Analyze and visualize the distribution of investment returns.

## Functionalities

1. **User Inputs**: 
   - Enter the ticker symbol of the stock.
   - Specify the start and end dates for retrieving stock data.
   - Provide details of monthly income and expenses.

2. **Expense Breakdown**:
   - A pie chart visualizes the breakdown of transportation, food, outings, other fixed costs, and variable costs.

3. **Savings and Investment**:
   - Calculate and display monthly savings.
   - Recommend an investment amount based on savings.
   - Predict the potential returns from the investment.

4. **Stock Data Analysis**:
   - Display real-time stock data.
   - Plot cumulative savings over time based on stock data.
   - Generate a histogram for the distribution of investment returns.
   - Plot the 50-day moving average for stock prices.

## Images

### Monthly Expense Breakdown
![Monthly Expense Breakdown](image_path_1.png)

### Cumulative Savings Over Time
![Cumulative Savings Over Time](image_path_2.png)

### Investment Returns Distribution
![Investment Returns Distribution](image_path_3.png)

## How to Run

1. Install the required packages:
   pip install streamlit yfinance matplotlib numpy
# Predictions and recommendations


This application is designed to help users manage their monthly budgets effectively and provide investment recommendations based on their financial inputs. The app fetches real-time stock data, analyzes investment returns, generates buy/sell signals, and predicts future stock prices using the ARIMA model.

## Features

### Monthly Budget Management
- **Expense Tracking**: Record and categorize your monthly expenses.
- **Income Tracking**: Keep track of your monthly income sources.
- **Budget Visualization**: Visualize the distribution of expenses and income with interactive charts.
- **Budget Limits**: Set budget limits and receive alerts when nearing the limits.

### Real-Time Stock Data
- **Stock Data Fetching**: Fetch real-time stock data using the Yahoo Finance API.
- **Stock Visualization**: Visualize stock price trends with interactive candlestick charts.
- **Stock Performance Analysis**: Analyze stock performance over different periods.

### Investment Analysis and Recommendations
- **Buy and Sell Signal Alerts**: Generate buy and sell signal alerts based on selected indicators such as Simple Moving Average (SMA) and Relative Strength Index (RSI).
- **Overbought and Oversold Signals**: Identify overbought and oversold conditions to make informed investment decisions.
- **Stock Price Prediction**: Predict future stock prices using the ARIMA model and visualize the forecasted trends.


    ```

### Stock Prediction Buy and Selling Signals

1. **Enter Stock Information**:
    - Enter the ticker symbol of the stock (e.g., AAPL).
    - Select the start date and end date for the stock data.

2. **Configure Indicators**:
    - Set the window size for the Simple Moving Average (SMA).
    - Set the window size for the Relative Strength Index (RSI).

3. **Forecast Configuration**:
    - Enter the number of days to forecast.
    - Configure the ARIMA model parameters: Autoregressive (p), Integrated (d), and Moving Average (q).

4. **Generate Signals and Forecast**:
    - Click to generate buy and sell signals based on the selected indicators.
    - View the overbought and oversold signals.
    - Visualize the stock price trend with buy/sell signals.
    - View the future stock price prediction.

## Examples

### Example 1: Budget Visualization
![Budget Visualization](path/to/budget_visualization.png)

### Example 2: Stock Price Chart with Buy/Sell Signals
![Stock Price Chart](path/to/stock_price_chart.png)

### Example 3: Future Stock Price Prediction
![Stock Price Prediction](path/to/stock_price_prediction.png)

## Screenshots

### Budget Visualization
![Budget Visualization](path/to/budget_visualization.png)
*This screenshot shows the distribution of monthly expenses and income in an interactive pie chart.*

### Stock Price Chart with Buy/Sell Signals
![Stock Price Chart](path/to/stock_price_chart.png)
*This screenshot shows the stock price trend with buy and sell signals marked on a candlestick chart.*

### Future Stock Price Prediction
![Stock Price Prediction](path/to/stock_price_prediction.png)
*This screenshot shows the future stock price prediction using the ARIMA model, displayed as a line chart.*

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

