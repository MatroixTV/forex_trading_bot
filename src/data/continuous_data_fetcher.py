import MetaTrader5 as mt5
import pandas as pd
import time
import os


def initialize_mt5():
    # Initialize MetaTrader 5
    if not mt5.initialize():
        print("MetaTrader5 initialization failed.")
        mt5.shutdown()
        return False
    else:
        print("MetaTrader5 initialized successfully.")
        return True


def fetch_real_time_price(symbol="EURUSD"):
    # Fetch real-time market data
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 1)  # 1-minute data
    if rates:
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        return df
    else:
        print(f"Failed to fetch data for {symbol}")
        return None


def save_to_csv(df, file_path="C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD_real_time.csv"):
    if os.path.exists(file_path):
        # If the file already exists, append new data
        df.to_csv(file_path, mode='a', header=False)
    else:
        # If the file doesn't exist, create it and write the header
        df.to_csv(file_path)


def main():
    # Initialize MT5 connection
    if not initialize_mt5():
        return

    symbol = "EURUSD"

    # Continuously fetch data and save to CSV
    try:
        while True:
            df = fetch_real_time_price(symbol)
            if df is not None:
                print(f"Real-time price for {symbol}: {df['close'].iloc[-1]}")
                save_to_csv(df)  # Save the data to the real-time CSV file

            time.sleep(10)  # Fetch data every 10 seconds (or adjust as needed)

    except KeyboardInterrupt:
        print("Process interrupted by user.")

    finally:
        mt5.shutdown()  # Close MT5 connection on exit


if __name__ == "__main__":
    main()
