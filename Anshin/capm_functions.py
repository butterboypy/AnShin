import numpy as np
import plotly.express as px
import plotly.graph_objects as go


###function to plot interaactive plotly charts
def interactive_plot(df):
    fig = go.Figure()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
    fig.update_layout(width = 450, 
                      margin = dict(l=20, r=20, t=50, b=20), 
                      legend = dict(orientation = 'h', 
                                    yanchor = 'bottom', 
                                    y=1.02, xanchor = 'right', x = 1)
                    )
    return fig

#function to normalize the prices based on the inital price
def normalize_prices(df):
    normalized_df = df.copy()
    for col in df.columns[1:]:
        normalized_df[col] = df[col] / df[col].iloc[0]
    return normalized_df


# #function to calculate daily returns
# def daily_returns(df):
#     returns_df = df.copy()
#     for col in df.columns[1:]:
#         for i in range(1, len(df)):
#             returns_df[col].iloc[i] = ((df[col].iloc[i] / df[col].iloc[i-1]) - 1) * 100
#     return returns_df


# Function to calculate daily returns 
def daily_returns(df):
    returns_df = df.copy()
    
    for col in returns_df.columns:
        if col == 'Date':
            continue  # Explicitly skips the date column
        # .pct_change()  - (Today / Yesterday) - 1) formula instantly without loop
        returns_df[col] = returns_df[col].pct_change()
    #Dropping first row, making it NaN and resetting index    
    return returns_df.dropna().reset_index(drop=True)

#function to calculate beta
def calculate_beta(daily_returns_df, stock):
    rm = daily_returns_df['sp500'].mean() * 252
    
    b, a = np.polyfit(daily_returns_df['sp500'], daily_returns_df[stock], 1)
    return b, a