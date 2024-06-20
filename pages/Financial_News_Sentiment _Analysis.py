import streamlit as st
import requests
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import time

# Function to fetch financial news related to a given ticker symbol
def fetch_financial_news(api_key, ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={api_key}&language=en&pageSize=10"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles
    else:
        st.error("Failed to fetch news. Please check your API key or try again later.")
        return []

# Function to perform sentiment analysis on news articles
def analyze_sentiment(article):
    text = article['title'] + '. ' + article['description']
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Function to display buy or sell recommendations based on sentiment analysis
def display_recommendations(ticker, articles):
    st.title(f"Recommendations for {ticker}")

    if not articles:
        st.warning("No financial news articles found for the given ticker.")
        return

    # Analyzing sentiment for each article
    sentiments = [analyze_sentiment(article) for article in articles]
    avg_sentiment = sum(sentiments) / len(sentiments)

    # Displaying recommendations based on average sentiment
    if avg_sentiment > 0:
        st.success("Based on the financial news sentiment analysis, it's recommended to BUY.")
    elif avg_sentiment < 0:
        st.error("Based on the financial news sentiment analysis, it's recommended to SELL.")
    else:
        st.warning("The sentiment analysis did not yield a clear recommendation.")

    st.subheader("Financial News:")
    # Displaying articles and their sentiment scores
    articles_data = []
    for article, sentiment in zip(articles, sentiments):
        articles_data.append({
            'Title': article['title'],
            'Description': article['description'],
            'Source': article['source']['name'],
            'Published At': article['publishedAt'],
            'Sentiment Score': sentiment
        })

    df_articles = pd.DataFrame(articles_data)
    st.dataframe(df_articles)

    # Plotting sentiment over time
    if len(articles) > 1:
        df_articles['Date'] = pd.to_datetime(df_articles['Published At'])
        df_articles.set_index('Date', inplace=True)
        df_articles['Sentiment'] = sentiments
        fig, ax = plt.subplots()
        df_articles['Sentiment'].plot(ax=ax, marker='o')
        ax.set_title('Sentiment Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Sentiment Score')
        st.pyplot(fig)

    # Provide download link for the CSV file
    csv = df_articles.to_csv(index=False)
    st.download_button("Download data as CSV", csv, "articles_data.csv", "text/csv")

# Main function to run the app
def main():
    st.set_page_config(page_title="Stock Analysis App")
    st.title("Financial News Sentiment Analysis")
    st.write("This app fetches financial news related to a given stock ticker and provides buy or sell recommendations based on sentiment analysis of the news.")

    api_key = st.text_input("Enter your News API key:")
    ticker = st.text_input("Enter the ticker symbol of the stock:")

    if st.button("Get Recommendations"):
        if not api_key or not ticker:
            st.warning("Please enter both your News API key and ticker symbol.")
        else:
            articles = fetch_financial_news(api_key, ticker)
            display_recommendations(ticker, articles)

if __name__ == "__main__":
    main()
