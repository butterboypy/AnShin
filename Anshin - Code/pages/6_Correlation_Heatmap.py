import datetime
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="Correlation Heatmap", page_icon="🔥", layout="wide")
st.title("Asset Correlation Matrix")
st.caption("Tracks how tightly asset prices move in tandem. Values close to 1 mean locked directional movement, while values near 0 show strong diversification potential.")

# Wide default pool to get a beautiful variance map out-of-the-box
default_basket = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "JPM", "XOM", "KO", "PG"]

stockslist = st.multiselect(
    "Modify Heatmap Asset Basket Selection", 
    options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", 
             "V", "UNH", "INTC", "AMD", "CRM", "BAC", "GS", "MS", "BLK", "AXP", "JNJ", 
             "PFE", "ABBV", "MRK", "XOM", "CVX", "COP", "MCD", "KO", "PG", "WMT", 
             "NKE", "CAT", "BA", "HON"], 
    default=default_basket
)

if len(stockslist) > 1:
    end = datetime.date.today()
    start = datetime.date(end.year - 2, end.month, end.day)
    
    with st.spinner("Calculating price movements..."):
        data = yf.download(stockslist, start=start, end=end)['Close']
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(1)
            
        # Calculate log or percentage changes for returns correlation matrix
        returns_corr = data.pct_change().corr(method='pearson')
        
    # Generate interactive color heatmap layout seamlessly
    fig = px.imshow(
        returns_corr,
        text_auto=".2f", # Overlay numbers cleanly inside the grid blocks
        aspect="auto",
        color_continuous_scale="RdBu_r", # Classic red-to-blue balance map
        zmin=-1,
        zmax=1
    )
    
    fig.update_layout(
        height=600,
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=50, r=20, t=20, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please choose at least 2 stocks to build an overlapping correlation framework.")