import MetaTrader5 as mt5
import pandas as pd

# Initialize connection to MetaTrader 5
if not mt5.initialize():
    print("MetaTrader5 initialization failed. Error code:", mt5.last_error())
else:
    print("MetaTrader5 initialized successfully.")

    # Check if EURUSD is available in symbols
    symbols = mt5.symbols_get()
    available_symbols = [symbol.name for symbol in symbols]
    print("Available symbols:", available_symbols)

    # Ensure EURUSD is in the available symbols list
    if "EURUSD" in available_symbols:
        print("EURUSD symbol is available. Fetching data...")

        # Get the last 1000 bars for EURUSD
        symbol = "EURUSD"
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 1000)

        if len(rates) > 0:
            # Convert the data into a DataFrame
            df = pd.DataFrame(rates)

            # Convert the 'time' column from Unix timestamp to datetime
            df['time'] = pd.to_datetime(df['time'], unit='s')

            # Set 'time' as the index
            df.set_index('time', inplace=True)

            # Display the DataFrame
            print(df.head())
        else:
            print("No data available for EURUSD.")

    else:
        print("EURUSD symbol not found in the available symbols.")
