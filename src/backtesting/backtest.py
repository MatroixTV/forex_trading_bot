import pandas as pd
import numpy as np
from src.strategies.strategy_logic import trading_logic
from src.indicators.indicators_setup import add_indicators  # Ensure this import exists

def backtest(data):
    initial_balance = 10000
    balance = initial_balance
    position = None

    for index, row in data.iterrows():
        if row["Buy_Signal"] and position is None:
            position = row["Close"]
            print(f"Buy at {position:.2f}")
        elif row["Sell_Signal"] and position is not None:
            profit = row["Close"] - position
            balance += profit
            print(f"Sell at {row['Close']:.2f}")
            position = None

    return balance


# Example usage (replace with your dataset loading logic)
data = pd.read_csv("C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD.csv")
data = add_indicators(data)  # Ensure this function works correctly
final_balance = backtest(data)




# C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD.csv