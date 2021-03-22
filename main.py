import yfinance as yf

import streamlit as st

import pandas as pd

st.write("# Simple Stock Price")

st.write("Shown are the stock closing price and volumn of Google!")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-2-16')

st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)