# import plotly.graph_objects as go
# import dateutil
# import pandas_ta as pta
# import datetime

# import plotly.graph_objects as go

# def plotly_table(dataframe):
#     # Setup custom theme parameters at the top
#     headerColor = '#ff8c00'   # <--- CHANGED: Swapped tech blue for professional Dark Orange
#     rowEvenColor = '#f8fafd'  # Soft off-white for even rows 
#     rowOddColor = '#e1efff'   # Soft light blue accent for odd rows 
    
#     fig = go.Figure(data=[go.Table(
#         header=dict(
#             # Automatically applies bold labels to headers cleanly 
#             values=[f"<b>{str(i).replace('_', ' ')}</b>" for i in dataframe.columns],
#             line_color=headerColor, 
#             fill_color=headerColor,
#             align='center', 
#             font=dict(color='white', size=15), 
#             height=35
#         ),
#         cells=dict(
#             values=[dataframe[col] for col in dataframe.columns], 
#             fill_color=[[rowEvenColor if i % 2 == 0 else rowOddColor for i in range(len(dataframe))]],
#             align='left', 
#             line_color=['white'], 
#             font=dict(color='black', size=15)
#         )
#     )])
    
#     fig.update_layout(height=300, margin=dict(l=0, r=0, t=0, b=0))
#     return fig


# # def filter_data(dataframe, num_period):
# #     if num_period == '1mo':
# #         date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
# #     elif num_period == '5d':
# #         date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
# #     elif num_period == '6mo':
# #         date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
# #     elif num_period == '1y':
# #         date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
# #     elif num_period == '5y':
# #         date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
# #     elif num_period == 'ytd':
# #         date = datetime.datetime(dataframe.index[-1].year, 1, 1).strftime('%Y-%m-%d')
# #     else:
# #         date = dataframe.index[0]

# #     return dataframe.reset_index()[dataframe.reset_index()['Date'] > date]

# # def close_chart(dataframe, num_period=False):
# #     if num_period:
# #         dataframe = filter_data(dataframe, num_period)
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'],
# #                              mode='lines',
# #                              name='Open', line = dict( width=2,color = '#5ab7ff')))
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'],
# #                              mode='lines',
# #                              name='Close', line = dict( width=2,color = 'black')))
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'],
# #                              mode='lines', name='High', line = dict( width=2,color = '#0078ff')))
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'],
# #                              mode='lines', name='Low', line = dict( width=2,color = 'red')))
# #     fig.update_xaxes(rangeslider_visible=True)
# #     fig.update_layout(height = 500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor = 'white', paper_bgcolor = '#e1efff', legend=dict(
# #     yanchor="top",
# #     xanchor="right"
# #     ))
# #     return fig

# # def candlestick(dataframe, num_period):
# #     dataframe = filter_data(dataframe, num_period)
# #     fig = go.Figure()
# #     fig.add_trace(go.Candlestick(x=dataframe['Date'],
# #                   open=dataframe['Open'], high=dataframe['High'],
# #                   low=dataframe['Low'], close=dataframe['Close']))

# #     fig.update_layout(showlegend = False, height = 500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor = 'white', paper_bgcolor = '#e1efff')
# #     return fig

# # def RSI(dataframe, num_period):
# #     dataframe['RSI'] = pta.rsi(dataframe['Close'])
# #     dataframe = filter_data(dataframe, num_period)
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(
# #         x=dataframe['Date'],
# #         y=dataframe.RSI, name = 'RSI', marker_color='orange', line = dict( width=2,color = 'orange'),
# #     ))
# #     fig.add_trace(go.Scatter(
# #         x=dataframe['Date'],
# #         y=[70]*len(dataframe), name = 'Overbought', marker_color='red', line = dict( width=2,color = 'red',dash='dash'),
# #     ))
    
# #     fig.add_trace(go.Scatter(
# #         x=dataframe['Date'],
# #         y=[30]*len(dataframe),fill='tonexty', name = 'Oversold', marker_color='#79da84',line = dict( width=2,color = '#79da84',dash='dash')
# #     ))
    
# #     fig.update_layout(yaxis_range=[0,100],
# #         height=200,plot_bgcolor = 'white', paper_bgcolor = '#e1efff', margin=dict(l=0, r=0, t=0, b=0), legend=dict(orientation="h",
# #     yanchor="top",
# #     y=1.02,
# #     xanchor="right",
# #     x=1
# #     ))
# #     return fig

# # def Moving_average(dataframe, num_period):
# #     dataframe['SMA_50'] = pta.sma(dataframe['Close'], 50)
# #     dataframe = filter_data(dataframe, num_period)
# #     fig = go.Figure()
    
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'],
# #                              mode='lines',
# #                              name='Open', line = dict( width=2,color = '#5ab7ff')))
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'],
# #                              mode='lines',
# #                              name='Close', line = dict( width=2,color = 'black')))
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'],
# #                              mode='lines', name='High', line = dict( width=2,color = '#0078ff')))
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'],
# #                              mode='lines', name='Low', line = dict( width=2,color = 'red')))
# #     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['SMA_50'],
# #                              mode='lines', name='SMA 50', line = dict( width=2,color = 'purple')))
                             
# #     fig.update_xaxes(rangeslider_visible=True)
# #     fig.update_layout(height = 500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor = 'white', paper_bgcolor = '#e1efff', legend=dict(
# #     yanchor="top",
# #     xanchor="right"
# #     ))
    
# #     return fig

# # def MACD(dataframe, num_period):
# #     macd = pta.macd(dataframe['Close']).iloc[:,0]
# #     macd_signal = pta.macd(dataframe['Close']).iloc[:,1]
# #     macd_hist = pta.macd(dataframe['Close']).iloc[:,2]
# #     dataframe['MACD'] = macd
# #     dataframe['MACD Signal'] = macd_signal
# #     dataframe['MACD Hist'] = macd_hist
# #     dataframe = filter_data(dataframe, num_period)
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(
# #         x=dataframe['Date'],
# #         y=dataframe['MACD'], name = 'RSI', marker_color='orange', line = dict( width=2,color = 'orange'),
# #     ))
# #     fig.add_trace(go.Scatter(
# #         x=dataframe['Date'],
# #         y=dataframe['MACD Signal'], name = 'Overbought', marker_color='red', line = dict( width=2,color = 'red',dash='dash'),
# #     ))
# #     c = ['red' if cl < 0 else "green" for cl in macd_hist]

# #     fig.update_layout(
# #         height=200,plot_bgcolor = 'white', paper_bgcolor = '#e1efff', margin=dict(l=0, r=0, t=0, b=0), legend=dict(orientation="h",
# #     yanchor="top",
# #     y=1.02,
# #     xanchor="right",
# #     x=1
# #     )
# #     )
# #     return fig

# def filter_data(dataframe, num_period):
#     # Ensure we don't manipulate the original dataframe in place unexpectedly
#     df = dataframe.copy()
    
#     if num_period == '1mo':
#         date = df.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
#     elif num_period == '5d':
#         date = df.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
#     elif num_period == '6mo':
#         date = df.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
#     elif num_period == '1y':
#         date = df.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
#     elif num_period == '5y':
#         date = df.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
#     elif num_period == 'ytd':
#         date = datetime.datetime(df.index[-1].year, 1, 1).strftime('%Y-%m-%d')
#     else:
#         date = df.index[0]

#     # Convert index to 'Date' column safely for Plotly
#     df = df.reset_index()
#     return df[df['Date'] > date]

# def close_chart(dataframe, num_period=False):
#     if num_period:
#         dataframe = filter_data(dataframe, num_period)
#     else:
#         dataframe = dataframe.reset_index()
        
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'], mode='lines', name='Open', line=dict(width=2, color='#5ab7ff')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'], mode='lines', name='Close', line=dict(width=2, color='black')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'], mode='lines', name='High', line=dict(width=2, color='#0078ff')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'], mode='lines', name='Low', line=dict(width=2, color='red')))
    
#     fig.update_xaxes(rangeslider_visible=True)
#     fig.update_layout(font=dict(color="black"),
#                         height=500,
#                         plot_bgcolor='white',
#                         paper_bgcolor='#e1efff',
#                         margin=dict(l=50, r=20, t=20, b=0), # Fixed left margin
#                         legend=dict(yanchor="top", xanchor="right"))
#     return fig

# def candlestick(dataframe, num_period):
#     dataframe = filter_data(dataframe, num_period)
#     fig = go.Figure()
#     fig.add_trace(go.Candlestick(x=dataframe['Date'], open=dataframe['Open'], high=dataframe['High'], low=dataframe['Low'], close=dataframe['Close']))
#     fig.update_layout(showlegend=False, font=dict(color="black"),
#                         height=500,
#                         plot_bgcolor='white',
#                         paper_bgcolor='#e1efff', 
#                         margin=dict(l=50, r=20, t=20, b=0)) # Fixed left margin
#     return fig

# def RSI(dataframe, num_period):
#     df_indicators = dataframe.copy()
#     df_indicators['RSI'] = pta.rsi(df_indicators['Close'])
    
#     dataframe = filter_data(df_indicators, num_period)
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['RSI'], name='RSI', marker_color='orange', line=dict(width=2, color='orange')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=[70]*len(dataframe), name='Overbought', marker_color='red', line=dict(width=2, color='red', dash='dash')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=[30]*len(dataframe), fill='tonexty', name='Oversold', marker_color='#79da84', line=dict(width=2, color='#79da84', dash='dash')))
    
#     fig.update_layout(yaxis_range=[0, 100], font=dict(color="black"),
#                         height=200,
#                         plot_bgcolor='white',
#                         paper_bgcolor='#e1efff', 
#                         margin=dict(l=50, r=20, t=20, b=0), # Fixed margins to align perfectly with price chart
#                         legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1))
#     return fig

# def Moving_average(dataframe, num_period):
#     df_indicators = dataframe.copy()
#     df_indicators['SMA_50'] = pta.sma(df_indicators['Close'], 50)
    
#     dataframe = filter_data(df_indicators, num_period)
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'], mode='lines', name='Open', line=dict(width=2, color='#5ab7ff')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'], mode='lines', name='Close', line=dict(width=2, color='black')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'], mode='lines', name='High', line=dict(width=2, color='#0078ff')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'], mode='lines', name='Low', line=dict(width=2, color='red')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['SMA_50'], mode='lines', name='SMA 50', line=dict(width=2, color='purple')))
                             
#     fig.update_xaxes(rangeslider_visible=True)
#     fig.update_layout(font=dict(color="black"),
#                         height=500,
#                         plot_bgcolor='white',
#                         paper_bgcolor='#e1efff', 
#                         margin=dict(l=50, r=20, t=20, b=0), # Fixed left margin
#                         legend=dict(yanchor="top", xanchor="right"))
#     return fig

# def MACD(dataframe, num_period):
#     df_indicators = dataframe.copy()
#     macd_df = pta.macd(df_indicators['Close'])
    
#     df_indicators['MACD'] = macd_df.iloc[:, 0]
#     df_indicators['MACD Signal'] = macd_df.iloc[:, 1]
#     df_indicators['MACD Hist'] = macd_df.iloc[:, 2]
    
#     dataframe = filter_data(df_indicators, num_period)
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['MACD'], name='MACD Line', line=dict(width=2, color='orange')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['MACD Signal'], name='Signal Line', line=dict(width=2, color='red', dash='dash')))
    
#     c = ['red' if cl < 0 else "green" for cl in dataframe['MACD Hist']]
#     fig.add_trace(go.Bar(x=dataframe['Date'], y=dataframe['MACD Hist'], name='Histogram', marker_color=c))

#     fig.update_layout(font=dict(color="black"),
#                         height=200,
#                         plot_bgcolor='white',
#                         paper_bgcolor='#e1efff', 
#                         margin=dict(l=50, r=20, t=20, b=0), # Fixed margins to align perfectly with price chart
#                         legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1))
#     return fig

# def Moving_average_forecast(forecast):
#     fig = go.Figure()

#     fig.add_trace(go.Scatter(x=forecast.index[:-30], y=forecast['Close'].iloc[:-30],
#                              mode='lines',
#                              name='Close Price', line = dict(width=2, color='black')))
#     fig.add_trace(go.Scatter(x=forecast.index[-31:], y=forecast['Close'].iloc[-31:],
#                              mode='lines', name='Future Close Price', line = dict(width=2, color='red')))

#     fig.update_xaxes(rangeslider_visible=True)
#     fig.update_layout(height=500, 
#                       font=dict(color="black"),
#                       plot_bgcolor='white', 
#                       paper_bgcolor='#e1efff', 
#                       margin=dict(l=50, r=20, t=20, b=0), # Fixed left margin
#                       legend=dict(yanchor="top", xanchor="right"))

#     return fig

import plotly.graph_objects as go
import dateutil
import pandas_ta as pta
import datetime
import pandas as pd

def plotly_table(dataframe):
    headerColor = '#0078ff'   # Royal Blue header matching original theme layout designs
    rowEvenColor = '#f8fafd'
    rowOddColor = '#e1efff'
    
    df_display = dataframe.copy()
    
    # Convert all column names to uppercase strings to check for a metrics table
    upper_cols = [str(c).upper() for c in df_display.columns]
    
    if 'METRICS' in upper_cols:
        # Drop the automatic pandas index columns cleanly
        if 'index' in df_display.columns:
            df_display = df_display.drop(columns=['index'])
        df_display = df_display.reset_index(drop=True)
    else:
        # Keep the standard Date formatting for prediction time-series tables
        if 'Date' not in df_display.columns:
            df_display = df_display.reset_index().rename(columns={'index': 'Date'})
        if pd.api.types.is_datetime64_any_dtype(df_display['Date']):
            df_display['Date'] = df_display['Date'].dt.strftime('%Y-%m-%d')
    

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=[f"<b>{str(i).upper()}</b>" for i in df_display.columns],
            line_color=headerColor, 
            fill_color=headerColor,
            align='center', 
            font=dict(color='white', size=14), 
            height=35
        ),
        cells=dict(
            values=[df_display[col] for col in df_display.columns], 
            fill_color=[[rowEvenColor if i % 2 == 0 else rowOddColor for i in range(len(df_display))]],
            align='center', 
            line_color=['#cbd5e1'], 
            font=dict(color='black', size=13),
            height=28
        )
    )])
    
    fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10))
    return fig

def filter_data(dataframe, num_period):
    df = dataframe.copy()
    if num_period == '' or num_period == 'max':
        df = df.reset_index()
        return df
    
    if num_period == '1d':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(days = -1)
    elif num_period == '5d':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period == '15d':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(days=-15)
    elif num_period == '1mo':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period == '6mo':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period == '1y':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
    elif num_period == '5y':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
    elif num_period == '10y':
        date = df.index[-1] + dateutil.relativedelta.relativedelta(years=-10)
    elif num_period == 'ytd':
        date = datetime.datetime(df.index[-1].year, 1, 1).strftime('%Y-%m-%d')
    else:
        date = df.index[0]

    df = df.reset_index()
    return df[df['Date'] >= date]

def close_chart(dataframe, num_period=False):
    dataframe = filter_data(dataframe, num_period) if num_period else dataframe.reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'], mode='lines', name='Open', line=dict(width=2, color='#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'], mode='lines', name='Close', line=dict(width=2, color='black')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'], mode='lines', name='High', line=dict(width=2, color='#0078ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'], mode='lines', name='Low', line=dict(width=2, color='red')))
    
    fig.update_xaxes(rangeslider_visible=True, tickfont=dict(color="black"), gridcolor="#e2e8f0")
    fig.update_yaxes(tickfont=dict(color="black"), gridcolor="#e2e8f0")
    fig.update_layout(font=dict(color="black"), height=450, plot_bgcolor='white', paper_bgcolor='white',
                      margin=dict(l=50, r=20, t=20, b=40), legend=dict(font=dict(color="black")))
    return fig

def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=dataframe['Date'], open=dataframe['Open'], high=dataframe['High'], low=dataframe['Low'], close=dataframe['Close']))
    fig.update_xaxes(tickfont=dict(color="black"), gridcolor="#e2e8f0")
    fig.update_yaxes(tickfont=dict(color="black"), gridcolor="#e2e8f0")
    fig.update_layout(showlegend=False, font=dict(color="black"), height=450, plot_bgcolor="#e2e2e3", paper_bgcolor="#e2e2e3", margin=dict(l=50, r=20, t=20, b=40))
    return fig

# def RSI(dataframe, num_period):
#     df_indicators = dataframe.copy()
#     df_indicators['RSI'] = pta.rsi(df_indicators['Close'])
#     dataframe = filter_data(df_indicators, num_period)
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['RSI'], name='RSI', marker_color='orange', line=dict(width=2)))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=[70]*len(dataframe), name='Overbought', line=dict(width=1.5, color='red', dash='dash')))
#     fig.add_trace(go.Scatter(x=dataframe['Date'], y=[30]*len(dataframe), fill='tonexty', name='Oversold', line=dict(width=1.5, color='#79da84', dash='dash')))
    
#     fig.update_xaxes(tickfont=dict(color="black"))
#     fig.update_yaxes(yaxis_range=[0, 100], tickfont=dict(color="black"))
#     fig.update_layout(font=dict(color="black"), height=200, plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=50, r=20, t=20, b=40))
#     return fig

def RSI(dataframe, num_period):
    df_indicators = dataframe.copy()
    df_indicators['RSI'] = pta.rsi(df_indicators['Close'])
    dataframe = filter_data(df_indicators, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['RSI'], name='RSI', marker_color='orange', line=dict(width=2)))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=[70]*len(dataframe), name='Overbought', line=dict(width=1.5, color='red', dash='dash')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=[30]*len(dataframe), fill='tonexty', name='Oversold', line=dict(width=1.5, color='#79da84', dash='dash')))
    
    # FIX: Explicitly configure the Y-Axis range parameters using update_yaxes
    fig.update_xaxes(tickfont=dict(color="black"))
    fig.update_yaxes(range=[0, 100], tickfont=dict(color="black"), gridcolor="#e2e8f0")
    
    fig.update_layout(font=dict(color="black"), 
                      height=200, 
                      plot_bgcolor="#e2e2e3", 
                      paper_bgcolor="#e2e2e3", 
                      margin=dict(l=50, r=20, t=20, b=40))
    return fig

def Moving_average(dataframe, num_period):
    df_indicators = dataframe.copy()
    df_indicators['SMA_50'] = pta.sma(df_indicators['Close'], 50)
    dataframe = filter_data(df_indicators, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'], mode='lines', name='Open', line=dict(width=2, color='#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'], mode='lines', name='Close', line=dict(width=2, color='black')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'], mode='lines', name='High', line=dict(width=2, color='#0078ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'], mode='lines', name='Low', line=dict(width=2, color='red')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['SMA_50'], mode='lines', name='SMA 50', line=dict(width=2, color='purple')))
    
    fig.update_xaxes(rangeslider_visible=True, tickfont=dict(color="black"))
    fig.update_yaxes(tickfont=dict(color="black"))
    fig.update_layout(font=dict(color="black"), height=450, plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=50, r=20, t=20, b=40))
    return fig

def MACD(dataframe, num_period):
    df_indicators = dataframe.copy()
    macd_df = pta.macd(df_indicators['Close'])
    df_indicators['MACD'] = macd_df.iloc[:, 0]
    df_indicators['MACD Signal'] = macd_df.iloc[:, 1]
    df_indicators['MACD Hist'] = macd_df.iloc[:, 2]
    
    dataframe = filter_data(df_indicators, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['MACD'], name='MACD Line', line=dict(width=2, color='orange')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['MACD Signal'], name='Signal Line', line=dict(width=2, color='red', dash='dash')))
    c = ['red' if cl < 0 else "green" for cl in dataframe['MACD Hist']]
    fig.add_trace(go.Bar(x=dataframe['Date'], y=dataframe['MACD Hist'], name='Histogram', marker_color=c))

    fig.update_xaxes(tickfont=dict(color="black"))
    fig.update_yaxes(tickfont=dict(color="black"))
    fig.update_layout(font=dict(color="black"), height=200, plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=50, r=20, t=20, b=40))
    return fig

def Moving_average_forecast(forecast):
    fig = go.Figure()
    
    # Ensure index values are converted cleanly to timestamps
    dates = forecast.index
    
    # Separates historical actuals from the 30-day forecast horizon
    fig.add_trace(go.Scatter(x=dates[:-30], y=forecast['Close'].iloc[:-30], mode='lines', name='Historical Data', line=dict(width=2.5, color='black')))
    fig.add_trace(go.Scatter(x=dates[-31:], y=forecast['Close'].iloc[-31:], mode='lines', name='30-Day Forecast', line=dict(width=2.5, color='#ef4444')))

    fig.update_xaxes(rangeslider_visible=False, tickfont=dict(color="black", size=11), gridcolor="#cbd5e1", type='date')
    fig.update_yaxes(tickfont=dict(color="black", size=11), gridcolor="#cbd5e1")
    
    # Configures plot dimensions and forces grid lines to display cleanly
    fig.update_layout(
        font=dict(color="black"),
        height=480, 
        plot_bgcolor='white', 
        paper_bgcolor='white', 
        margin=dict(l=60, r=30, t=20, b=50),
        legend=dict(font=dict(color="black", size=11), yanchor="top", y=0.99, xanchor="left", x=0.01, bgcolor="rgba(255,255,255,0.8)")
    )
    return fig