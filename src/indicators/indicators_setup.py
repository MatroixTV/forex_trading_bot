import pandas as pd
import numpy as np

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(series, fast=12, slow=26, signal=9):
    fast_ema = series.ewm(span=fast, min_periods=1).mean()
    slow_ema = series.ewm(span=slow, min_periods=1).mean()
    macd = fast_ema - slow_ema
    signal_line = macd.ewm(span=signal, min_periods=1).mean()
    return macd, signal_line

def calculate_bollinger_bands(series, window=20):
    sma = series.rolling(window=window).mean()
    std = series.rolling(window=window).std()
    upper_band = sma + (2 * std)
    lower_band = sma - (2 * std)
    return upper_band, lower_band

def calculate_xmode(series):
    rolling_mean = series.rolling(window=14).mean()
    rolling_std = series.rolling(window=14).std()
    return (series - rolling_mean) / rolling_std

def add_indicators(df):
    if "Close" not in df.columns:
        raise KeyError("The dataframe does not contain a 'Close' column.")

    df["RSI"] = calculate_rsi(df["Close"], 14)
    df["MACD"], df["MACD_Signal"] = calculate_macd(df["Close"])
    df["BB_Upper"], df["BB_Lower"] = calculate_bollinger_bands(df["Close"])
    df["XMODE"] = calculate_xmode(df["Close"])

    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)

    return df
