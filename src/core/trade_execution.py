# trade_execution.py

import pandas as pd

def execute_trade(df, account_balance, risk_per_trade=0.02):
    df['Position_Size'] = (account_balance * risk_per_trade) / df['ATR']
    balance = account_balance
    position = 0
    buy_price = 0

    for i in range(1, len(df)):
        if df['Buy_Signal'].iloc[i] and position == 0:
            position = df['Position_Size'].iloc[i]
            buy_price = df['close'].iloc[i]
            print(f"Buy at {buy_price}, position size: {position}")

        elif df['Sell_Signal'].iloc[i] and position > 0:
            sell_price = df['close'].iloc[i]
            profit = (sell_price - buy_price) * position
            balance += profit
            position = 0
            print(f"Sell at {sell_price}, profit: {profit}, balance: {balance}")

    return balance
