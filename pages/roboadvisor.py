import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import seaborn as sns
from sklearn.linear_model import LinearRegression
from textblob import TextBlob
from PIL import Image
import requests
from io import BytesIO
import time

# Function to determine risk profile
def risk_profile(age, risk_tolerance):
    if age < 35:
        if risk_tolerance == 'High':
            return 'Aggressive'
        elif risk_tolerance == 'Moderate':
            return 'Moderately Aggressive'
        else:
            return 'Moderate'
    elif 35 <= age < 50:
        if risk_tolerance == 'High':
            return 'Moderately Aggressive'
        elif risk_tolerance == 'Moderate':
            return 'Moderate'
        else:
            return 'Moderately Conservative'
    else:
        if risk_tolerance == 'High':
            return 'Moderate'
        elif risk_tolerance == 'Moderate':
            return 'Moderately Conservative'
        else:
            return 'Conservative'

# Function to suggest portfolio allocation
def suggest_portfolio(risk_profile):
    if risk_profile == 'Aggressive':
        return {'Stocks': 0.80, 'Bonds': 0.15, 'Cash': 0.05}
    elif risk_profile == 'Moderately Aggressive':
        return {'Stocks': 0.70, 'Bonds': 0.20, 'Cash': 0.10}
    elif risk_profile == 'Moderate':
        return {'Stocks': 0.60, 'Bonds': 0.30, 'Cash': 0.10}
    elif risk_profile == 'Moderately Conservative':
        return {'Stocks': 0.50, 'Bonds': 0.40, 'Cash': 0.10}
    else:
        return {'Stocks': 0.40, 'Bonds': 0.50, 'Cash': 0.10}

# Fetch real-time data using yfinance
def get_real_time_data(tickers):
    data = {}
    for ticker in tickers:
        stock_info = yf.Ticker(ticker)
        hist = stock_info.history(period="1d")
        if not hist.empty:
            data[ticker] = hist['Close'][0]
        else:
            data[ticker] = None  # Handle missing data
    return data

# Fetch historical data with error handling for missing 'Adj Close'
def get_historical_data(tickers, period="1y"):
    if not tickers:
        return None
    data = yf.download(tickers, period=period)
    # Handle multi-ticker downloads (MultiIndex columns)
    if isinstance(data.columns, pd.MultiIndex):
        if 'Adj Close' in data.columns.levels[0]:
            return data['Adj Close']
        else:
            st.warning("Adjusted Close data not found for tickers: " + ", ".join(tickers))
            return None
    else:
        if 'Adj Close' in data.columns:
            return data['Adj Close']
        else:
            st.warning("Adjusted Close data not found for tickers: " + ", ".join(tickers))
            return None

# Calculate additional financial metrics
def calculate_metrics(returns):
    mean_return = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = mean_return / volatility if volatility != 0 else 0  # Avoid division by zero
    return mean_return, volatility, sharpe_ratio

# Streamlit app
st.title("Enhanced Robo-Advisor with Real-time Data")

# User authentication (placeholder for actual implementation)
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False

if not st.session_state['user_logged_in']:
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        st.session_state['user_logged_in'] = True  # Placeholder for actual authentication

if st.session_state['user_logged_in']:
    # User inputs
    age = st.number_input("Enter your age:", min_value=18, max_value=100, value=30)
    risk_tolerance = st.selectbox("Select your risk tolerance:", ['High', 'Moderate', 'Low'])
    investment_amount = st.number_input("Enter your investment amount ($):", min_value=1000, value=10000)
    financial_goal = st.number_input("Enter your financial goal amount ($):", min_value=1000, value=50000)
    goal_years = st.number_input("Enter the number of years to achieve your goal:", min_value=1, max_value=50, value=10)

    # Determine risk profile
    profile = risk_profile(age, risk_tolerance)
    st.write(f"Based on your inputs, your risk profile is: **{profile}**")

    # Suggest portfolio allocation
    portfolio = suggest_portfolio(profile)
    st.write("Suggested Portfolio Allocation:")
    st.write(pd.DataFrame.from_dict(portfolio, orient='index', columns=['Allocation']).style.format("{:.0%}"))

    # Example tickers for a diversified portfolio
    default_stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    default_bond_tickers = ['BND', 'AGG']

    # Allow user to customize their portfolio
    st.write("Customize your portfolio:")
    stock_tickers = st.multiselect("Select your stocks:", default_stock_tickers, default=default_stock_tickers)
    bond_tickers = st.multiselect("Select your bonds:", default_bond_tickers, default=default_bond_tickers)

    # Get stock and bond prices
    stock_prices = get_real_time_data(stock_tickers)
    bond_prices = get_real_time_data(bond_tickers)

    # Calculate investment allocation
    investment_allocation = {}
    total_allocation = portfolio['Stocks'] + portfolio['Bonds']
    investment_allocation['Stocks'] = portfolio['Stocks'] * investment_amount / total_allocation
    investment_allocation['Bonds'] = portfolio['Bonds'] * investment_amount / total_allocation
    investment_allocation['Cash'] = portfolio['Cash'] * investment_amount

    # Detailed allocation
    detailed_allocation = {}

    # Distribute stock investments
    if stock_tickers:
        stock_investment_per_stock = investment_allocation['Stocks'] / len(stock_tickers)
        for ticker in stock_tickers:
            if stock_prices.get(ticker) is not None:
                detailed_allocation[ticker] = stock_investment_per_stock / stock_prices[ticker]
            else:
                detailed_allocation[ticker] = 0
    # Distribute bond investments
    if bond_tickers:
        bond_investment_per_bond = investment_allocation['Bonds'] / len(bond_tickers)
        for ticker in bond_tickers:
            if bond_prices.get(ticker) is not None:
                detailed_allocation[ticker] = bond_investment_per_bond / bond_prices[ticker]
            else:
                detailed_allocation[ticker] = 0

    # Combine detailed allocation
    detailed_allocation['Cash'] = investment_allocation['Cash']

    # Display investment allocation
    st.write("Detailed Investment Allocation:")
    detailed_allocation_df = pd.DataFrame.from_dict(detailed_allocation, orient='index', columns=['Shares'])
    st.write(detailed_allocation_df.style.format("{:.2f}"))

    # Display pie chart of portfolio allocation
    st.write("Portfolio Allocation Breakdown:")
    fig, ax = plt.subplots()
    pd.Series(portfolio).plot(kind='pie', autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)

    # Fetch historical data for performance analysis
    all_tickers = stock_tickers + bond_tickers
    historical_data = get_historical_data(all_tickers)

    portfolio_returns = None  # Initialize portfolio_returns
    if historical_data is not None:
        # Calculate portfolio historical performance
        weights = ([portfolio['Stocks'] / len(stock_tickers)] * len(stock_tickers)) + ([portfolio['Bonds'] / len(bond_tickers)] * len(bond_tickers))
        portfolio_returns = (historical_data * weights).sum(axis=1).pct_change().dropna()

        # Calculate financial metrics
        mean_return, volatility, sharpe_ratio = calculate_metrics(portfolio_returns)
        st.write(f"Mean Return: {mean_return:.2%}")
        st.write(f"Volatility: {volatility:.2%}")
        st.write(f"Sharpe Ratio: {sharpe_ratio:.2f}")

        # Display historical performance using Plotly
        st.write("Historical Performance:")
        fig = px.line(portfolio_returns.cumsum(), title="Portfolio Cumulative Returns")
        st.plotly_chart(fig)
    else:
        st.error("Historical data could not be retrieved. Please check the selected tickers.")

    # Only perform risk analysis if portfolio_returns is defined
    if portfolio_returns is not None:
        # Rebalancing Recommendations
        st.write("Rebalancing Recommendations:")
        current_allocations = {'Stocks': investment_allocation['Stocks'], 'Bonds': investment_allocation['Bonds'], 'Cash': investment_allocation['Cash']}
        for asset, allocation in portfolio.items():
            current_allocation = current_allocations[asset] / investment_amount
            if abs(current_allocation - allocation) > 0.05:  # if drift is more than 5%
                st.write(f"Consider rebalancing {asset}: Current allocation is {current_allocation:.2%}, Target is {allocation:.2%}")

        # Scenario Analysis
        st.write("Scenario Analysis:")
        market_change = st.slider("Market Change (%)", -50, 50, 0)
        new_prices = {ticker: price * (1 + market_change / 100) for ticker, price in stock_prices.items() if price is not None}
        new_detailed_allocation = {ticker: (investment_allocation['Stocks'] / len(stock_tickers)) / new_prices[ticker] for ticker in stock_tickers if ticker in new_prices}
        new_allocation_df = pd.DataFrame.from_dict(new_detailed_allocation, orient='index', columns=['Shares'])
        st.write(f"New Allocation if market changes by {market_change}%:")
        st.write(new_allocation_df.style.format("{:.2f}"))

        # Risk Profile Analysis based on portfolio_returns
        if profile == 'Aggressive':
            st.write("Aggressive Risk Profile Analysis:")
            st.write("This profile focuses on high growth with significant volatility. Suitable for younger investors with a longer time horizon.")
            max_drawdown = (portfolio_returns.cumsum().max() - portfolio_returns.cumsum().min()) / portfolio_returns.cumsum().max()
            st.write(f"Max Drawdown: {max_drawdown:.2f}")
            st.write(f"Annualized Volatility: {portfolio_returns.std() * np.sqrt(252):.2f}")
        elif profile == 'Moderately Aggressive':
            st.write("Moderately Aggressive Risk Profile Analysis:")
            st.write("This profile aims for growth with moderate volatility. Suitable for investors who can tolerate some market fluctuations.")
            max_drawdown = (portfolio_returns.cumsum().max() - portfolio_returns.cumsum().min()) / portfolio_returns.cumsum().max()
            st.write(f"Max Drawdown: {max_drawdown:.2f}")
            st.write(f"Annualized Volatility: {portfolio_returns.std() * np.sqrt(252):.2f}")
        elif profile == 'Moderate':
            st.write("Moderate Risk Profile Analysis:")
            st.write("This profile balances growth and income with moderate volatility. Suitable for investors with a balanced risk tolerance.")
            max_drawdown = (portfolio_returns.cumsum().max() - portfolio_returns.cumsum().min()) / portfolio_returns.cumsum().max()
            st.write(f"Max Drawdown: {max_drawdown:.2f}")
            st.write(f"Annualized Volatility: {portfolio_returns.std() * np.sqrt(252):.2f}")
        elif profile == 'Moderately Conservative':
            st.write("Moderately Conservative Risk Profile Analysis:")
            st.write("This profile focuses on income with low to moderate volatility. Suitable for investors who prefer stable returns.")
            max_drawdown = (portfolio_returns.cumsum().max() - portfolio_returns.cumsum().min()) / portfolio_returns.cumsum().max()
            st.write(f"Max Drawdown: {max_drawdown:.2f}")
            st.write(f"Annualized Volatility: {portfolio_returns.std() * np.sqrt(252):.2f}")
        else:
            st.write("Conservative Risk Profile Analysis:")
            st.write("This profile focuses on capital preservation with minimal volatility. Suitable for older investors or those with low risk tolerance.")
            max_drawdown = (portfolio_returns.cumsum().max() - portfolio_returns.cumsum().min()) / portfolio_returns.cumsum().max()
            st.write(f"Max Drawdown: {max_drawdown:.2f}")
            st.write(f"Annualized Volatility: {portfolio_returns.std() * np.sqrt(252):.2f}")

        # Investment Goals and Planning
        st.write("Investment Goals and Planning:")
        target_return = (financial_goal / investment_amount) ** (1 / goal_years) - 1
        st.write(f"To achieve your goal of ${financial_goal} in {goal_years} years, your portfolio needs to achieve an annual return of {target_return:.2%}.")

        # Monte Carlo simulation for future portfolio value projection
        st.write("Monte Carlo Simulation:")
        simulations = 1000
        future_values = []
        for _ in range(simulations):
            simulated_returns = np.random.normal(mean_return / 252, volatility / np.sqrt(252), 252 * goal_years)
            future_values.append(investment_amount * np.prod(1 + simulated_returns))
        future_values = np.array(future_values)
        fig = px.histogram(future_values, nbins=50, title="Distribution of Future Portfolio Values")
        st.plotly_chart(fig)
        st.write(f"Based on the Monte Carlo simulation, there is a {np.mean(future_values >= financial_goal):.2%} chance of achieving your financial goal.")
else:
    st.write("Please log in to access your personalized robo-advisor dashboard.")
