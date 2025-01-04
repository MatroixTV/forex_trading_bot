import pandas as pd

# EMA Setup
def calculate_ema(df, short_span=12, long_span=26):
    df['EMA_Short'] = df['close'].ewm(span=short_span, adjust=False).mean()
    df['EMA_Long'] = df['close'].ewm(span=long_span, adjust=False).mean()
    return df

def calculate_rsi(df, period=14):
    # Calculate price differences
    delta = df['close'].diff()

    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate the average gain and loss over the period
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    # Calculate RS (Relative Strength)
    rs = avg_gain / avg_loss

    # Calculate RSI
    df['RSI'] = 100 - (100 / (1 + rs))
    return df