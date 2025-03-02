import streamlit as st
import yfinance as yf
import pandas as pd

@st.cache_data
def load_stock_prices(tickers, start_date, end_date):
    data = yf.download(tickers, 
                       start=start_date, 
                       end=end_date)['Close']
    return data


# Title
st.subheader("Personal Project Example")
st.subheader("KAIST Computer Programming in Finance 2025", divider="gray")
st.title("Portfolio Dashboard")

# Sidebar Inputs
tickers = st.sidebar.multiselect(
    "Enter Stock Tickers",
    ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", 
     "META", "TSLA", "TSM", "BRK-A", "AVGO"],
    ["AAPL", "NVDA"],
)
start_date = st.sidebar.date_input("Start Date", 
                                   pd.to_datetime("2025-01-01"))
end_date = st.sidebar.date_input("End Date", 
                                 pd.to_datetime("2025-12-31"))

normalize = st.sidebar.checkbox("Normalize?")

if st.sidebar.button("Fetch Portfolio Data"):
    data = load_stock_prices(tickers, start_date, end_date)
    
    if normalize:
        data /= data.iloc[0]
    st.write("### Portfolio Stock Prices")
    st.line_chart(data)
    
    st.write("### Correlation Matrix")
    st.dataframe(data.pct_change().corr())
    
