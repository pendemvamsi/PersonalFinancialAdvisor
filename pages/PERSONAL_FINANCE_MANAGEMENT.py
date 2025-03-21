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
    # Calculate the percentage change in stock price
    stock_data['Price_Change'] = stock_data['Close'].pct_change()
    # Calculate the total return based on the investment
    total_return = (stock_data['Price_Change'] * investment_in_stocks).sum()
    return total_return

# Function to calculate moving average
def moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

# Function to interactively gather financial information from the user
def financial_questions_chatbot():
    st.title("PERSONAL_FINANCE_MANAGEMENT")
    st.write("MONTHLY BUDGET MANAGEMENT")
    st.write("Efficient monthly budget management is key to financial stability, ensuring expenses align with income while leaving room for saving and investing. By diligently tracking spending and income, individuals can make informed decisions to optimize their finances and achieve their financial goals.")

    # Get user input
    symbol = st.text_input("Enter the ticker symbol of the stock you're interested in (e.g., AAPL for Apple Inc.):")
    start_date = st.date_input("Enter the start date for retrieving stock data:")
    end_date = st.date_input("Enter the end date for retrieving stock data:")
    net_income = st.number_input("What is your net fixed income per month?", min_value=0)
    transportation_costs = st.number_input("How much do you spend on transportation per month?", min_value=0)
    food_costs = st.number_input("How much do you spend on food per month?", min_value=0)
    outing_expenses = st.number_input("How much do you spend on outings per month?", min_value=0)
    other_fixed_costs = st.number_input("What are your other fixed costs per month?", min_value=0)
    has_variable_costs = st.radio("Do you have any variable costs this year?", ("Yes", "No"))

    if has_variable_costs == "Yes":
        st.write("Please provide variable costs for each month:")
        variable_costs = {}
        for month in range(1, 13):
            cost = st.number_input(f"Variable costs for month {month}:", min_value=0)
            variable_costs[f"Month {month}"] = cost
    else:
        variable_costs = None

    available_savings = st.number_input("How much available savings do you have?", min_value=0)

    # Calculate total expenses
    total_expenses = transportation_costs + food_costs + outing_expenses + other_fixed_costs
    if variable_costs:
        total_expenses += sum(variable_costs.values())

    # Calculate savings
    savings = available_savings + net_income - total_expenses

    # Calculate investment in stocks
    investment_in_stocks = savings * 0.20  # 20% of savings

    # Display user's inputs and savings
    st.write("Summary of Your Inputs:")
    st.write(f"Stock Symbol: {symbol}")
    st.write(f"Start Date: {start_date}")
    st.write(f"End Date: {end_date}")
    st.write(f"Net Fixed Income per Month: {net_income}")
    st.write(f"Transportation Costs per Month: {transportation_costs}")
    st.write(f"Food Costs per Month: {food_costs}")
    st.write(f"Outing Expenses per Month: {outing_expenses}")
    st.write(f"Other Fixed Costs per Month: {other_fixed_costs}")
    st.write(f"Variable Costs per Month: {variable_costs}")
    st.write(f"Available Savings: {available_savings}")

    # Provide feedback on savings and investment recommendation
    if savings > 0:
        st.success("Congratulations! You have positive savings.")
        st.write(f"Your savings for the month: {savings}")
        st.write(f"Recommended investment in stocks (20% of savings): {investment_in_stocks}")
        st.write("Keep up the good work!")
    elif savings < 0:
        st.error("Oops! Your expenses exceed your income.")
        st.write(f"Your deficit for the month: {-savings}")
        st.write("Consider reducing expenses or increasing income.")
    else:
        st.warning("Your income equals your expenses.")
        st.write("Consider saving some money for the future.")

    # Pie chart for expense breakdown
    if total_expenses > 0:
        expenses_labels = ['Transportation', 'Food', 'Outings', 'Other Fixed', 'Variable']
        expenses_values = [transportation_costs, food_costs, outing_expenses, other_fixed_costs, sum(variable_costs.values()) if variable_costs else 0]

        fig, ax = plt.pyplot()
        ax.pie(expenses_values, labels=expenses_labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

    # Fetch real-time stock data and provide investment recommendation
    if symbol:
        st.write("Fetching real-time stock data...")
        stock_data = get_stock_data(symbol, start_date, end_date)

        if not stock_data.empty:
            st.write("Real-time Stock Data:")
            st.write(stock_data.head())

            # Line chart for savings over time
            st.subheader('Savings Over Time')
            savings_over_time = np.cumsum(stock_data['Close'].pct_change() * investment_in_stocks)
            plt.figure(figsize=(10, 5))
            plt.plot(savings_over_time, label='Cumulative Savings')
            plt.title('Cumulative Savings Over Time')
            plt.xlabel('Days')
            plt.ylabel('Cumulative Savings')
            plt.legend()
            st.pyplot()

            # Histogram for investment returns
            st.subheader('Investment Returns Distribution')
            returns = stock_data['Close'].pct_change() * investment_in_stocks
            plt.figure(figsize=(10, 5))
            plt.hist(returns.dropna(), bins=30, alpha=0.75, label='Returns')
            plt.title('Investment Returns Distribution')
            plt.xlabel('Return Amount')
            plt.ylabel('Frequency')
            plt.legend()
            st.pyplot()

            # Moving average plot for stock prices
            st.subheader('Stock Price Moving Average')
            stock_data['50_MA'] = moving_average(stock_data, 50)
            plt.figure(figsize=(10, 5))
            plt.plot(stock_data['Close'], label='Close Price')
            plt.plot(stock_data['50_MA'], label='50-Day Moving Average', color='orange')
            plt.title('Stock Price and 50-Day Moving Average')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            st.pyplot()

            # Predict the amount of money returned to the user after retrieving from stocks
            st.write("Predicting the amount of money returned to the user...")
            money_returned = predict_money_returned(stock_data, investment_in_stocks)

            # Indicate profit or loss
            if money_returned > 0:
                st.success(f"Predicted money returned to the user after retrieving from stocks: {money_returned}")
                st.write("Congratulations! You made a profit.")
            elif money_returned < 0:
                st.error(f"Predicted money returned to the user after retrieving from stocks: {money_returned}")
                st.write("Oops! You incurred a loss.")
            else:
                st.warning(f"Predicted money returned to the user after retrieving from stocks: {money_returned}")
                st.write("You neither gained nor lost any money.")

# Run the chatbot
financial_questions_chatbot()
