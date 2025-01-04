# main.py
from src.bot.bot import ForexBot
from src.strategies.strategy_logic import Scalping

# Sample mock data (replace this with real data in the future)
import pandas as pd
data = pd.DataFrame({
    'timestamp': ['2024-07-25', '2024-07-26'],
    'RSI': [25, 75],
    'EMA_Short': [1.085, 1.088],
    'EMA_Long': [1.085, 1.087],
    'close': [1.08513, 1.086],
})
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

# Create the strategy and bot
strategy = Scalping()
bot = ForexBot(data, strategy, None)

# Run the bot
bot.run()

import numpy as np
import pandas as pd


# Define trading signals based on indicators
def create_signals(df):
    # Buy signal when RSI is below 30 and EMA short crosses above EMA long
    df['Buy_Signal'] = (df['RSI'] < 30) & (df['EMA_Short'] > df['EMA_Long'])

    # Sell signal when RSI is above 70 and EMA short crosses below EMA long
    df['Sell_Signal'] = (df['RSI'] > 70) & (df['EMA_Short'] < df['EMA_Long'])

    # You can add more conditions here as needed

    # For example, use ATR to filter trades or other indicators (e.g., MACD, Bollinger Bands)
    return df


# Function to calculate position size based on risk and ATR
def calculate_position_size(account_balance, risk_per_trade, atr_value, current_price):
    position_size = (account_balance * risk_per_trade) / atr_value
    return position_size


# Function to simulate trading (buy/sell logic)
def trade_logic(df, account_balance, risk_per_trade):
    position = 0  # Initial position size
    buy_price = 0  # Initial price at buy time

    for index, row in df.iterrows():
        # Buy logic: when Buy_Signal is True and position is 0 (no current position)
        if row['Buy_Signal'] and position == 0:
            position_size = calculate_position_size(account_balance, risk_per_trade, row['ATR'], row['close'])
            position = position_size  # Set position to the calculated size
            buy_price = row['close']  # Save the buy price
            account_balance -= position * buy_price  # Subtract the cost of the position from account balance

        # Sell logic: when Sell_Signal is True and position is greater than 0 (already in a position)
        elif row['Sell_Signal'] and position > 0:
            profit_loss = (row['close'] - buy_price) * position  # Calculate profit or loss
            account_balance += profit_loss  # Update account balance with profit/loss
            position = 0  # Reset position to 0 (no position after selling)

    return account_balance


# Example usage
account_balance = 10000  # Starting balance
risk_per_trade = 0.01  # Risk per trade (1%)

# Create signals
df = create_signals(df)

# Simulate trading based on buy/sell signals
final_balance = trade_logic(df, account_balance, risk_per_trade)

print(f"Final Account Balance: ${final_balance}")
