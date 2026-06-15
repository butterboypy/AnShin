# ANSHIN // Quantitative Equity Analytics & Risk Intelligence Platform

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/frontend-streamlit-FF4B4B.svg)](https://streamlit.io/)
[![yfinance](https://img.shields.io/badge/data-yfinance-brightgreen.svg)](https://pypi.org/project/yfinance/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Anshin (安心)** — A Japanese philosophy of *structured peace of mind*: the elimination of uncertainty through systematic clarity. Applied here to financial risk, this platform transforms raw market noise into rigorous, decision-ready intelligence.

---

## 🏦 Business Context & Motivation

Institutional desks at firms rely on integrated quantitative workstations to centralize asset risk exposure, expected return modeling, and cross-portfolio correlation diagnostics. Retail-grade platforms fragment these capabilities — isolating charting tools from pricing models and risk-adjustment frameworks.

**Anshin closes this gap.** Built as a full-stack quantitative analytics workstation, it aggregates, processes, and models live multi-sector equity data across **33 core stocks spanning 6 economic sectors** (Technology, Finance, Healthcare, Energy, Consumer, and Industrial), delivering institutional-grade portfolio intelligence through a clean, interactive dashboard interface.

This project demonstrates direct competency in the quantitative methods, data engineering patterns, and analytical storytelling that underpin modern sell-side research, risk analytics, and investment data roles.

---

## 📐 Quantitative Analytics Modules

### 1. Systemic Risk & Beta Sensitivity (`1_CAPM_Beta.py`)
Computes individual equity **Beta coefficients** by regressing daily asset returns against S&P 500 benchmark returns using Ordinary Least Squares. Surfaces the OLS trend line over a live scatter plot to enable immediate visual detection of return outliers and volatility clustering.

**Applicable to:** Market risk quantification, VaR pre-processing, factor model construction.

---

### 2. Multi-Asset CAPM Return Comparator (`2_CAPM_Return.py`)
Normalizes multi-ticker price series to a shared $t_0$ baseline to enable side-by-side historical return and alpha comparison. Computes CAPM-implied expected returns per ticker to flag valuation mismatches between realized and model-predicted performance.

**Applicable to:** Asset allocation optimization, equity research coverage, portfolio benchmarking.

---

### 3. Corporate Fundamentals & Technical Indicator Dashboard (`3_Stock_Analysis.py`)
Fuses balance-sheet health metrics (Market Cap, P/E, EPS, Debt-to-Equity) with real-time technical oscillators (14-Day RSI, MACD) and dynamic candlestick charts. Provides a single-screen view bridging fundamental valuation with short-term momentum signals.

**Applicable to:** Equity research due diligence, credit risk screening, analyst coverage workflows.

---

### 4. Hybrid Ensemble Forecasting Engine (`4_Stock_Prediction.py`)
30-day forward price trajectory modeling using a custom **Hybrid Ensemble Pipeline** that resolves the mean-reversion flattening problem of standalone ARIMA and the logical drift risk of standalone Monte Carlo simulations — by multiplying their outputs:

$$\text{Hybrid Prediction}_t = \text{ARIMA Baseline}_t \cdot e^{\left(-\frac{1}{2}\sigma^2 + \sigma \cdot Z_t\right)}$$

Three model variants are exposed (Hybrid Ensemble, ARIMA-only, Pure Monte Carlo) for side-by-side methodological benchmarking.

**Applicable to:** Price target modeling, stress testing scenario construction, quantitative research.

---

### 5. Sharpe Ratio & Risk-Adjusted Return Profiler (`5_Sharpe_Ratio.py`)
Annualizes portfolio returns across 252 active trading days and scales against a user-configurable risk-free benchmark rate to compute true risk-adjusted efficiency. Separates raw return magnitude from excess variance to surface genuine outperformance.

$$\text{Sharpe Ratio} = \frac{\text{Annualized } R_a - R_f}{\sigma_{\text{annualized}}}$$

**Applicable to:** Portfolio performance attribution, fund manager evaluation, capital allocation decisioning.

---

### 6. Asset Correlation Matrix & Diversification Diagnostics (`6_Correlation_Heatmap.py`)
Computes Pearson Product-Moment Correlation matrices across custom user-defined asset baskets to identify hidden co-movements and diversification gaps. Interactive heatmap renders statistically significant dependencies as immediately readable color gradients.

$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \cdot \sigma_Y}$$

**Applicable to:** Portfolio construction, systemic risk concentration analysis, multi-asset diversification strategy.

---

## 🧮 Statistical & Quantitative Financial Frameworks

### Capital Asset Pricing Model (CAPM)

Beta is derived by regressing the covariance of asset and market returns against market variance:

$$\beta = \frac{\text{Cov}(R_a, R_m)}{\text{Var}(R_m)}$$

Expected return is then priced using the fundamental CAPM risk-return identity:

$$E(R_a) = R_f + \beta \cdot (E(R_m) - R_f)$$

### Time-Series Ensemble Forecasting Architecture

The forecasting engine resolves two structural limitations in isolation:

- **ARIMA** captures directional trend but produces long-horizon mean-reversion flattening
- **Monte Carlo (GBM)** captures stochastic volatility but produces logical price drift over time

The **Hybrid Ensemble Pipeline** blends both via a 3-stage architecture:

1. **Trend Baseline** — Fits a non-stationary $\text{ARIMA}(2, d, 2)$ model (auto-differencing order selected via Augmented Dickey-Fuller stationarity test)
2. **Stochastic Shock Generation** — Simulates geometric Brownian motion paths from historical drift ($\mu$) and volatility ($\sigma$):

$$S_t = S_{t-1} \cdot e^{\left((\mu - \frac{1}{2}\sigma^2) + \sigma \cdot Z_t\right)}, \quad Z_t \sim \mathcal{N}(0,1)$$

3. **Ensemble Blending** — Chronologically multiplies ARIMA trend by GBM shock factor to produce economically-bounded, volatile prediction paths

---

## ⚙️ Engineering Architecture

This project enforces strict **Separation of Concerns** — a software design principle central to maintainable, production-grade analytics systems:

```text
AnShin - Code/                          # Project Root Directory
├── pages/                              # Independent Analytics Dashboard Views
│   ├── utils/                          # CALCULATIONS & VISUALIZATION ENGINES
│   │   ├── model_train.py              # Statistical backend (Time-Series Modeling & Simulations)
│   │   └── plotly_figure.py            # Centralized interactive data visualization templates
│   ├── 1_CAPM_Beta.py                  # Systemic risk & macro sensitivity view
│   ├── 2_CAPM_Return.py                # Comparative expected returns analytics view
│   ├── 3_Stock_Analysis.py             # Corporate fundamentals & technical indicators view
│   ├── 4_Stock_Prediction.py           # Hybrid time-series forecasting & trend analysis view
│   ├── 5_Sharpe_Ratio.py               # Risk-adjusted return performance profiling view
│   ├── 6_Correlation_Heatmap.py        # Cross-asset dependency & multicollinearity view
│   └── 7_About.py                      # Project documentation & methodological breakdown
├── app.png                             # Dashboard overview graphic
├── capm_functions.py                   # Data normalization & mathematical transformation utilities
├── SOURCES.txt                         # Environment dependencies & library manifests
└── Trading_Guide_App.py                # Dashboard welcome landing page

```

**Architectural Principles Applied:**
- **Modular layer separation:** Statistical computation (`utils/`) is fully decoupled from UI presentation (`pages/`) — mirroring the ETL-to-BI-layer pattern common in enterprise data platforms
- **Vectorized data transformations:** All time-series operations run via pandas/NumPy vectorized pipelines — no row-level iteration
- **Stationarity-aware modeling:** Dickey-Fuller tests gate ARIMA differencing order selection, preventing spurious regressions on non-stationary financial series
- **Caching for performance:** Data ingestion calls are memory-cached to eliminate redundant API round-trips on parameter recalibration

---

## 🔄 End-to-End Data Pipeline

```
[yfinance API] → [Raw OHLCV Arrays] → [Pandas Cleaning & Date Alignment]
       ↓
[capm_functions.py / model_train.py] → [Beta, Returns, ARIMA, GBM, Sharpe, Correlation]
       ↓
[plotly_figure.py] → [Dark-themed interactive Plotly figures]
       ↓
[Streamlit Multi-page App] → [Dashboard output layer]
```

1. **Ingestion & Caching** — Ticker selection triggers programmatic extraction of daily historical OHLCV arrays; responses are cached in-session to minimize redundant API calls
2. **Statistical Transformation** — Raw arrays pass into vectorized calculation modules; pandas DataFrames execute transformations, stationarity checks, and date vector alignment
3. **Visualization Mapping** — Processed outputs feed the centralized Plotly engine, configuring hover nodes, axis labels, and high-contrast dark theme styling
4. **Dashboard Rendering** — Final visual assets are output to the Streamlit page layer for interactive delivery

---

## ⚡ Technology Stack

| Layer | Tool | Purpose |
|---|---|---|
| Language | Python 3.13 | Core runtime |
| Dashboard Framework | Streamlit | Multi-page interactive UI |
| Market Data | yfinance (Yahoo Finance API) | Live OHLCV ingestion |
| Vector Mathematics | NumPy + Pandas | Vectorized matrix operations |
| Statistical Modeling | Statsmodels | ARIMA, ADF stationarity testing |
| Technical Indicators | pandas-ta | RSI, MACD computation |
| Visualization | Plotly (Graph Objects + Express) | Interactive dark-theme charting |

---

## 📊 Dashboard Preview

| Module | View |
|---|---|
| CAPM Beta | OLS regression scatter — daily returns vs. S&P 500 |
| CAPM Return | Normalized multi-ticker price performance comparison |
| Stock Analysis | Candlestick + RSI/MACD + fundamentals panel |
| Stock Prediction | Hybrid Ensemble, ARIMA, and Monte Carlo forecast overlays |
| Sharpe Ratio | Annualized risk-adjusted return ranking across tickers |
| Correlation Heatmap | Interactive Pearson matrix — user-defined asset basket |

---

## 👤 Author

**Krishnendu Das**
End-to-end quantitative data engineering, financial modeling, and analytics dashboard development.
