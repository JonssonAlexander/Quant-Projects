# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import datetime as dt
import yfinance as yf

# Set parameters
stock_ticker = 'AAPL'
higher_bound = 0.3
lower_bound = 0.2
num_of_years = 40

# Set start and end dates for data
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=int(365.25 * num_of_years))

# Retrieve data from Yahoo Finance
def get_stock_data(stock,startdate,enddate,period,interval):
    ticker = stock  
    yf.pdr_override()
    df = yf.download(tickers=stock, start=startdate, end=enddate, interval=interval,period=period)
    df.reset_index(inplace=True) 
    df['date'] = df['Date'].dt.date
    return df
stock_data = get_stock_data(stock_ticker,start_date,end_date,'max','1d')


# Extract stock returns
open_prices = stock_data['Open'].tolist()
open_prices = open_prices[::253] # take every 253rd value starting from the first
df_returns = pd.DataFrame({'Open': open_prices})
df_returns['Return'] = df_returns['Open'].pct_change()
df_returns.dropna(inplace=True)
returns = df_returns['Return'].tolist()

# Plot normal distribution
x = np.linspace(min(returns), 1, 100)
mean = np.mean(returns)
std = np.std(returns)
norm_dist = norm.pdf(x, mean, std)
plt.plot(x, norm_dist)
plt.title(f'Normal Distribution of Returns for {stock_ticker.upper()}')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.show()

# Estimate the probability of returns falling between lower_bound and higher_bound
norm_cdf = norm(mean, std).cdf
prob = round(norm_cdf(higher_bound) - norm_cdf(lower_bound), 4)
print(f'The probability of returns falling between {lower_bound} and {higher_bound} for {stock_ticker.upper()} is: {prob}')