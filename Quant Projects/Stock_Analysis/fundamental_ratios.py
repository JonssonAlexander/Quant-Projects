import FundamentalAnalysis as fa
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
#from config import fundamentalanalysis_api_key as fb

# Set the Yahoo Finance API key
yf.pdr_override()
api_key='37418e186027a6d524184bc33919b3b2'

# Define a list of stocks to fetch financial data for
ticker_list = ['INVE-B.ST']

# Download financial indicators data and output as Excel files for each stock
for ticker in ticker_list:
    # Get key metrics
    key_metrics_annually = fa.key_metrics(ticker, api_key,period="annual")
    # Save key metrics data to an Excel file
    with pd.ExcelWriter(f'Bot/Stock_Analysis/Financial_Ratios/{ticker}_key_metrics.xlsx') as writer:
        key_metrics_annually.to_excel(writer, ticker)

    # Get financial ratios
    financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")
    # Save financial ratios data to an Excel file
    with pd.ExcelWriter(f'Bot/Stock_Analysis/Financial_Ratios/{ticker}_financial_ratios.xlsx') as writer:
        financial_ratios_annually.to_excel(writer, ticker)
    print('Percent done:')
    print('{:.1f} % of 100%'.format(100*(int(ticker_list.index(ticker))/len(ticker_list))))

# Download stock prices for the specified date range
data = pdr.get_data_yahoo(ticker_list, start="2017-01-01")
price = data.loc[:, 'Close']
# Save stock prices data to an Excel file
price.to_excel(f'{ticker}_price.xlsx')
