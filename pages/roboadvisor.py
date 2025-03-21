import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Function to determine risk profile
def risk_profile(age, risk_tolerance):
    if age < 35:
        return 'Aggressive' if risk_tolerance == 'High' else 'Moderate' if risk_tolerance == 'Moderate' else 'Conservative'
    elif 35 <= age < 50:
        return 'Moderately Aggressive' if risk_tolerance == 'High' else 'Moderate' if risk_tolerance == 'Moderate' else 'Moderately Conservative'
    else:
        return 'Moderate' if risk_tolerance == 'High' else 'Moderately Conservative' if risk_tolerance == 'Moderate' else 'Conservative'

# Function to suggest portfolio allocation
def suggest_portfolio(risk_profile):
    allocations = {
        'Aggressive': {'Stocks': 0.80, 'Bonds': 0.15, 'Cash': 0.05},
        'Moderately Aggressive': {'Stocks': 0.70, 'Bonds': 0.20, 'Cash': 0.10},
        'Moderate': {'Stocks': 0.60, 'Bonds': 0.30, 'Cash': 0.10},
        'Moderately Conservative': {'Stocks': 0.50, 'Bonds': 0.40, 'Cash': 0.10},
        'Conservative': {'Stocks': 0.40, 'Bonds': 0.50, 'Cash': 0.10},
    }
    return allocations.get(risk_profile, {})

# Fetch historical data safely
def get_historical_data(tickers, period="1y"):
    if not tickers:
        return None
    data = yf.download(tickers, period=period)
    
    if 'Adj Close' in data.columns:
        return data['Adj Close']
    else:
        return None  # Return None if data format is unexpected

# Streamlit app
st.title("Enhanced Robo-Advisor with Real-time Data")

# User authentication
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False

if not st.session_state['user_logged_in']:
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        st.session_state['user_logged_in'] = True

if st.session_state['user_logged_in']:
    # User inputs
    age = st.number_input("Enter your age:", min_value=18, max_value=100, value=30)
    risk_tolerance = st.selectbox("Select your risk tolerance:", ['High', 'Moderate', 'Low'])
    investment_amount = st.number_input("Enter your investment amount ($):", min_value=1000, value=10000)

    # Determine risk profile and suggest allocation
    profile = risk_profile(age, risk_tolerance)
    st.write(f"Your risk profile: **{profile}**")
    portfolio = suggest_portfolio(profile)

    # Display allocation
    st.write("Suggested Portfolio Allocation:")
    st.write(pd.DataFrame.from_dict(portfolio, orient='index', columns=['Allocation']).style.format("{:.0%}"))

    # Fetch historical data
    stock_tickers = ['AAPL', 'MSFT', 'GOOGL']
    bond_tickers = ['BND', 'AGG']
    tickers = stock_tickers + bond_tickers

    historical_data = get_historical_data(tickers)

    if historical_data is not None:
        # Display historical performance
        st.write("Historical Performance:")
        fig = px.line(historical_data, title="Stock and Bond Price History")
        st.plotly_chart(fig)
    else:
        st.write("No historical data available for selected tickers.")
else:
    st.write("Please log in to access your dashboard.")
