import streamlit as st

st.set_page_config(
    page_title="Anshin",
    page_icon="💸",
    layout="wide"
)

st.title("Anshin 🍜")
st.write("---")
st.header("Welcome to Anshin, Navigate Complexity Tension-Free!")
st.write(
    "Anshin is a Quantitative Financial Analysis Platform built using Python - Streamlit & yfinance. "
    "It is a full-stack equity analytics trading guide platform, engineered for Market Clarity, "
    "featuring live market data for stock analysis & prediction, CAPM/Beta "
    "risk modeling, Sharpe Ratio analysis, correlation matrices, technical indicators like RSI/MACD, "
    "and an ML-based hybrid forecasting engine (ARIMA + Monte Carlo) across 34 stocks spanning 6 sectors — "
    "Tech, Finance, Healthcare, Energy, Consumer, and Industrial."
)

# Maintain your local image banner asset pipeline
#st.image("app2.png")

st.write("---")
st.markdown("## 🛠️ Core Analytical Services & Architecture")
st.write("---")

# Section 1
st.markdown("### :one: Systemic Risk Profiling & CAPM Beta Engine")
st.write(
    "Quantify asset volatility relative to macro-market indices. This module calculates historical "
    "covariance metrics against the S&P 500 benchmark over custom multi-year windows to derive "
    "precise **Beta coefficients** and map underlying equity risk profiles."
)

# Section 2
st.markdown("### :two: Multi-Asset Expected Return Optimization")
st.write(
    "Apply the mathematical foundation of the **Capital Asset Pricing Model (CAPM)** to evaluate "
    "portfolio risk-return trade-offs. This feature automates risk-premium evaluations to determine "
    "the baseline expected return requirements for individual equity tiers and diversified asset classes."
)

# Section 3
st.markdown("### :three: Real-Time Market Intelligence & Stock Analysis")
st.write(
    "Access institutional-grade market data streaming. Powered by live API connectivity, this interface "
    "delivers detailed financial disclosures, fundamental accounting metrics (EPS, P/E, Debt-to-Equity), "
    "and interactive technical analysis chart tracking featuring custom candle layouts and RSI oscillators."
)

# Section 4
st.markdown("### :four: Stochastic & Statistical Price Path Forecasting")
st.write(
    "Explore future asset valuation bounds through an advanced predictive suite. By incorporating an "
    "**Ensemble Hybrid Model**, the forecasting pipeline anchors long-term momentum to statistical time-series "
    "regression (ARIMA) while injecting realistic short-term daily volatility shocks via **Monte Carlo simulations**."
)

# Section 5
st.markdown("### :five: Portfolio Risk & Annualized Sharpe Ratio Profiling")
st.write(
    "Evaluate assets on a risk-adjusted basis by parsing historical volatility against guaranteed risk-free benchmarks. "
    "This module calculates the **Sharpe Ratio** to isolate whether an equity's raw excess return premium is driven by "
    "smart investment allocations or exposure to destabilizing systemic variance."
)

# Section 6
st.markdown("### :six: Cross-Asset Pearson Correlation Diagnostics")
st.write(
    "Visualize systemic dependencies across customizable baskets of equities. By computing a live **Pearson Correlation Matrix**, "
    "this tracking tool maps directional cross-asset multi-collinearity to assist in risk-diversification strategies."
)

st.write("---")
st.info("ℹ️ **Looking for a deep dive into the code mechanics and theoretical foundations?** For more details go to the about page section via the sidebar navigation menu.")

st.write("---")
st.caption("🚀 Designed as an end-to-end Financial Analysis & Quantitative Data Project. Navigate using the sidebar to explore the individual analytical layers.")