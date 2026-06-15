import streamlit as st

st.set_page_config(
    page_title="About This Project",
    page_icon="📝",
    layout="wide"
)

st.title("Project Documentation & Engineering Insights 📝")
st.write("---")

# Three-part tab design separates high-level context from intense math/engineering blocks
tab1, tab2, tab3 = st.tabs(["📌 Project Overview", "🧮 Quantitative Methodologies", "💻 System Architecture"])

with tab1:
    st.markdown("### 🎯 Why This Project Exists")
    st.write(
        "Standard retail financial web portals often segment raw market data away from institutional-grade portfolio risk "
        "engineering frameworks and stochastic predictive modeling suites. This platform was built to bridge that gap—providing "
        "investors, analysts, and portfolio managers with an integrated environment to monitor real-time asset health, "
        "quantify systematic and risk-adjusted risk exposures, extract cross-asset dependencies, and evaluate algorithmic future price paths."
    )
    st.write(
        "By merging modern software development paradigms with empirical mathematical asset pricing models, this platform converts "
        "unstructured pricing files into automated, visual quantitative metrics dashboards."
    )
    
    st.markdown("### 🔍 Key Objectives")
    st.markdown(
        "* **Automate Complex Risk Quantifications:** Extract live market returns to calculate standalone, multi-asset comparative, and risk-adjusted parameters instantly.\n"
        "* **Demystify Advanced Modeling Suites:** Translate rigorous econometric algorithms (like ARIMA), path-dependent probability workflows (like Monte Carlo simulations), and diversification frameworks into visual, interactive chart telemetry.\n"
        "* **Eliminate Metric Information Friction:** Provide programmatic calculation layers that eliminate manual data pulling, historical timestamp alignment, and matrix cleaning errors.\n"
        "* **Enforce Enterprise Software Standards:** Prove how clean modular software architecture, decoupled structural logic layers, and separation of concerns apply directly to financial engineering domains."
    )

with tab2:
    st.markdown("### 📐 Deep-Dive Financial Mathematics & Feature Walkthrough")
    st.write(
        "To ensure the application functions as a robust quantitative tool rather than a generic chart tracker, "
        "independent financial mathematical architectures were engineered directly into each dashboard pipeline:"
    )
    st.write("---")
    
    # 1_CAPM_Beta
    st.markdown("### 📊 1. Individual Stock Systemic Risk (CAPM Beta Page)")
    st.markdown("**Use:**")
    st.write(
        "Isolates and evaluates an individual asset's historical sensitivity to macro-market movements. It was included to "
        "give investors a direct metric showing whether an equity magnifies or dampens overall stock market volatility trends."
    )
    st.markdown("**Quantitative Mechanics:**")
    st.write(
        "The system processes a rolling historical covariance matrix matching the selected equity's daily returns against the S&P 500 benchmark index. "
        "Beta ($$\beta$$) is derived by dividing that asset-market covariance by the variance of the market benchmark itself:"
    )
    st.latex(r"\beta = \frac{Cov(R_a, R_m)}{Var(R_m)}")
    st.write(
        "The calculated expected return ($$E(R_a)$$) scales this coefficient against the annualized average market return premium ($$R_m$$), assuming a zero baseline risk-free rate ($$R_f = 0$$):"
    )
    st.latex(r"E(R_a) = R_f + \beta \cdot (R_m - R_f)")
    st.write("---")

    # 2_CAPM_Return
    st.markdown("### 📈 2. Capital Asset Pricing Model (Multi-Asset CAPM Return Page)")
    st.markdown("**Use:**")
    st.write(
        "Extends systemic risk logic to a multi-asset comparative table layout. It automates simultaneous price normalization "
        "and portfolio risk calculations across an array of equities to evaluate real-time capital allocation trade-offs."
    )
    st.markdown("**Quantitative Mechanics:**")
    st.write(
        "The asset arrays undergo an automated temporal synchronization. First, historical index closes are normalized by anchoring them to their initial pricing coordinate ($$t_0$$) to track real percentage gains relative to the market baseline:"
    )
    st.latex(r"\text{Normalized Price}_t = \frac{\text{Price}_t}{\text{Price}_{t_0}}")
    st.write(
        "The background math engine leverages standard ordinary least squares linear regression via polynomial fitting across the arrays to extract individual asset alphas ($$\alpha$$) and betas ($$\beta$$) simultaneously:"
    )
    st.latex(r"R_{a,t} = \alpha + \beta \cdot R_{m,t} + \epsilon_t")
    st.write("---")

    # 3_Stock_Analysis
    st.markdown("### 🔍 3. Real-Time Market Intelligence (Stock Analysis Page)")
    st.markdown("**Use:**")
    st.write(
        "Delivers a holistic overview of fundamental corporate health and classic technical indicators. It pairs underlying accounting metrics "
        "with directional volume trends to contextualize short-term momentum shifts against longer macro asset horizons."
    )
    st.markdown("**Quantitative Mechanics:**")
    st.write(
        "The interface parses institutional-grade financial indices (including Market Cap, EPS, P/E, Debt-to-Equity, and Quick Ratios) "
        "while running real-time mathematical calculations for the **Relative Strength Index (RSI)** using a standard 14-day tracking frame:"
    )
    st.latex(r"\text{RSI} = 100 - \left[ \frac{100}{1 + \frac{\text{Average Gain}}{\text{Average Loss}}} \right]")
    st.write("---")

    # 4_Stock_Prediction
    st.markdown("### 🔮 4. Advanced Predictive Models Dashboard (Stock Prediction Page)")
    st.markdown("**Use:**")
    st.write(
        "Projects asset valuation paths over a fixed 30-day horizon using an advanced forecasting pipeline. It helps users visualize "
        "pure statistical trajectories alongside stochastic real-world risk variance bounds."
    )
    st.markdown("**Quantitative Mechanics:**")
    st.write(
        "This dashboard integrates a **Combined Algorithmic Hybrid Ensemble Engine** that resolves the limitations of standard standalone models. "
        "The forecasting pipeline operates through three distinct structural methods:"
    )
    st.write(
        "1. **Pure ARIMA Model:** Fits an AutoRegressive Integrated Moving Average model $$\\text{ARIMA}(2, d, 2)$$, where $$d$$ represents "
        "the dynamic differencing order computed via an automated Augmented Dickey-Fuller (ADF) stationarity check. This isolates the smooth macro directional mean trend line."
    )
    st.write(
        "2. **Pure Monte Carlo Simulation:** Generates a stochastic random risk walk based on geometric Brownian motion. It models unstructured daily market shocks by sampling from a normal distribution based on the asset's historical drift ($$\mu$$) and daily volatility factor ($$\sigma$$):"
    )
    st.latex(r"S_t = S_{t-1} \cdot e^{\left((\mu - \frac{1}{2}\sigma^2) + \sigma \cdot Z_t\right)} \quad \text{where } Z_t \sim N(0,1)")
    st.write(
        "3. **The Hybrid Ensemble (Recommended):** Combines both worlds. It takes the structured statistical regression trend vector produced by the ARIMA model "
        "and multiplies it by the Monte Carlo stochastic random shock factor at each chronological point. This preserves a realistic, volatile market path while keeping the prediction bound to logical underlying financial trends:"
    )
    st.latex(r"\text{Hybrid Projection}_t = \text{ARIMA Baseline}_t \cdot e^{\left(-\frac{1}{2}\sigma^2 + \sigma \cdot Z_t\right)}")
    st.write("---")

    # 5_Sharpe_Ratio
    st.markdown("### 🏆 5. Portfolio Risk & Sharpe Ratio Profiling (Sharpe Ratio Page)")
    st.markdown("**Use:**")
    st.write(
        "Evaluates asset efficiency on an annualized risk-adjusted basis. This page was included to determine whether an equity's "
        "excess performance return premium is driven by high-yield investment choice or exposure to dangerous underlying portfolio variance."
    )
    st.markdown("**Quantitative Mechanics:**")
    st.write(
        "The engine calculates total annualized returns alongside annualized volatility (scaling standard deviation across 252 active trading days). "
        "The **Sharpe Ratio** is derived by subtracting the user-defined Risk-Free Treasury Rate ($$R_f$$) from the total expected asset return, divided by the annualized standard deviation:"
    )
    st.latex(r"\text{Sharpe Ratio} = \frac{\text{Annualized } R_a - R_f}{\sigma_{\text{annualized}}}")
    st.write("---")

    # 6_Correlation_Heatmap
    st.markdown("### 🔥 6. Cross-Asset Pearson Correlation Diagnostics (Correlation Heatmap Page)")
    st.markdown("**Use:**")
    st.write(
        "Evaluates cross-asset dependencies across customized equity baskets. It provides a quick look at multi-collinearity, helping "
        "investors identify true diversification opportunities and avoid overlapping systemic asset exposures."
    )
    st.markdown("**Quantitative Mechanics:**")
    st.write(
        "The system extracts the daily fractional returns of all active equities and constructs a symmetric tracking matrix. It uses "
        "the **Pearson Product-Moment Correlation Coefficient** to check how tightly any two distinct asset series move in relation to one another:"
    )
    st.latex(r"\rho_{X,Y} = \frac{Cov(X,Y)}{\sigma_X \cdot \sigma_Y}")

with tab3:
    st.markdown("### 🏗️ Software Engineering Design Pattern & Architecture")
    st.write(
        "This application is built entirely on **clean modular coding principles**. Instead of utilizing messy monolithic script files where "
        "data ingestion, statistical analysis, and UI formatting code are dangerously tangled together, this codebase enforces a strict **Separation of Concerns**:"
    )
    
    st.markdown("#### 📁 Production Directory Layout Tree")
    st.code(
        """
QUANTDESK - Financial Analysis Platform/
├── __pycache__/                    # Compiled python bytecode cache files
├── pages/                          # Isolated multi-page application interfaces
│   ├── utils/                      # CENTRAL MODULAR UTILITY LOGIC ENGINE
│   │   ├── __pycache__/            # Cached utility execution binaries
│   │   ├── __init__.py             # Standard package directory declaration marker
│   │   ├── model_train.py          # Back-end algorithmic calculations (ARIMA, MC)
│   │   └── plotly_figure.py        # Layout canvas definitions & dark theme styling
│   ├── 1_CAPM_Beta.py              # Individual asset risk analysis component
│   ├── 2_CAPM_Return.py            # Multi-stock capital asset pricing component
│   ├── 3_Stock_Analysis.py         # Corporate fundamentals & momentum indicator dashboard
│   ├── 4_Stock_Prediction.py       # 30-day tab-matrix mathematical forecasting suite
│   ├── 5_Sharpe_Ratio.py           # Risk-adjusted portfolio metrics engine
│   └── 6_Correlation_Heatmap.py    # Symmetric asset dependencies plotting suite
├── 7_About.py                      # Central project technical documentation (This Page)
├── app.png                         # Global banner application asset
├── capm_functions.py               # Core vector math operations & data normalization
├── SOURCES.txt                     # System repository tracking logs
└── Trading_Guide_App.py            # Root application landing page deployment script
        """,
        language="text"
    )
    
    st.markdown("#### 🔄 Data Pipeline Pipeline Execution Flow")
    st.markdown(
        "1. **Ingestion Layer:** The user inputs an equity selection or target time window in the active frontend view (`pages/*.py`). The interface dispatches a data call downstream to download live ticker frames.\n"
        "2. **Transformation Layer:** Raw data matrices pass directly into `pages/utils/model_train.py` or `capm_functions.py`. The back-end calculation scripts run vector computations, execute stationarity checks, and isolate statistical prediction frames.\n"
        "3. **Aesthetic Mapping Layer:** The finalized mathematical datasets transfer into `pages/utils/plotly_figure.py`. The graphing script strips index files and enforces high-contrast text layers and custom plot styles.\n"
        "4. **Rendering Layer:** The output figure objects return cleanly to the front-end interface, which draws them onto the Streamlit canvas."
    )

st.write("---")
st.caption("📝 Project System Documentation Module • Version 1.2.0 • Engineered by Krishnendu Das")