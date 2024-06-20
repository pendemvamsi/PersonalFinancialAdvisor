# 🚀 Personal Financial Advisor - Empowering Smart Financial Decisions Through AI and ML Learning

# Finance Chatbot

The Finance Chatbot is an interactive web application designed to answer finance-related questions. It utilizes a collection of pre-defined Q&A pairs, which can be easily updated to reflect the latest financial information.

## Features

- **Random Question Generator**: Displays a random finance question from the dataset.
- **Custom Question Input**: Users can input their own questions and receive tailored responses.
- **External Links in Responses**: Recognizes URLs in responses and provides clickable links for further reading.
- **User-Friendly Interface**: Built with Streamlit, ensuring a smooth and engaging user experience.

## Screenshots

1. **Main Interface**: The primary user interface where users interact with the chatbot.
<<<<<<< HEAD
   ![Main Interface](./images/financialchatbotinterface.png)

2. **Question Input**: Interface for entering custom finance questions.
   ![Question Input](./images/input.png)
=======
   ![Main Interface](path/to/screenshot1.png)

2. **Response Display**: Shows how answers are presented, including URL handling.
   ![Response Display](path/to/screenshot2.png)

3. **Question Input**: Interface for entering custom finance questions.
   ![Question Input](path/to/screenshot3.png)
>>>>>>> 8e272830fa817c7d602a5185766c124254197986

## Getting Started

Follow these instructions to set up the Finance Chatbot on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Streamlit
- A JSON file containing finance-related Q&A pairs (`config.json`)

Install the necessary Python packages using pip:

pip install streamlit
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
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
<<<<<<< HEAD

![User Interface](./images/newssentimentalinterface.png)
_Figure 1: Main User Interface showing the input fields for API key and ticker symbol._

### Sentiment Analysis Visualization

![Sentiment Analysis](./images/newssentimentalarticles.png)
_Figure 2: Visualization of sentiment analysis results and recommendation chart._

### Sentiment Analysis overTime Visualization

![Sentiment Analysis](./images/sentimentalscorenewsanalysis.png)
_Figure 3: Visualization of sentiment analysis results overtime._
=======
![User Interface](path/to/user-interface-image.png)
*Figure 1: Main User Interface showing the input fields for API key and ticker symbol.*

### Sentiment Analysis Visualization
![Sentiment Analysis](path/to/sentiment-analysis-image.png)
*Figure 2: Visualization of sentiment analysis results and recommendation chart.*

## Getting Started

1. Clone the repository:
   git clone https://github.com/yourusername/financial-news-sentiment-analysis.git
>>>>>>> 8e272830fa817c7d602a5185766c124254197986

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

<<<<<<< HEAD
1. **User Inputs**:

=======
1. **User Inputs**: 
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - Enter the ticker symbol of the stock.
   - Specify the start and end dates for retrieving stock data.
   - Provide details of monthly income and expenses.

2. **Expense Breakdown**:
<<<<<<< HEAD

   - A pie chart visualizes the breakdown of transportation, food, outings, other fixed costs, and variable costs.

3. **Savings and Investment**:

=======
   - A pie chart visualizes the breakdown of transportation, food, outings, other fixed costs, and variable costs.

3. **Savings and Investment**:
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
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
<<<<<<< HEAD

![Monthly Expense Breakdown](./images/personalfinanceinterface.png)

### Cumulative Savings Over Time

![Cumulative Savings Over Time](./images/personalfinanceinvestment.png)

### Investment Returns Distribution

![Investment Returns Distribution](./images/personalinvestmentreturns.png)

### Investment Returns Distribution

![Investment Returns Distribution](./images/personalinvestmentreturns.png)

# Predictions and Recommendations App 📈

Welcome to the Predictions and Recommendations app. This application allows you to visualize stock data and generate buy/sell signals based on different indicators, as well as predict future stock prices using the ARIMA model.

## Features and Functionalities 🛠️

1. **Buy and Sell Signal Alerts**: The app generates buy and sell signals based on stock data, including overbought and oversold signals derived from technical indicators like the Simple Moving Average (SMA) and Relative Strength Index (RSI).

2. **Real-Time Stock Data Fetching**: Utilizes the `yfinance` library to fetch real-time stock data for the specified ticker symbol and date range.

3. **ARIMA Model for Stock Price Prediction**: Implements the ARIMA model to forecast future stock prices, providing insights into potential market movements.

4. **Customizable Indicators**: Allows users to select and customize indicators such as SMA and RSI to tailor the analysis to their preferences.

5. **Interactive Visualizations**: Leverages Plotly for creating interactive charts, including candlestick charts with buy/sell signals, historical performance graphs, and forecasted price trends.

6. **Performance Metrics**: Calculates and displays model performance metrics, including Mean Squared Error (MSE) and Root Mean Squared Error (RMSE), to evaluate the predictive accuracy of the ARIMA model.

## Predictions and Recommendations 📊

The app provides valuable insights into stock market trends and potential investment opportunities by analyzing historical data and generating actionable buy/sell signals.

- **Buy/Sell Signals**: Based on the SMA and RSI indicators, the app identifies potential buy and sell opportunities.
- **Overbought/Oversold Alerts**: Alerts users to market conditions that may indicate overbought or oversold stocks.
- **Future Price Prediction**: Utilizes the ARIMA model to predict future stock prices, helping users make informed investment decisions.

## Screenshots 📸

1. **predictions and recommendation input**
   ![Stock Price Chart](./images/predict_input.png)

2. **Indicators: SMA and RSI Over Time alerts**
   ![SMA and RSI alerts](./images//predict_alert.png)

3. **Buy Signal Detection and sell signals**
   ![Buy Signal and sell](./images//predict_buysellsignals.png)

4. **Future Price Prediction**
   ![Future Prediction](./images/predict_future.png)

## How to Use the App

1. **Select Option**: Choose "Stock Prediction Buy and Selling Signals" from the options provided in the app interface.

2. **Input Parameters**:
   - Enter the ticker symbol of the stock.
   - Specify the start and end dates for fetching stock data.
   - Set the window size for SMA and RSI calculations.
   - Determine the number of days for forecasting and configure ARIMA model parameters.

3. **Select Indicators**: Choose the indicators (SMA, RSI) you wish to use for analysis.

4. **Generate Analysis**: Click the button to generate the stock analysis, which will display the buy/sell signals, visualizations, and future predictions.

The app provides a comprehensive toolset for investors to analyze stocks, make informed decisions, and visualize market trends through advanced statistical models.

=======
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
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
### Enhanced Robo-Advisor App - README

Welcome to the Enhanced Robo-Advisor App! This application provides personalized investment advice based on user input, leveraging real-time stock data, financial analysis, and advanced forecasting techniques. Below you'll find a detailed description of the app's features, functionalities, and usage instructions.

---

#### **Features and Functionalities**

1. **User Authentication**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - **Login System**: Secure login system to ensure personalized advice.
   - **Session Management**: Maintains user session for personalized interaction.

2. **Risk Profile Assessment**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - **Age and Risk Tolerance**: Users input their age and risk tolerance to determine their risk profile.
   - **Dynamic Risk Profiles**: Profiles such as Aggressive, Moderately Aggressive, Moderate, Moderately Conservative, and Conservative.

3. **Portfolio Allocation**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - **Suggested Portfolio**: Based on the user’s risk profile, the app suggests a suitable portfolio allocation.
   - **Customizable Portfolio**: Users can customize their portfolio by selecting specific stocks and bonds.

4. **Real-time Data Fetching**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - **Stock Prices**: Fetches real-time stock and bond prices using yfinance.
   - **Investment Distribution**: Calculates and displays the investment distribution based on real-time prices.

5. **Financial Metrics and Analysis**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - **Historical Performance**: Fetches historical data to analyze the portfolio's past performance.
   - **Metrics Calculation**: Calculates mean return, volatility, Sharpe ratio, and maximum drawdown.
   - **Scenario Analysis**: Allows users to simulate portfolio changes based on hypothetical market conditions.
   - **Monte Carlo Simulation**: Projects future portfolio values using Monte Carlo simulation to assess the likelihood of achieving financial goals.

6. **Visualizations**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - **Pie Chart**: Displays portfolio allocation breakdown.
   - **Line Charts**: Shows historical performance and future value projections.
   - **Histograms**: Represents distribution of future portfolio values from Monte Carlo simulations.

7. **Rebalancing Recommendations**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - **Rebalancing Alerts**: Provides alerts when the portfolio drifts significantly from the target allocation.

8. **Investment Goals and Planning**
   - **Goal Achievement**: Calculates the required annual return to achieve the user’s financial goals.
   - **Simulation Results**: Displays the probability of achieving financial goals based on simulations.

---

#### **How to Use the App**

1. **Login**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - Enter your username and password to log in to the app.
   - New users can sign up to create an account (future implementation).

2. **Provide User Inputs**
<<<<<<< HEAD

   - Enter your age, risk tolerance, investment amount, financial goal, and the time frame to achieve your goal.

3. **View Suggested Portfolio**

=======
   - Enter your age, risk tolerance, investment amount, financial goal, and the time frame to achieve your goal.

3. **View Suggested Portfolio**
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - Based on your inputs, the app will suggest a suitable portfolio allocation.
   - Customize your portfolio by selecting specific stocks and bonds.

4. **Analyze Portfolio**
<<<<<<< HEAD

=======
>>>>>>> 8e272830fa817c7d602a5185766c124254197986
   - View real-time data and historical performance metrics.
   - Check rebalancing recommendations and perform scenario analysis.

5. **Project Future Values**
   - Use the Monte Carlo simulation to project future portfolio values.
   - Assess the probability of achieving your financial goals.

---

#### **Images of the App**

1. **Login Page**
<<<<<<< HEAD
   ![Login Page](./images/robo_login.png)

2. **User Input Form**
   ![User Input Form](./images//robo_input.png)

3. **Portfolio Allocation Chart**
   ![Portfolio Allocation Chart](./images//robo_piechart.png)

4. **Historical Performance Graph**
   ![Historical Performance Graph](./images//robo_cumulative.png)

5. **Monte Carlo Simulation Results**
   ![Monte Carlo Simulation Results](./images//robo_future.png)
=======
   ![Login Page](https://via.placeholder.com/300x200.png?text=Login+Page)

2. **User Input Form**
   ![User Input Form](https://via.placeholder.com/300x200.png?text=User+Input+Form)

3. **Portfolio Allocation Chart**
   ![Portfolio Allocation Chart](https://via.placeholder.com/300x200.png?text=Portfolio+Allocation+Chart)

4. **Historical Performance Graph**
   ![Historical Performance Graph](https://via.placeholder.com/300x200.png?text=Historical+Performance+Graph)

5. **Monte Carlo Simulation Results**
   ![Monte Carlo Simulation Results](https://via.placeholder.com/300x200.png?text=Monte+Carlo+Simulation+Results)
>>>>>>> 8e272830fa817c7d602a5185766c124254197986

---

Thank you for using the Enhanced Robo-Advisor App. We hope it helps you make informed investment decisions and achieve your financial goals! For any questions or support, please contact our support team.

---

**Note:** This README includes placeholder images. Replace the image URLs with actual screenshots of your app to provide users with a visual guide.

<<<<<<< HEAD
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.
=======

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

>>>>>>> 8e272830fa817c7d602a5185766c124254197986
