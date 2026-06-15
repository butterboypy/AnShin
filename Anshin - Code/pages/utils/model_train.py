import yfinance as yf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import pandas as pd
from datetime import timedelta

def get_data(ticker):
    stock_data = yf.download(ticker, start='2024-01-01')
    if isinstance(stock_data.columns, pd.MultiIndex):
        stock_data.columns = stock_data.columns.get_level_values(0)
    return stock_data[['Close']].dropna()

def stationary_check(close_price):
    try:
        adf_test = adfuller(close_price)
        return round(adf_test[1], 3)
    except:
        return 0.99

def get_differencing_order(close_price):
    p_value = stationary_check(close_price)
    d = 0
    df_temp = close_price.copy()
    while p_value > 0.05 and d < 2:
        d += 1
        df_temp = df_temp.diff().dropna()
        p_value = stationary_check(df_temp)
    return d

def get_predictions_all(original_price):
    # --- COMBINED ALGORITHMIC ENGINE ---
    d = get_differencing_order(original_price)
    returns = original_price['Close'].pct_change().dropna()
    sigma = returns.std()  # Daily Volatility Factor
    mu = returns.mean()    # Historical Drift Trend
    
    last_price = original_price['Close'].iloc[-1]
    last_date = original_price.index[-1]
    days = 30
    forecast_index = pd.date_range(start=last_date + timedelta(days=1), periods=days, freq='D')
    
    # 1. MODEL 1: PURE ARIMA GENERATION
    try:
        model = ARIMA(np.asarray(original_price['Close']), order=(2, d, 2))
        model_fit = model.fit()
        arima_preds = model_fit.get_forecast(steps=days).predicted_mean
    except:
        arima_preds = np.linspace(last_price, last_price * (1 + mu * days), days)

    # 2. MODEL 2: PURE MONTE CARLO GENERATION
    np.random.seed(42)  
    random_shocks = np.random.normal(0, 1, days)
    mc_preds = np.zeros(days)
    curr_mc = last_price
    for t in range(days):
        curr_mc *= np.exp((mu - 0.5 * sigma**2) + sigma * random_shocks[t])
        mc_preds[t] = curr_mc

    # 3. MODEL 3: HYBRID ENSEMBLE GENERATION
    hybrid_preds = np.zeros(days)
    for t in range(days):
        base_trend = arima_preds[t]
        shock_factor = np.exp(-0.5 * sigma**2 + sigma * random_shocks[t])
        hybrid_preds[t] = base_trend * shock_factor

    # Convert results into clean structured dataframes
    df_arima = pd.DataFrame(arima_preds, index=forecast_index, columns=['Close'])
    df_mc = pd.DataFrame(mc_preds, index=forecast_index, columns=['Close'])
    df_hybrid = pd.DataFrame(hybrid_preds, index=forecast_index, columns=['Close'])
    
    return df_arima, df_mc, df_hybrid, round(sigma * 100, 2)