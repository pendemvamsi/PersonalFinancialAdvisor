import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Function to fetch real stock data using the provided ticker symbol
def get_stock_data(symbol, start_date, end_date):
    stock = yf.download(symbol, start=start_date, end=end_date)
    return stock

# Function to predict the amount of money returned to the user after retrieving from stocks
def predict_money_returned(stock_data, investment_in_stocks):
    stock_data['Price_Change'] = stock_data['Close'].pct_change()
    total_return = (stock_data['Price_Change'] * investment_in_stocks).sum()
    return total_return

# Function to calculate moving average
def moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

# Function to display financial chatbot
def financial_questions_chatbot():
    st.title("PERSONAL FINANCE MANAGEMENT")
    st.write("### Efficient Monthly Budget Management")
    st.write(
        "Managing a monthly budget effectively ensures financial stability by aligning expenses with income, "
        "while also allowing room for saving and investing."
    )

    # User Input
    symbol = st.text_input("Enter a stock ticker symbol (e.g., AAPL for Apple Inc.):")
    start_date = st.date_input("Start date for stock data:")
    end_date = st.date_input("End date for stock data:")
    net_income = st.number_input("Your net fixed income per month:", min_value=0)
    transportation_costs = st.number_input("Monthly transportation expenses:", min_value=0)
    food_costs = st.number_input("Monthly food expenses:", min_value=0)
    outing_expenses = st.number_input("Monthly outing expenses:", min_value=0)
    other_fixed_costs = st.number_input("Other fixed monthly expenses:", min_value=0)
    has_variable_costs = st.radio("Do you have variable costs?", ("Yes", "No"))

    # Variable costs input
    variable_costs = {}
    if has_variable_costs == "Yes":
        st.write("Enter variable costs for each month:")
        for month in range(1, 13):
            variable_costs[f"Month {month}"] = st.number_input(f"Variable costs for Month {month}:", min_value=0)

    available_savings = st.number_input("Available savings:", min_value=0)

    # Calculate total expenses and savings
    total_expenses = transportation_costs + food_costs + outing_expenses + other_fixed_costs + sum(variable_costs.values())
    savings = available_savings + net_income - total_expenses
    investment_in_stocks = savings * 0.20  # 20% of savings recommended for investment

    # Display Summary
    st.write("## Summary of Your Inputs")
    st.write(f"**Stock Symbol:** {symbol}")
    st.write(f"**Start Date:** {start_date}")
    st.write(f"**End Date:** {end_date}")
    st.write(f"**Total Expenses:** {total_expenses}")
    st.write(f"**Savings:** {savings}")

    # Financial recommendations
    if savings > 0:
        st.success(f"Good job! Your monthly savings: {savings}")
        st.write(f"Recommended stock investment (20% of savings): {investment_in_stocks}")
    elif savings < 0:
        st.error(f"You're running a deficit of {-savings}. Consider reducing expenses or increasing income.")
    else:
        st.warning("Your income and expenses are equal. Consider saving for future needs.")

    # Pie chart for expense breakdown
    if total_expenses > 0:
        expenses_labels = ['Transportation', 'Food', 'Outings', 'Other Fixed', 'Variable']
        expenses_values = [transportation_costs, food_costs, outing_expenses, other_fixed_costs, sum(variable_costs.values())]

        fig, ax = plt.subplots()
        ax.pie(expenses_values, labels=expenses_labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    # Fetch and analyze stock data
    if symbol:
        st.write("Fetching stock data...")
        stock_data = get_stock_data(symbol, start_date, end_date)

        if not stock_data.empty:
            st.write("### Stock Data Overview")
            st.write(stock_data.head())

            # Cumulative Savings Over Time Plot
            st.subheader("Cumulative Savings Over Time")
            savings_over_time = np.cumsum(stock_data['Close'].pct_change() * investment_in_stocks)

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(savings_over_time, label='Cumulative Savings')
            ax.set_title("Cumulative Savings Over Time")
            ax.set_xlabel("Days")
            ax.set_ylabel("Savings")
            ax.legend()
            st.pyplot(fig)

            # Investment Returns Distribution
            st.subheader("Investment Returns Distribution")
            returns = stock_data['Close'].pct_change() * investment_in_stocks

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.hist(returns.dropna(), bins=30, alpha=0.75, label='Returns')
            ax.set_title("Investment Returns Distribution")
            ax.set_xlabel("Return Amount")
            ax.set_ylabel("Frequency")
            ax.legend()
            st.pyplot(fig)

            # Stock Price and Moving Average Plot
            st.subheader("Stock Price & 50-Day Moving Average")
            stock_data['50_MA'] = moving_average(stock_data, 50)

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(stock_data['Close'], label='Close Price')
            ax.plot(stock_data['50_MA'], label='50-Day Moving Average', color='orange')
            ax.set_title("Stock Price and 50-Day Moving Average")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price")
            ax.legend()
            st.pyplot(fig)

            # Predict money returned from stocks
            st.write("### Predicted Money Returned from Stocks")
            money_returned = predict_money_returned(stock_data, investment_in_stocks)

            if money_returned > 0:
                st.success(f"You made a profit: {money_returned}")
            elif money_returned < 0:
                st.error(f"You incurred a loss: {money_returned}")
            else:
                st.warning(f"No gains or losses: {money_returned}")

# Run the chatbot
financial_questions_chatbot()
