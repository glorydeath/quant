from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
from indicators.ema import EMA
from indicators.macd import MACD
from indicators.rsi import RSI
from strategies.ema_crossing import EMA_Crossing
import numpy as np

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2018 until 04/01/2020.
start_date = '2018-01-01'
end_date = '2020-04-01'

def get_single_data(ticker, start_date, end_date):
    panel_data = data.DataReader(ticker, 'yahoo', start_date, end_date)

    print(panel_data.head(9))

def get_data(tickers, start_date, end_date):
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    panel_data = data.DataReader(tickers, 'yahoo', start_date, end_date)

    # print(panel_data.head(9))


    # Getting just the adjusted closing prices. This will return a Pandas DataFrame
    # The index in this DataFrame is the major index of the panel_data.
    close = panel_data['Close']

    data_open = panel_data['Open']

    # Getting all weekdays between 01/01/2000 and 12/31/2016
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

    # How do we align the existing prices in adj_close with our new set of dates?
    # All we need to do is reindex close using all_weekdays as the new index
    close = close.reindex(all_weekdays)
    data_open = data_open.reindex(all_weekdays)

    # Reindexing will insert missing values (NaN) for the dates that were not present
    # in the original set. To cope with this, we can fill the missing by replacing them
    # with the latest available price for each instrument.
    close = close.fillna(method='ffill')
    data_open = data_open.fillna(method='ffill')


    # close.head(10)

    # close.describe()
    return close, data_open

# data is Series
data, data_open = get_data('MSFT', start_date, end_date)

ema_crossing = EMA_Crossing()
ema_crossing.get_transaction_point(data, 13, 34)


# ema = EMA()
#
# # ema_13 is Series
# ema_3 = ema.get_ema(data, 3)
# ema_13 = ema.get_ema(data, 13)
# ema_34 = ema.get_ema(data, 34)
#
# macd = MACD()
#
# macd_line = macd.get_macd(data)
#
# rsi = RSI()
#
# rsi = rsi.get_rsi(data, 14)
# print(rsi)
#
# # print(ema_13)
# df = pd.DataFrame({'date': ema_13.index, 'ema_3': ema_3.values, 'ema_13': ema_13.values, 'ema_34': ema_34.values, 'macd': macd_line.values})
# df.set_index('date', inplace=True, drop=True)
# df.index = pd.to_datetime(df.index)
# # print(df.head(10))
# df.plot()
# plt.show()

# get_data(tickers, start_date, end_date)
