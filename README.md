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
