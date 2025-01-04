import os
import pandas as pd

# Use the absolute file path to the CSV file
file_path = "C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD_2024-12-25_17-57-19.csv"

# Print the current working directory for verification
print("Current working directory:", os.getcwd())

# Load the data
try:
    df = pd.read_csv(file_path)
    print(f"Data successfully loaded from {file_path}")
    print(df.head())  # Display the first few rows of the data
except FileNotFoundError as e:
    print(f"Error: {e}")
