import sys
import os
# Add the src directory to the Python path explicitly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

import pandas as pd
from strategies.strategy_logic import trend_following_signal, mean_reversion_signal, breakout_signal, scalping_signal, trading_logic, enhanced_rsi_strategy
from core.trade_execution import execute_trade

# Access the environment variable for the project directory
project_directory = os.getenv('PROJECT_DIRECTORY_1')  # For ismac

# If the environment variable is not set, fall back to the default path
if project_directory is None:
    print("Environment variable 'PROJECT_DIRECTORY_1' is not set. Using default path.")
    project_directory = 'C:/Users/ismac/PycharmProjects/forex_trading_bot'

# Verify that the path is correct
print(f"Using project directory: {project_directory}")

# Define the path to the cleaned data file
data_file = os.path.join(project_directory, 'data', 'EURUSD.csv')  # Correct path to cleaned data

# Load the data
df = pd.read_csv(data_file)

# Define a function to calculate indicators (like EMA, RSI, etc.)
def calculate_indicators(df):
    df['EMA_Short'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['EMA_Long'] = df['Close'].ewm(span=26, adjust=False).mean()
    # Add RSI calculation
    df['RSI'] = 100 - (100 / (1 + (df['Close'].diff(1).where(lambda x: x > 0, 0).rolling(window=14).mean() /
                               df['Close'].diff(1).where(lambda x: x < 0, 0).rolling(window=14).mean())))
    return df

# Apply the indicators
df = calculate_indicators(df)

# Apply trading logic with the enhanced strategy
trading_logic(df)

# Backtest the strategy
def backtest(df, initial_balance=10000):
    df = trend_following_signal(df)
    df = mean_reversion_signal(df)
    df = breakout_signal(df)
    df = scalping_signal(df)
    balance = execute_trade(df, initial_balance)
    print(f"Final balance after backtest: {balance}")

# Run the backtest
backtest(df, initial_balance=10000)
