# Updated strategy_logic.py
import pandas as pd


class TradingStrategy:
    def __init__(self, data_row, full_data):
        self.data_row = data_row
        self.full_data = full_data

    def generate_signals(self):
        close_price = self.data_row['Close']
        rsi = self.data_row['RSI']
        macd = self.data_row['MACD']
        macd_signal = self.data_row['MACD_Signal']
        xmode = self.data_row['XMODE']
        atr = self.data_row['ATR']

        buy_signal = False
        sell_signal = False

        # Example logic: RSI oversold and MACD bullish crossover
        if rsi < 30 and macd > macd_signal and xmode > 0:
            buy_signal = True

        # Example logic: RSI overbought and MACD bearish crossover
        elif rsi > 70 and macd < macd_signal and xmode < 0:
            sell_signal = True

        return buy_signal, sell_signal

    def stop_loss_take_profit(self, buy_price, risk_ratio=1.5):
        atr = self.data_row['ATR']
        stop_loss = buy_price - (atr * risk_ratio)
        take_profit = buy_price + (atr * risk_ratio)
        return stop_loss, take_profit


# Example usage within backtest logic
import numpy as np

def trading_logic(row, data):
    signal = None
    sl = None  # Stop Loss
    tp = None  # Take Profit

    # Example conditions using RSI, MACD, and XMODE
    if row["RSI"] < 30 and row["XMODE"] > 0.7:  # Example XMODE threshold
        signal = "Buy"
        sl = row["Close"] * 0.99  # Example Stop Loss at 1% below entry
        tp = row["Close"] * 1.02  # Example Take Profit at 2% above entry
    elif row["RSI"] > 70 and row["XMODE"] < -0.7:  # Example XMODE threshold
        signal = "Sell"
        sl = row["Close"] * 1.01  # Example Stop Loss at 1% above entry
        tp = row["Close"] * 0.98  # Example Take Profit at 2% below entry

    return signal, sl, tp
