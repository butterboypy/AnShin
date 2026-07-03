# import streamlit as st
# from pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, get_forecast, inverse_scaling, scaling, evaluate_model
# import pandas as pd
# from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

# st.set_page_config(
#     page_title="Stock Prediction",
#     page_icon="chart_with_downwards_trend",
#     layout="wide",
# )

# st.title("Stock Prediction")

# coll, col2, col3 = st.columns(3)

# with coll:
#     ticker = st.text_input('Stock Ticker', 'AAPL')

# rmse = 0

# st.subheader('Predicting Next 30 days Close Price for: ' + ticker)

# close_price = get_data(ticker)
# rolling_price = get_rolling_mean(close_price)

# differencing_order = get_differencing_order(rolling_price)
# scaled_data, scaler = scaling(rolling_price)
# rmse = evaluate_model(scaled_data, differencing_order)

# st.write("**Model RMSE Score:**", rmse)

# forecast = get_forecast(scaled_data, differencing_order)

# forecast['Close'] = inverse_scaling(scaler, forecast['Close'])
# st.write('##### Forecast Data (Next 30 days)')
# fig_tail = plotly_table(forecast.sort_index(ascending = True).round(3))
# fig_tail.update_layout(height = 220)
# st.plotly_chart(fig_tail, use_container_width=True)

# forecast = pd.concat([rolling_price, forecast])

# st.plotly_chart(Moving_average_forecast(forecast.iloc[150:]), use_container_width = True)

# import streamlit as st
# from pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, get_forecast, inverse_scaling, scaling, evaluate_model
# import pandas as pd
# from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

# st.set_page_config(
#     page_title="Stock Prediction",
#     page_icon="🔮",
#     layout="wide",
# )

# st.title("Stock Prediction")

# col1, col2, col3 = st.columns([1, 1, 1])

# with col1:
#     # Dropdown selector matches option patterns used across other application views
#     ticker = st.selectbox(
#         "Select Stock Ticker", 
#         options=["AAPL", "AMD", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "UNH"],
#         index=1  # Defaults to AMD to match your current layout view
#     )

# st.subheader(f'Predicting Next 30 days Close Price for: {ticker}')

# with st.spinner("Processing time-series transformations and fitting model models..."):
#     # Execute historical model pipeline
#     close_price = get_data(ticker)
#     # rolling_price = get_rolling_mean(close_price)
#     differencing_order = get_differencing_order(close_price)
    
#     # Scale features and evaluate baseline model validation scores
#     scaled_data, scaler = scaling(close_price)
#     rmse = evaluate_model(scaled_data, differencing_order)

# # st.markdown(f"**Model RMSE Score:** `{rmse}`")
# st.markdown(f"**Daily Volatility (Risk Factor):** `{rmse}%`")

# # Generate 30-day forecast values
# forecast_scaled = get_forecast(scaled_data, differencing_order)
# forecast_scaled['Close'] = inverse_scaling(scaler, forecast_scaled['Close'])

# st.write('##### Forecast Data (Next 30 days)')

# # Render the formatted table containing explicit Date indexes
# fig_table = plotly_table(forecast_scaled)
# st.plotly_chart(fig_table, use_container_width=True)

# # Combine datasets chronologically to display trendlines cleanly
# historical_flat = pd.DataFrame(close_price['Close'], index=close_price.index)
# combined_forecast = pd.concat([historical_flat, forecast_scaled])

# st.write('##### Historical vs Future Close Price Forecast Chart')
# # Displays the last 90 trading sessions along with the 30-day forecast to improve layout proportions
# st.plotly_chart(Moving_average_forecast(combined_forecast.iloc[-120:]), use_container_width=True)

import streamlit as st
from pages.utils.model_train import get_data, get_predictions_all
import pandas as pd
from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

st.set_page_config(
    page_title="Stock Prediction",
    page_icon="🔮",
    layout="wide",
)

st.title("Advanced Predictive Models Dashboard")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    ticker = st.selectbox(
        "Select Stock Ticker", 
        options= ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V",
                  "UNH", "INTC", "AMD", "CRM", "BAC", "GS", "MS", "BLK", "AXP", "JNJ", 
                  "PFE", "ABBV", "MRK", "XOM", "CVX", "COP", "MCD", "KO", "PG", "WMT", 
                  "NKE", "CAT", "BA", "HON"],
        index=1  # Defaults to AMD
    )

st.subheader(f'Analysis Pipeline Metrics for: {ticker}')

with st.spinner("Synchronizing datasets and mapping algorithmic projection vectors..."):
    close_price = get_data(ticker)
    # Extracts all three forecasts simultaneously from your combined model_train engine
    df_arima, df_mc, df_hybrid, volatility = get_predictions_all(close_price)

st.markdown(f"**Asset Daily Risk Factor (Volatility):** `{volatility}%`")

# --- INTERACTIVE TAB BAR CONFIGURATION ---
tab1, tab2, tab3 = st.tabs(["🔴 Hybrid Ensemble (Recommended)", "🔵 ARIMA Model", "🟢 Pure Monte Carlo"])

historical_flat = pd.DataFrame(close_price['Close'], index=close_price.index)

with tab1:
    st.markdown("### Hybrid Ensemble Forecast (Trend + Volatility)")
    st.caption("Combines the regression path of ARIMA with stochastic volatility factors.")
    st.plotly_chart(plotly_table(df_hybrid), use_container_width=True, key="tbl_hybrid")
    
    combined_hybrid = pd.concat([historical_flat, df_hybrid])
    st.plotly_chart(Moving_average_forecast(combined_hybrid.iloc[-120:]), use_container_width=True, key="chart_hybrid")

with tab2:
    st.markdown("### Pure ARIMA Forecast (Statistical Mean)")
    st.caption("Calculates past patterns and draws an explicit, streamlined macro directional path.")
    st.plotly_chart(plotly_table(df_arima), use_container_width=True, key="tbl_arima")
    
    combined_arima = pd.concat([historical_flat, df_arima])
    st.plotly_chart(Moving_average_forecast(combined_arima.iloc[-120:]), use_container_width=True, key="chart_arima")

with tab3:
    st.markdown("### Pure Monte Carlo Simulation (Random Risk Walk)")
    st.caption("Simulates standard drift returns utilizing unstructured normal shock distributions.")
    st.plotly_chart(plotly_table(df_mc), use_container_width=True, key="tbl_mc")
    
    combined_mc = pd.concat([historical_flat, df_mc])
    st.plotly_chart(Moving_average_forecast(combined_mc.iloc[-120:]), use_container_width=True, key="chart_mc")