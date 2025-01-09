import yfinance as yf
import pandas as pd

# Configuration
SYMBOL = 'EURUSD=X'  # Yahoo Finance ticker for EUR/USD
INTERVAL = '15m'      # Interval (1m = 1 minute data)
PERIOD = '1mo'        # Time period (e.g., '5d' for 5 days)

# Filepath for saving raw data
RAW_FILE = 'C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD_raw.csv'


def fetch_raw_data():
    try:
        # Fetch historical data
        print(f"Fetching historical data for {SYMBOL}...")
        data = yf.download(tickers=SYMBOL, interval=INTERVAL, period=PERIOD)

        # Display raw data preview
        print("Raw data preview:")
        print(data.head())

        # Save raw data directly without any processing
        data.to_csv(RAW_FILE)
        print(f"Raw data saved successfully to {RAW_FILE}")

    except Exception as e:
        print(f"Error fetching historical data: {e}")


# Execute the function
fetch_raw_data()


# import yfinance as yf
# import pandas as pd
#
# # Fetch historical data
# def fetch_data(symbol='EURUSD=X', interval='1m', period='7d', save_path='data/EURUSD_raw.csv'):
#     try:
#         print(f"Fetching historical data for {symbol}...")
#         data = yf.download(tickers=symbol, interval=interval, period=period, group_by='ticker')
#
#         if data.empty:
#             print("No data fetched. Please check symbol and internet connection.")
#             return
#
#         # Reset index to make 'Datetime' a column
#         data.reset_index(inplace=True)
#
#         # Flatten multi-index columns
#         data.columns = ['Datetime'] + [col[1] if isinstance(col, tuple) else col for col in data.columns[1:]]
#
#         # Rename columns explicitly
#         rename_columns = {
#             'Open': 'Open',
#             'High': 'High',
#             'Low': 'Low',
#             'Close': 'Close',
#             'Adj Close': 'Close',
#             'Volume': 'Volume'
#         }
#         data.rename(columns=rename_columns, inplace=True)
#
#         # Fill missing values for Open, High, Low, and Close with 'Close' value
#         for col in ['Open', 'High', 'Low', 'Close']:
#             data[col] = data[col].fillna(data['Close'])
#
#         # Save raw data
#         data.to_csv(save_path, index=False)
#         print(f"Data saved successfully to {save_path}")
#
#     except Exception as e:
#         print(f"Error fetching historical data: {e}")
#
#
# # Main Execution
# fetch_data()
