import datetime
import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Sharpe Ratio Analysis", page_icon="🏆", layout="wide")
st.title("Portfolio Risk & Sharpe Ratio Analysis")

col1, col2 = st.columns([2, 1])

with col1:
    stockslist = st.multiselect(
        "Select Assets for Risk Profiling", 
        options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V",
                  "UNH", "INTC", "AMD", "CRM", "BAC", "GS", "MS", "BLK", "AXP", "JNJ", 
                  "PFE", "ABBV", "MRK", "XOM", "CVX", "COP", "MCD", "KO", "PG", "WMT", 
                  "NKE", "CAT", "BA", "HON"], 
        default=["AAPL", "MSFT", "NVDA"]
    )
with col2:
    rf_rate = st.number_input("Risk-Free Rate (%) (e.g., US 10Y Treasury)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)

if stockslist:
    end = datetime.date.today()
    start = datetime.date(end.year - 3, end.month, end.day) # 3 Year lookback window for stable metrics
    
    # Fetch Data
    raw_data = yf.download(stockslist, start=start, end=end)['Close']
    if isinstance(raw_data.columns, pd.MultiIndex):
        raw_data.columns = raw_data.columns.get_level_values(1)
        
    # Calculate daily returns
    returns_df = raw_data.pct_change().dropna()
    
    sharpe_data = []
    
    for stock in stockslist:
        # Annualized Return formula (252 trading days)
        mean_return = returns_df[stock].mean() * 252
        # Annualized Volatility (Standard Deviation scaled to 252 days)
        annualized_vol = returns_df[stock].std() * np.sqrt(252)
        
        # Sharpe Ratio = (Expected Return - Risk Free Rate) / Volatility
        rf_decimal = rf_rate / 100
        sharpe_ratio = (mean_return - rf_decimal) / annualized_vol
        
        sharpe_data.append({
            "Asset": stock,
            "Annualized Return (%)": round(mean_return * 100, 2),
            "Annualized Volatility (%)": round(annualized_vol * 100, 2),
            "Sharpe Ratio": round(sharpe_ratio, 2)
        })
        
    summary_df = pd.DataFrame(sharpe_data)
    
    # Display Metrics Table
    st.markdown("### Risk-Adjusted Return Metrics Table")
    st.dataframe(summary_df, use_container_width=True)
    
    # Plotly Bar Chart for Visual Comparison
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=summary_df["Asset"],
        y=summary_df["Sharpe Ratio"],
        marker_color=['#22c55e' if x > 1 else '#ef4444' for x in summary_df["Sharpe Ratio"]],
        text=summary_df["Sharpe Ratio"],
        textposition='auto'
    ))
    
    fig.update_layout(
        title="Sharpe Ratio Comparison (Higher = Better Risk-Adjusted Performance)",
        xaxis_title="Assets",
        yaxis_title="Sharpe Ratio Value",
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please pick at least one asset to generate risk calculations.")