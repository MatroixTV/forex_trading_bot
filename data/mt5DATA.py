import MetaTrader5 as mt5
import pandas as pd

# Ensure MetaTrader5 is initialized
if not mt5.initialize():
    print("MetaTrader5 initialization failed")
    mt5.shutdown()
else:
    print("MetaTrader5 initialized successfully")

# Fetch real-time data for EUR/USD
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_M1  # Use the appropriate timeframe
rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1000)

# Fetch real-time bid and ask prices
tick = mt5.symbol_info_tick(symbol)
ask = tick.ask if tick else None
bid = tick.bid if tick else None

# Convert to a pandas DataFrame
df = pd.DataFrame(rates)

# Convert 'time' to a readable datetime format
df['time'] = pd.to_datetime(df['time'], unit='s')

# Set time as the index
df.set_index('time', inplace=True)

# Add tick data (bid, ask) to the dataframe
df['ask'] = ask
df['bid'] = bid
df['spread'] = df['ask'] - df['bid']  # Calculate the spread

# Display the fetched data
print(df.head())

# Now include the missing columns (Tick_volume, Spread, Real_volume)
df['Tick_volume'] = df['tick_volume']
df['Real_volume'] = df['real_volume']

# Verify that the required columns are now present
print("Columns in DataFrame:", df.columns)
