import os
import sys
import pandas as pd

# Explicitly add the src directory to the sys.path
sys.path.append('C:/Users/ismac/PycharmProjects/forex_trading_bot/src')

# Access the environment variable for the project directory
project_directory = os.getenv('PROJECT_DIRECTORY_1')  # For ismac
if project_directory is None:
    print("Environment variable 'PROJECT_DIRECTORY_1' is not set. Using default path.")
    project_directory = 'C:/Users/ismac/PycharmProjects/forex_trading_bot'  # For ismac

# Define the path to the data file using environment variable or default
data_file = os.getenv('DATA_FILE', 'data/EURUSD.csv')

# Verify that the paths are correct
print(f"Using project directory: {project_directory}")
print(f"Using data file: {data_file}")

# Load the data (first row as headers, second row to be dropped)
file_path = os.path.join(project_directory, data_file)

# Read the data and drop the ticker row (row 1)
df = pd.read_csv(file_path, header=0)  # Use first row as headers
df = df.iloc[1:].reset_index(drop=True)  # Drop the second row (tickers)

# Rename headers for consistency
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

# Parse 'Date' column into datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')  # Force conversion

# Drop rows where 'Date' is NaT (invalid dates)
df = df.dropna(subset=['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Print columns to verify changes
print("Final columns in the data:", df.columns)

# Display the first few rows of the cleaned data
print(df.head())

# Save the cleaned data to a new CSV file
cleaned_file_path = os.path.join(project_directory, 'data', 'EURUSD.csv')
df.to_csv(cleaned_file_path)

print(f"Cleaned data saved to {cleaned_file_path}")
