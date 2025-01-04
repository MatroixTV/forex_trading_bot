# strategy_logic.py
import talib
import os
print("Current directory:", os.getcwd())

def trend_following_signal(df):
    # Buy signal when EMA Short crosses above EMA Long and ADX confirms trend strength
    df['Buy_Signal'] = (df['EMA_Short'] > df['EMA_Long']) & (df['ADX'] > 25)
    df['Sell_Signal'] = (df['EMA_Short'] < df['EMA_Long']) | (df['ADX'] < 25)
    return df

def mean_reversion_signal(df):
    # Buy signal when RSI is below 30 and price is below the lower Bollinger Band
    df['Buy_Signal'] = (df['RSI'] < 30) & (df['close'] < df['BB_Lower'])
    df['Sell_Signal'] = (df['RSI'] > 70) & (df['close'] > df['BB_Upper'])
    return df

def breakout_signal(df):
    # Buy signal when price breaks above upper Bollinger Band and Volume is high
    df['Buy_Signal'] = (df['close'] > df['BB_Upper']) & (df['Volume'] > df['Volume'].rolling(window=20).mean())
    df['Sell_Signal'] = (df['close'] < df['BB_Lower'])
    return df

def scalping_signal(df):
    # Buy signal when RSI is below 30 and MACD shows bullish crossover
    df['Buy_Signal'] = (df['RSI'] < 30) & (df['MACD'] > df['MACD_Signal'])
    df['Sell_Signal'] = (df['RSI'] > 70) & (df['MACD'] < df['MACD_Signal'])
    return df

def enhanced_rsi_strategy(df):
    # Calculate RSI and add to dataframe
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)

    # Calculate EMA and ADX
    df['EMA_Short'] = talib.EMA(df['Close'], timeperiod=12)
    df['EMA_Long'] = talib.EMA(df['Close'], timeperiod=26)
    df['ADX'] = talib.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)

    # Buy signal
    df['Buy_Signal'] = (df['RSI'] > 30) & (df['EMA_Short'] > df['EMA_Long']) & (df['ADX'] > 25)

    # Sell signal
    df['Sell_Signal'] = (df['RSI'] < 70) & (df['EMA_Short'] < df['EMA_Long']) & (df['ADX'] < 25)

    return df

# In src/strategies/strategy_logic.py
from strategies.xmode import XModeAlgorithm
from strategies.RTD import check_rtd_trend
from strategies.MAW import check_maw  # Ensure MAW.py has check_maw
from strategies.strategy_logic import enhanced_rsi_strategy

def trading_logic(df):
    df = enhanced_rsi_strategy(df)

    for index, row in df.iterrows():
        if row['Buy_Signal'] or row['Sell_Signal']:
            # Check if the market trend aligns with the signal (RTD)
            if check_rtd_trend(df.loc[index]) == "uptrend" and row['Buy_Signal']:
                if x_mode_check(df.loc[index]) and check_maw(df.loc[index]):
                    # Proceed with buy execution logic
                    print(f"Buy signal confirmed at {row['Date']}")
            elif check_rtd_trend(df.loc[index]) == "downtrend" and row['Sell_Signal']:
                if x_mode_check(df.loc[index]) and check_maw(df.loc[index]):
                    # Proceed with sell execution logic
                    print(f"Sell signal confirmed at {row['Date']}")
