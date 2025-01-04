import os
import sys
import pandas as pd
import yfinance as yf  # Import Yahoo Finance library

# Explicitly add the src directory to the sys.path
sys.path.append('C:/Users/ismac/PycharmProjects/forex_trading_bot/src')

# Access the environment variable for the project directory
project_directory = os.getenv('PROJECT_DIRECTORY_1')  # For ismac
if project_directory is None:
    print("Environment variable 'PROJECT_DIRECTORY_1' is not set. Using default path.")
    project_directory = 'C:/Users/ismac/PycharmProjects/forex_trading_bot'  # For ismac

# Set data file path
data_file = os.path.join(project_directory, 'data', 'EURUSD.csv')

# Download EURUSD data using Yahoo Finance
ticker = 'EURUSD=X'  # Yahoo Finance symbol for EUR/USD
interval = '1d'      # Use '1d' for daily data or '1h' for shorter range
start_date = '2020-01-01'  # Start date
end_date = '2024-12-25'    # End date (adjust if using intraday)

print(f"Downloading data for {ticker} from {start_date} to {end_date}...")

# Fetch data from Yahoo Finance
data = yf.download(ticker, interval=interval, start=start_date, end=end_date)

# Check if data is empty
if data.empty:
    raise ValueError(f"No data found for {ticker}. Check the date range or interval.")

# Standardize column names
data.reset_index(inplace=True)
data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']  # Fixed column count

# Save the data to CSV
data.to_csv(data_file, index=False)

print(f"Data collected and saved to: {data_file}")
