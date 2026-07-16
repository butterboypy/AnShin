# importing libraries
import datetime
import streamlit as st
import pandas as pd
import yfinance as yf 
import plotly.graph_objects as go
import ta
from pages.utils.plotly_figure import plotly_table

# setting page config
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("Stock Analysis")

col1, col2, col3 = st.columns(3)
today = datetime.date.today()

with col1:
    stockslist = st.selectbox("Select stock to analyze", 
                            options= ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V",
                                      "UNH", "INTC", "AMD", "CRM", "BAC", "GS", "MS", "BLK", "AXP", "JNJ", 
                                      "PFE", "ABBV", "MRK", "XOM", "CVX", "COP", "MCD", "KO", "PG", "WMT", 
                                      "NKE", "CAT", "BA", "HON"], 
                            index=0)
    ticker = stockslist
with col2:
    start_date = st.date_input("Choose Start Date", datetime.date(today.year - 1, today.month, today.day))
with col3:
    end_date = st.date_input("Choose End Date", today)

st.subheader(ticker)

stock = yf.Ticker(ticker)

st.write("**Description:** " + stock.info.get("longBusinessSummary", "N/A"))
st.write("**Sector:** " + stock.info.get("sector", "N/A"))
st.write("**Full Time Employees:** " + str(stock.info.get("fullTimeEmployees", "N/A")))
st.write("**Website:** " + stock.info.get("website", "N/A"))

col1, col2 = st.columns(2)

with col1:
    # 1. Clean, ordered list of financial labels
    metrics_index = ['Market Cap', 'Beta', 'EPS', 'PE Ratio']
    info = stock.info
    
    # 2. Extract values safely from the yfinance info dictionary
    market_cap = f"<b>${info.get('marketCap', 0):,}</b>"
    beta_val   = f"<b>{round(info.get('beta', 0), 2)}</b>"
    eps        = f"<b>${round(info.get('trailingEps', 0), 2)}</b>"
    pe_ratio   = f"<b>{round(info.get('trailingPE', 0), 2)}</b>"

    # 3. Create DataFrame cleanly with columns specified upfront (skips reset_index bugs)
    df1_clean = pd.DataFrame({
        'METRICS': [f"<b>{m}</b>" for m in metrics_index],
        'VALUES': [market_cap, beta_val, eps, pe_ratio]
    })
    
    # 4. Pass the clean two-column DataFrame into your custom layout engine
    fig_df1 = plotly_table(df1_clean)
    st.plotly_chart(fig_df1, use_container_width=True)

with col2:
    # 1. Clean, ordered list of financial labels for table 2
    metrics_index_2 = ['Quick Ratio', 'Revenue per Share', 'Profit Margins', 'Debt to Equity', 'Return on Equity']
    
    # 2. Extract values safely from the yfinance info dictionary
    quick_ratio = f"<b>{round(info.get('quickRatio', 0), 2)}</b>"
    rev_per_share = f"<b>${info.get('revenuePerShare', 0):,}</b>"
    profit_margins = f"<b>{round(info.get('profitMargins', 0), 2)}</b>"
    debt_to_equity = f"<b>{round(info.get('debtToEquity', 0), 2)}</b>"
    roe = f"<b>{round(info.get('returnOnEquity', 0), 2)}</b>"

    # 3. Create DataFrame cleanly with columns specified upfront (skips reset_index bugs)
    df2_clean = pd.DataFrame({
        'METRICS': [f"<b>{m}</b>" for m in metrics_index_2],
        'VALUES': [quick_ratio, rev_per_share, profit_margins, debt_to_equity, roe]
    })
    
    # 4. Pass the clean two-column DataFrame into your custom layout engine
    fig_df2 = plotly_table(df2_clean)
    st.plotly_chart(fig_df2, use_container_width=True)

# =====================================================================
# UPGRADED FINANCIAL METRIC CARDS SECTION
# =====================================================================
st.markdown("### Daily Performance Metrics")

current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
prior_close   = info.get('regularMarketPreviousClose', 0)

daily_change = current_price - prior_close
pct_change   = (daily_change / prior_close) * 100 if prior_close != 0 else 0

card_cols = st.columns(3)

with card_cols[0]:
    st.metric(
        label=f"Daily Change ({ticker})",
        value=f"${current_price:,.2f}",
        delta=f"${daily_change:,.2f} ({pct_change:.2f}%)"
    )

with card_cols[1]:
    st.metric(
        label="Previous Close",
        value=f"${prior_close:,.2f}"
    )

with card_cols[2]:
    day_low  = info.get('dayLow', 0)
    day_high = info.get('dayHigh', 0)
    st.metric(
        label="Day's Range",
        value=f"${day_low:,.2f} - ${day_high:,.2f}"
    )

# Last 10 Days Section
last_10_df = stock.history(period="10d").sort_index(ascending=False).round(3)
columns_to_keep = ['Open', 'High', 'Low', 'Close', 'Volume']
last_10_filtered = last_10_df[columns_to_keep].reset_index()
last_10_filtered['Date'] = last_10_filtered['Date'].dt.strftime('%Y-%m-%d')

fig_last_10 = plotly_table(last_10_filtered[['Date'] + columns_to_keep])
st.write("### Last 10 Days Closing Price")
st.plotly_chart(fig_last_10, use_container_width=True)

# BUTTONS & CHARTS TECHNICAL ANALYSIS SECTION
from pages.utils.plotly_figure import candlestick, RSI, MACD, close_chart, Moving_average

if "num_period" not in st.session_state:
    st.session_state.num_period = "1y"

time_cols = st.columns([1,1,1,1,1,1,1,1,1,8], gap='small')

with time_cols[0]:
    if st.button('1D'): st.session_state.num_period = '1d'
with time_cols[1]:
    if st.button('5D'): st.session_state.num_period = '5d'
with time_cols[2]:
    if st.button('15D'): st.session_state.num_period = '15d'
with time_cols[3]:
    if st.button('1M'): st.session_state.num_period = '1mo'
with time_cols[4]:
    if st.button('6M'): st.session_state.num_period = '6mo'
with time_cols[5]:
    if st.button('1Y'): st.session_state.num_period = '1y'
with time_cols[6]:
    if st.button('5Y'): st.session_state.num_period = '5y'
with time_cols[7]:
    if st.button('10Y'): st.session_state.num_period = '10y'
with time_cols[8]:
    if st.button('YTD'): st.session_state.num_period = 'ytd'
with time_cols[9]:
    if st.button('MAX'): st.session_state.num_period = ''

num_period = st.session_state.num_period

select_cols = st.columns([1, 1, 4])
with select_cols[0]:
    chart_type = st.selectbox('Chart Type', ('Candle', 'Line'), key="chart_type_select")
with select_cols[1]:
    if chart_type == 'Candle':
        indicators = st.selectbox('Indicator', ('RSI', 'MACD'), key="indicator_candle_select")
    else:
        indicators = st.selectbox('Indicator', ('RSI', 'Moving Average', 'MACD'), key="indicator_line_select")    

# Dynamically links charts to your active selectbox ticker asset seamlessly
data1 = stock.history(period='max')

if data1.empty:
    st.error(f"No active data found for stock ticker symbol target '{ticker}'. Please verify connectivity parameters.")
else:
    # Standard fallback validation formatting maps selected intervals accurately
    active_period = num_period
    
    if chart_type == 'Candle' and indicators == 'RSI':
        st.plotly_chart(candlestick(data1, active_period), use_container_width=True)
        st.plotly_chart(RSI(data1, active_period), use_container_width=True)
    elif chart_type == 'Candle' and indicators == 'MACD':
        st.plotly_chart(candlestick(data1, active_period), use_container_width=True)
        st.plotly_chart(MACD(data1, active_period), use_container_width=True)
    elif chart_type == 'Line' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1, active_period), use_container_width=True)
        st.plotly_chart(RSI(data1, active_period), use_container_width=True)
    elif chart_type == 'Line' and indicators == 'Moving Average':
        st.plotly_chart(Moving_average(data1, active_period), use_container_width=True)
    elif chart_type == 'Line' and indicators == 'MACD':
        st.plotly_chart(close_chart(data1, active_period), use_container_width=True)
        st.plotly_chart(MACD(data1, active_period), use_container_width=True)