# Importing the required libraries; The explanation for each library is given in the requirements.txt file
import streamlit as st
import yfinance as yf
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import plotly.express as px
import pandas as pd


crypto_mapping = {"Bitcoin": "BTC-USD", "Ethereum": "ETH-USD", "DogeCoin":"DOGE-USD"}


# This is the title of the plot
st.title("Crypto Tracker")
crypto_option = st.sidebar.selectbox("About which Cryptocurrency do you want to visualize and see the plot?", ("Bitcoin", "Ethereum","DogeCoin"))

# We will be specifying the start and the end date
start_date = st.sidebar.date_input("Start Date", date.today() - relativedelta(months=1))
end_date = st.sidebar.date_input("End Date", date.today())


# Specifying the data interval for which you want to visualize the plots
data_interval = st.sidebar.selectbox(
    "Data Interval",
    ("1m","2m","5m","15m","30m","60m","90m","1h","1d","5d","1wk","1mo","3mo",),
)

symbol_crypto = crypto_mapping[crypto_option]
data_crypto = yf.Ticker(symbol_crypto)


# Specifying the Value selectors
value_selector = st.sidebar.selectbox("Value Selector", ("Open", "High", "Low", "Close", "Volume"))

if st.sidebar.button("Generate"):
    crypto_hist = data_crypto.history(start=start_date, end=end_date, interval=data_interval)
    fig = px.line(crypto_hist, x=crypto_hist.index, y=value_selector,labels={"x": "Date"})
    st.plotly_chart(fig)
