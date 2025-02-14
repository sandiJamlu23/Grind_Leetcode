import requests
from bs4 import BeautifulSoup
import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'][0]
    return price

# Example usage
ticker = 'KLBF.JK'
print(f"The current stock price of {ticker} is: {get_stock_data(ticker)}")