#importing libraries
import datetime
import streamlit as st
import pandas as pd
import yfinance as yf 
import capm_functions 

st.set_page_config(page_title = "CAPM", 
                   page_icon = "chart_with_upwards_trend", 
                   layout = "wide")

st.title("Capital Asset Pricing Model (CAPM) Calculator")

# getting user input
try:
    col1, col2 = st.columns([1,1])
    with col1:
        stockslist = st.multiselect("Select the stocks you want to analyze", 
                    options = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "V",
                               "UNH", "INTC", "AMD", "CRM", "BAC", "GS", "MS", "BLK", "AXP", "JNJ", 
                               "PFE", "ABBV", "MRK", "XOM", "CVX", "COP", "MCD", "KO", "PG", "WMT", 
                               "NKE", "CAT", "BA", "HON"], 
                    default = ["AAPL", "MSFT"])
    with col2:
        years = st.number_input("Number of years for historical data", 1, 10)

    # Fetching data window
    end = datetime.date.today()
    start = datetime.date(end.year - years, end.month, end.day)

    # 1. Download S&P 500 (Our Master Left Timeline)
    sp500_raw = yf.download('^GSPC', start=start, end=end)

    if isinstance(sp500_raw.columns, pd.MultiIndex):
        sp500_close = sp500_raw['Close']['^GSPC']
    else:
        sp500_close = sp500_raw['Close']

    SP500 = pd.DataFrame({'sp500': sp500_close})

    # 2. Collect other stock data in a temporary list to prevent index clipping
    extracted_stocks = []

    for stock in stockslist:
        stock_data = yf.download(stock, start=start, end=end)
        
        if isinstance(stock_data.columns, pd.MultiIndex):
            stock_close = stock_data['Close'][stock]
        else:
            stock_close = stock_data['Close']
            
        # Name the Series cleanly by its ticker name
        extracted_stocks.append(stock_close.rename(stock))

    # Combine all individual stock series into a single multi-column DataFrame
    stocks_df = pd.concat(extracted_stocks, axis=1)

    # 3. Strip timezone data cleanly (ensures perfect stringless date matching)
    stocks_df.index = pd.to_datetime(stocks_df.index).tz_localize(None)
    SP500.index = pd.to_datetime(SP500.index).tz_localize(None)

    # 4. Reset indices so 'Date' becomes an actual column for merging
    stocks_df.reset_index(inplace=True)
    SP500.reset_index(inplace=True)

    # 5. Perform the LEFT JOIN 
    # (SP500 is left, keeping all historical S&P dates. Missing stock data becomes NaN)
    final_df = pd.merge(SP500, stocks_df, on='Date', how='left')

    cols = [col for col in final_df.columns if col != 'sp500'] + ['sp500']
    final_df = final_df[cols]


    # # =====================================================================
    # # DATA CHECK SECTION
    # # =====================================================================
    # print("\n=== 1. DATAFRAME HEAD (First 5 Rows) ===")
    # print(final_df.head())

    # print("\n=== 2. DATAFRAME TAIL (Last 5 Rows) ===")
    # print(final_df.tail())

    # print("\n=== 3. DATA TYPES ===")
    # print(final_df.dtypes)

    # print("\n=== 4. MISSING VALUES COUNT (NaNs) ===")
    # # This tells you exactly how many days of missing data each stock has over the 15-year S&P timeline
    # print(final_df.isna().sum())

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("### Data Head")
        st.dataframe(final_df.head(), use_container_width = True)
    with col2:
        st.markdown("### Data Tail")
        st.dataframe(final_df.tail(), use_container_width = True)

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('### Price of all Stocks')
        st.plotly_chart(capm_functions.interactive_plot(final_df), use_container_width = True)
    with col2:
        st.markdown('### Normalized Stock Performance')
        # 1. First normalize your prices using the correct function name
        normalized_prices = capm_functions.normalize_prices(final_df)
        # 2. Pass those normalized prices into your plotting function using Streamlit
        st.plotly_chart(capm_functions.interactive_plot(normalized_prices), use_container_width = True)

    daily_returns_df = capm_functions.daily_returns(final_df)
    print(daily_returns_df.head())

    beta = {}
    alpha = {}

    for i in daily_returns_df.columns:
        if i != 'Date' and i != 'sp500':
            b, a = capm_functions.calculate_beta(daily_returns_df, i)

            beta[i] = b
            alpha[i] = a

    print(beta, alpha)

    beta_df = pd.DataFrame(columns = ['Stock', 'Beta Value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta Value'] = [str(round(i, 2)) for i in beta.values()]

    with col1:
        st.markdown('### Calculated Beta Values')
        st.dataframe(beta_df, use_container_width = True)

    rf = 0
    rm = daily_returns_df['sp500'].mean() * 252

    return_df = pd.DataFrame()
    return_value = []
    for stock, value in beta.items():
        return_value.append(str(round((rf + value * (rm - rf) * 100), 2)))

    return_df['Stock'] = stockslist
    return_df['Expected Return'] = return_value

    with col2:
        st.markdown('### Calculated Return using CAPM')
        st.dataframe(return_df, use_container_width = True)
except:
    st.write("Please select at least one stock and specify the number of years to analyze.")