# -*- coding: utf-8 -*-
"""myapp

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DMrc2g2I1mwEwi5tjkUE0K-xJastywD2
"""



# Import necessary libraries
import yfinance as yf
import streamlit as st
import pandas as pd

# Display the title and description of the app
st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Display the closing price chart
st.line_chart(tickerDF.Close)

# Display the volume chart
st.line_chart(tickerDF.Volume)

