import os
import sys
import pandas as pd
import talib

# Add the src directory to the Python path explicitly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from strategies.strategy_logic import enhanced_rsi_strategy  # Modify this line as per your file structure

# Access project directory
project_directory = os.getenv('PROJECT_DIRECTORY_1', 'C:/Users/ismac/PycharmProjects/forex_trading_bot')
file_path = os.path.join(project_directory, 'data', 'EURUSD.csv')

# Load the data
df = pd.read_csv(file_path)

# Apply the strategy to the data
df = enhanced_rsi_strategy(df)

# Print the resulting DataFrame to verify Buy/Sell signals
print(df[['Date', 'Close', 'RSI', 'Buy_Signal', 'Sell_Signal']].head(20))

# Optionally, plot the signals to visualize
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))

# Plot Close price
plt.subplot(2, 1, 1)
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.title('Close Price')
plt.legend()

# Plot RSI and buy/sell signals
plt.subplot(2, 1, 2)
plt.plot(df['Date'], df['RSI'], label='RSI', color='orange')
plt.axhline(y=70, color='red', linestyle='--', label='Overbought (70)')
plt.axhline(y=30, color='green', linestyle='--', label='Oversold (30)')
plt.scatter(df['Date'][df['Buy_Signal']], df['RSI'][df['Buy_Signal']], label='Buy Signal', marker='^', color='green')
plt.scatter(df['Date'][df['Sell_Signal']], df['RSI'][df['Sell_Signal']], label='Sell Signal', marker='v', color='red')
plt.title('RSI with Buy/Sell Signals')
plt.legend()

plt.tight_layout()
plt.show()
