import datetime
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="Portfolio Insights", page_icon="🧭", layout="wide")

st.title("Portfolio & Analyst Insights")
st.caption(
    "Cross-sectional view across the full stock universe — ranks assets by risk-adjusted "
    "performance and surfaces the takeaways a live dashboard normally leaves buried in single-stock views."
)

# ---------------------------------------------------------------------------
# 1. Universe & sector mapping
# ---------------------------------------------------------------------------
SECTOR_MAP = {
    "AAPL": "Tech", "MSFT": "Tech", "GOOGL": "Tech", "AMZN": "Tech", "META": "Tech",
    "NVDA": "Tech", "INTC": "Tech", "AMD": "Tech", "CRM": "Tech",
    "JPM": "Finance", "V": "Finance", "BAC": "Finance", "GS": "Finance",
    "MS": "Finance", "BLK": "Finance", "AXP": "Finance",
    "UNH": "Healthcare", "JNJ": "Healthcare", "PFE": "Healthcare",
    "ABBV": "Healthcare", "MRK": "Healthcare",
    "XOM": "Energy", "CVX": "Energy", "COP": "Energy",
    "MCD": "Consumer", "KO": "Consumer", "PG": "Consumer", "WMT": "Consumer", "NKE": "Consumer",
    "CAT": "Industrial", "BA": "Industrial", "HON": "Industrial",
    "TSLA": "Consumer",
}
TICKERS = list(SECTOR_MAP.keys())

col1, col2 = st.columns([2, 1])
with col1:
    selected = st.multiselect(
        "Universe to analyze (defaults to full basket)",
        options=TICKERS,
        default=TICKERS,
    )
with col2:
    rf_rate = st.number_input(
        "Risk-Free Rate (%) (US 10Y Treasury)", min_value=0.0, max_value=10.0, value=4.2, step=0.1
    )

if not selected:
    st.warning("Select at least one ticker to build the insights view.")
    st.stop()

# ---------------------------------------------------------------------------
# 2. Data fetch + metric calculations (cached so repeated visits are fast)
# ---------------------------------------------------------------------------
@st.cache_data(ttl=3600, show_spinner=False)
def load_universe_metrics(tickers, rf_pct):
    end = datetime.date.today()
    start = datetime.date(end.year - 3, end.month, end.day)

    raw = yf.download(tickers + ["^GSPC"], start=start, end=end)["Close"]
    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(-1)

    returns = raw.pct_change().dropna()
    rf = rf_pct / 100
    market_var = returns["^GSPC"].var()

    rows = []
    for t in tickers:
        if t not in returns.columns:
            continue
        stock_ret = returns[t]
        ann_return = stock_ret.mean() * 252
        ann_vol = stock_ret.std() * np.sqrt(252)
        beta = returns[[t, "^GSPC"]].cov().iloc[0, 1] / market_var
        sharpe = (ann_return - rf) / ann_vol if ann_vol > 0 else np.nan

        rows.append({
            "Ticker": t,
            "Sector": SECTOR_MAP.get(t, "Other"),
            "Beta": round(beta, 2),
            "Annualized Return (%)": round(ann_return * 100, 2),
            "Annualized Volatility (%)": round(ann_vol * 100, 2),
            "Sharpe Ratio": round(sharpe, 2),
        })

    return pd.DataFrame(rows)


with st.spinner("Pulling 3-year return history and computing risk metrics..."):
    metrics_df = load_universe_metrics(selected, rf_rate)

if metrics_df.empty:
    st.error("Could not retrieve data for the selected tickers. Try a different selection.")
    st.stop()

metrics_df = metrics_df.sort_values("Sharpe Ratio", ascending=False).reset_index(drop=True)

# ---------------------------------------------------------------------------
# 3. Risk-return scatter
# ---------------------------------------------------------------------------
st.markdown("### Risk-Return Landscape")
st.caption("Bubble size = Sharpe Ratio. Ideal assets sit up-and-left: high return, low volatility.")

fig = px.scatter(
    metrics_df,
    x="Annualized Volatility (%)",
    y="Annualized Return (%)",
    color="Sector",
    size=metrics_df["Sharpe Ratio"].clip(lower=0.05),
    hover_name="Ticker",
    text="Ticker",
    size_max=40,
)
fig.update_traces(textposition="top center")
fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    height=550,
    margin=dict(l=20, r=20, t=20, b=20),
)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# 4. Ranked table
# ---------------------------------------------------------------------------
st.markdown("### Ranked by Risk-Adjusted Return (Sharpe Ratio)")
st.dataframe(metrics_df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# 5. Auto-generated callouts
# ---------------------------------------------------------------------------
st.markdown("### Key Callouts")

best = metrics_df.iloc[0]
worst_vol = metrics_df.loc[metrics_df["Annualized Volatility (%)"].idxmax()]
lowest_beta = metrics_df.loc[metrics_df["Beta"].idxmin()]
highest_beta = metrics_df.loc[metrics_df["Beta"].idxmax()]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Best Risk-Adjusted", best["Ticker"], f"Sharpe {best['Sharpe Ratio']}")
c2.metric("Highest Volatility", worst_vol["Ticker"], f"{worst_vol['Annualized Volatility (%)']}%")
c3.metric("Most Defensive (Low Beta)", lowest_beta["Ticker"], f"β {lowest_beta['Beta']}")
c4.metric("Most Aggressive (High Beta)", highest_beta["Ticker"], f"β {highest_beta['Beta']}")

# ---------------------------------------------------------------------------
# 6. Sector-level summary + written takeaway
# ---------------------------------------------------------------------------
st.markdown("### Sector Summary")

sector_summary = (
    metrics_df.groupby("Sector")[["Annualized Return (%)", "Annualized Volatility (%)", "Sharpe Ratio"]]
    .mean()
    .round(2)
    .sort_values("Sharpe Ratio", ascending=False)
)
st.dataframe(sector_summary, use_container_width=True)

top_sector = sector_summary.index[0]
bottom_sector = sector_summary.index[-1]

st.markdown("### Takeaway")
st.write(
    f"Across the selected universe, **{best['Ticker']}** offers the strongest risk-adjusted return "
    f"(Sharpe {best['Sharpe Ratio']}), while **{worst_vol['Ticker']}** carries the most volatility at "
    f"{worst_vol['Annualized Volatility (%)']}% annualized. At the sector level, **{top_sector}** "
    f"shows the best average Sharpe ratio in this basket, whereas **{bottom_sector}** lags — worth "
    f"checking the correlation heatmap to see whether combining sectors like these actually improves "
    f"diversification or just adds volatility without added return."
)

st.info(
    "ℹ️ This page recomputes on every session using live 3-year return history — figures will drift "
    "as markets move, unlike a static report."
)
