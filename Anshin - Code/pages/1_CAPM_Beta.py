import datetime
import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="CAPM Beta",
    page_icon="📊",
    layout="wide"
)

st.title("Calculate Beta and Return for individual stock")

# 2. Layout Columns for Inputs
col1, col2 = st.columns([1, 1])

with col1:
    ticker = st.selectbox(
        "Choose a stock", 
        options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V",
                 "UNH", "INTC", "AMD", "CRM", "BAC", "GS", "MS", "BLK", "AXP", "JNJ", 
                 "PFE", "ABBV", "MRK", "XOM", "CVX", "COP", "MCD", "KO", "PG", "WMT", 
                 "NKE", "CAT", "BA", "HON"],
        index=5  # Defaults to TSLA to match your image reference
    )

with col2:
    years = st.number_input("Number of Years", min_value=1, max_value=10, value=1)

# 3. Fetching Historical Data
try:
    end_date = datetime.date.today()
    start_date = datetime.date(end_date.year - years, end_date.month, end_date.day)

    # Download Market Benchmark (^GSPC is the S&P 500 ticker) and Asset Data
    with st.spinner("Fetching market data..."):
        market_raw = yf.download('^GSPC', start=start_date, end=end_date)
        stock_raw = yf.download(ticker, start=start_date, end=end_date)

    # Handle yfinance MultiIndex columns if present
    if isinstance(market_raw.columns, pd.MultiIndex):
        market_close = market_raw['Close']['^GSPC']
        stock_close = stock_raw['Close'][ticker]
    else:
        market_close = market_raw['Close']
        stock_close = stock_raw['Close']

    # 4. Process Daily Returns
    df = pd.DataFrame({
        'Market_Close': market_close,
        'Stock_Close': stock_close
    }).dropna()

    df['Market_Return'] = df['Market_Close'].pct_change()
    df['Stock_Return'] = df['Stock_Close'].pct_change()
    df = df.dropna()

    # 5. Math Engine: Calculate Beta (Covariance / Variance)
    covariance_matrix = np.cov(df['Stock_Return'], df['Market_Return'])
    covariance = covariance_matrix[0, 1]
    market_variance = covariance_matrix[1, 1]
    
    beta_value = covariance / market_variance

    # Calculate CAPM Expected Return
    # Standardizing: Risk-Free Rate = 0%, Market Return = annualized mean of historical range
    rf = 0.0
    rm = df['Market_Return'].mean() * 252  # Annualized average market return
    expected_return = rf + (beta_value * (rm - rf))

    # Convert expected return to a clean percentage scale 
    expected_return_pct = expected_return * 100

    # 6. Display Values (Matching Your Target Layout)
    st.markdown(f"### **Beta : {beta_value:.14f}**")
    st.markdown(f"### **Return : {expected_return_pct:.2f}**")

    # 7. Chart Engine: Interactive Scatter Plot with Line of Best Fit
    st.subheader(ticker)

#     # Compute coordinates for the trend line (Line of Best Fit)
#     # Equation: y = alpha + beta * x
#     alpha = df['Stock_Return'].mean() - (beta_value * df['Market_Return'].mean())
#     x_line = np.linspace(df['Market_Return'].min(), df['Market_Return'].max(), 100)
#     y_line = alpha + beta_value * x_line

#     fig = go.Figure()

#     # Add historical daily data points
#     fig.add_trace(go.Scatter(
#         x=df['Market_Return'],
#         y=df['Stock_Return'],
#         mode='markers',
#         name='Daily Returns',
#         marker=dict(color='#5ab7ff', size=6, opacity=0.7)
#     ))

#     # Add Trend Line
#     fig.add_trace(go.Scatter(
#         x=x_line,
#         y=y_line,
#         mode='lines',
#         name='Trend Line (Beta)',
#         line=dict(color='crimson', width=2)
#     ))

#     # Layout Customization
#     fig.update_layout(
#         xaxis_title="S&P 500 Daily Returns (Market)",
#         yaxis_title=f"{ticker} Daily Returns",
#         height=500,
#         plot_bgcolor='rgba(30, 30, 40, 0.2)',  # Clean dark-mode friendly charting grid
#         margin=dict(l=40, r=20, t=20, b=40),
#         legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
#     )

#     st.plotly_chart(fig, use_container_width=True)

# Re-calculate coordinates for the trend line (Line of Best Fit)
    alpha = df['Stock_Return'].mean() - (beta_value * df['Market_Return'].mean())
    x_line = np.linspace(df['Market_Return'].min(), df['Market_Return'].max(), 100)
    y_line = alpha + beta_value * x_line

# === UPDATED CHART ENGINE: DARK THEME WITH CUSTOM TRACE COLORS ===
    fig = go.Figure()

    # Add historical daily data points (Changed to Green)
    fig.add_trace(go.Scatter(
        x=df['Market_Return'],
        y=df['Stock_Return'],
        mode='markers',
        name='Daily Returns',
        marker=dict(color="#1480fc", size=8, opacity=0.8) # Vibrant green dots
    ))

    # Add Trend Line (Changed to White)
    fig.add_trace(go.Scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        name='Trend Line (Beta)',
        line=dict(color="#c8c8c8", width=2) # Stark white trend line
    ))

    # Layout Customization (True Black Matte Theme)
    fig.update_layout(
        xaxis_title="S&P 500 Daily Returns (Market)",
        yaxis_title=f"{ticker} Daily Returns",
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#ffffff"), # Force all titles & tick marks to white
        xaxis=dict(gridcolor='rgba(0,0,0,0)', zerolinecolor='rgba(0,0,0,0)'),
        yaxis=dict(gridcolor='rgba(0,0,0,0)', zerolinecolor='rgba(0,0,0,0)'),
        margin=dict(l=40, r=20, t=20, b=40),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01, font=dict(color="white"))
    )

    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Could not calculate values for ticker symbol '{ticker}'. Error Details: {e}")