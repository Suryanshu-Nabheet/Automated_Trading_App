import requests
from textblob import TextBlob

def fetch_news(stock_symbol):
    url = f'https://newsapi.org/v2/everything?q={stock_symbol}&apiKey=your_api_key'
    response = requests.get(url)
    news_data = response.json()
    return news_data['articles']

def analyze_sentiment(news_articles):
    sentiments = []
    for article in news_articles:
        text = article['title'] + " " + article['description']
        sentiment = TextBlob(text).sentiment.polarity
        sentiments.append(sentiment)
    return sum(sentiments) / len(sentiments)  # average sentiment score