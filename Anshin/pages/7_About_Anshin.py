import streamlit as st

st.set_page_config(
    page_title="About This Project",
    page_icon="📝",
    layout="wide"
)

st.title("Project Documentation & Engineering Insights 📝")
st.write("---")

tab1, tab2, tab3 = st.tabs(["📌 Project Overview", "🧮 Quantitative Methodologies", "💻 System Architecture"])

with tab1:
    st.markdown("### 🎯 Why This Project Exists")
    st.write(
        "Most retail finance apps show raw prices but skip the risk analysis investors actually need. "
        "Anshin was built to close that gap — giving users a single place to check an asset's risk profile, "
        "compare it against others, see how correlated it is to the rest of a portfolio, and view a "
        "data-driven price forecast."
    )
    st.write(
        "It combines standard financial formulas (CAPM, Beta, Sharpe Ratio) with live market data, so every "
        "number on the page is calculated in real time rather than pulled from a static file."
    )

    st.markdown("### 🔍 Key Objectives")
    st.markdown(
        "* **Automate risk calculations:** Pull live returns and compute Beta, Sharpe Ratio, and correlation instantly, without manual spreadsheet work.\n"
        "* **Make the models understandable:** Show the math (ARIMA, Monte Carlo, CAPM) alongside interactive charts, not just a black-box output.\n"
        "* **Keep the data clean:** Handle date alignment, missing values, and API errors automatically so users see reliable numbers.\n"
        "* **Write maintainable code:** Separate data, calculations, and UI into distinct modules, the way a production app would be structured."
    )

with tab2:
    st.markdown("### 📐 Financial Mathematics Behind Each Page")
    st.write(
        "Each page runs its own calculation, not just a chart. Here's what each one computes and why."
    )
    st.write("---")

    # 1_CAPM_Beta
    st.markdown("### 📊 1. Individual Stock Risk (CAPM Beta Page)")
    st.markdown("**Use:**")
    st.write(
        "Shows how sensitive one stock is to overall market movements — whether it swings more or less "
        "than the market on average."
    )
    st.markdown("**Mechanics:**")
    st.write(
        "Beta is the covariance between the stock's daily returns and the S&P 500's daily returns, divided "
        "by the market's variance:"
    )
    st.latex(r"\beta = \frac{Cov(R_a, R_m)}{Var(R_m)}")
    st.write(
        "Expected return then scales that Beta against the market's annualized return, using the current "
        "10-Year Treasury yield (Rf ≈ 4.2%) as the risk-free baseline:"
    )
    st.latex(r"E(R_a) = R_f + \beta \cdot (R_m - R_f)")
    st.write("---")

    # 2_CAPM_Return
    st.markdown("### 📈 2. Multi-Asset CAPM Comparison (CAPM Return Page)")
    st.markdown("**Use:**")
    st.write(
        "Runs the same CAPM analysis across multiple stocks side by side, so you can compare expected "
        "returns and risk levels across a basket of assets."
    )
    st.markdown("**Mechanics:**")
    st.write(
        "Prices are normalized to a common starting point so percentage gains are directly comparable:"
    )
    st.latex(r"\text{Normalized Price}_t = \frac{\text{Price}_t}{\text{Price}_{t_0}}")
    st.write(
        "Each stock's Alpha and Beta are then estimated with a simple linear regression against the market:"
    )
    st.latex(r"R_{a,t} = \alpha + \beta \cdot R_{m,t} + \epsilon_t")
    st.write("---")

    # 3_Stock_Analysis
    st.markdown("### 🔍 3. Company Fundamentals & Technicals (Stock Analysis Page)")
    st.markdown("**Use:**")
    st.write(
        "Gives a quick snapshot of a company's financial health (Market Cap, EPS, P/E, Debt-to-Equity) "
        "alongside a price chart and momentum indicators."
    )
    st.markdown("**Mechanics:**")
    st.write(
        "RSI (Relative Strength Index) is calculated over a 14-day window to flag whether a stock looks "
        "overbought or oversold:"
    )
    st.latex(r"\text{RSI} = 100 - \left[ \frac{100}{1 + \frac{\text{Average Gain}}{\text{Average Loss}}} \right]")
    st.write("---")

    # 4_Stock_Prediction
    st.markdown("### 🔮 4. 30-Day Price Forecast (Stock Prediction Page)")
    st.markdown("**Use:**")
    st.write(
        "Projects where a stock's price might go over the next 30 days, using three different modeling "
        "approaches so you can compare a smooth trend line against a more realistic, volatile path."
    )
    st.markdown("**Mechanics:**")
    st.write("Three models run side by side:")
    st.write(
        "1. **ARIMA:** Fits an ARIMA(2, d, 2) model, where d (the differencing order) is chosen automatically "
        "using an Augmented Dickey-Fuller stationarity test. This captures the underlying trend."
    )
    st.write(
        "2. **Monte Carlo:** Simulates a random price path using geometric Brownian motion, sampling daily "
        "shocks from a normal distribution based on the stock's historical drift (μ) and volatility (σ):"
    )
    st.latex(r"S_t = S_{t-1} \cdot e^{\left((\mu - \frac{1}{2}\sigma^2) + \sigma \cdot Z_t\right)} \quad \text{where } Z_t \sim N(0,1)")
    st.write(
        "3. **Hybrid (recommended):** Multiplies the ARIMA trend by the Monte Carlo shock factor at each step — "
        "keeping the forecast anchored to the trend while still reflecting realistic day-to-day volatility:"
    )
    st.latex(r"\text{Hybrid Projection}_t = \text{ARIMA Baseline}_t \cdot e^{\left(-\frac{1}{2}\sigma^2 + \sigma \cdot Z_t\right)}")
    st.write("---")

    # 5_Sharpe_Ratio
    st.markdown("### 🏆 5. Risk-Adjusted Return (Sharpe Ratio Page)")
    st.markdown("**Use:**")
    st.write(
        "Answers the question: is this stock's return actually good, once you account for how much risk "
        "it took to get there?"
    )
    st.markdown("**Mechanics:**")
    st.write(
        "Sharpe Ratio subtracts the risk-free rate from the annualized return, then divides by annualized "
        "volatility (standard deviation, scaled to 252 trading days):"
    )
    st.latex(r"\text{Sharpe Ratio} = \frac{\text{Annualized } R_a - R_f}{\sigma_{\text{annualized}}}")
    st.write(
        "A higher Sharpe Ratio means better return per unit of risk. Anything above 1.0 is generally "
        "considered good; above 2.0 is very strong."
    )
    st.write("---")

    # 6_Correlation_Heatmap
    st.markdown("### 🔥 6. Cross-Asset Correlation (Correlation Heatmap Page)")
    st.markdown("**Use:**")
    st.write(
        "Shows how closely different stocks move together, which helps identify real diversification versus "
        "stocks that just look different but move in tandem."
    )
    st.markdown("**Mechanics:**")
    st.write(
        "Pairwise Pearson correlation is calculated across daily returns for every stock in the selected basket:"
    )
    st.latex(r"\rho_{X,Y} = \frac{Cov(X,Y)}{\sigma_X \cdot \sigma_Y}")
    st.write(
        "Values near 1 mean two stocks move almost identically; values near 0 mean little relationship — "
        "useful for spotting genuine diversification opportunities."
    )
    st.write("---")

    # 8_Portfolio_Insights
    st.markdown("### 🧭 7. Cross-Stock Ranking (Portfolio Insights Page)")
    st.markdown("**Use:**")
    st.write(
        "Pulls the same Beta, return, volatility, and Sharpe metrics used elsewhere in the app, but computes "
        "them across the full stock universe at once — ranking assets and sectors instead of viewing them one at a time."
    )
    st.markdown("**Mechanics:**")
    st.write(
        "Reuses the CAPM and Sharpe formulas above across every selected ticker, then aggregates results into "
        "a risk-return scatter plot and a sector-level summary table, with a short written takeaway generated "
        "from the current live numbers."
    )

with tab3:
    st.markdown("### 🏗️ Code Structure")
    st.write(
        "The app is split into separate files by responsibility — data fetching, calculations, and page "
        "layout are kept apart instead of mixed into one script. This makes each piece easier to test, "
        "debug, and reuse."
    )

    st.markdown("#### 📁 Project Layout")
    st.code(
        """
Anshin - Code/
├── pages/
│   ├── utils/
│   │   ├── __init__.py          # Package marker
│   │   ├── model_train.py       # ARIMA + Monte Carlo forecasting logic
│   │   └── plotly_figure.py     # Chart styling and layout helpers
│   ├── 1_CAPM_Beta.py           # Single-stock Beta and CAPM return
│   ├── 2_CAPM_Return.py         # Multi-stock CAPM comparison
│   ├── 3_Stock_Analysis.py      # Fundamentals + technical indicators
│   ├── 4_Stock_Prediction.py    # 30-day forecasting dashboard
│   ├── 5_Sharpe_Ratio.py        # Risk-adjusted return ranking
│   ├── 6_Correlation_Heatmap.py # Pairwise correlation matrix
│   ├── 7_About_Anshin.py        # This documentation page
│   └── 8_Portfolio_Insights.py  # Cross-stock ranking and takeaways
├── capm_functions.py            # Shared Beta/return/plotting functions
├── requirements.txt             # Pinned dependencies
├── SOURCES.txt                  # Repository tracking notes
└── Anshin.py                    # App entry point
        """,
        language="text"
    )

    st.markdown("#### 🔄 How Data Flows Through the App")
    st.markdown(
        "1. **Fetch:** The user picks a stock or time range on a page, which triggers a live call to yfinance.\n"
        "2. **Calculate:** Raw price data is passed into `capm_functions.py` or `model_train.py`, which run the "
        "actual math (returns, Beta, Sharpe, ARIMA, Monte Carlo).\n"
        "3. **Format:** Results are handed to `plotly_figure.py`, which builds the charts and tables with "
        "consistent dark-theme styling.\n"
        "4. **Render:** Streamlit displays the finished charts and tables on the page."
    )

st.write("---")
st.caption("📝 Project Documentation • Version 1.2.0 • Built by Krishnendu Das")
