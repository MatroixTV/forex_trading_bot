# import pandas as pd
#
# # Load Ismail's CSV
# file_path_ismail = 'C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD_raw.csv'
# df_ismail = pd.read_csv(file_path_ismail)
#
# # Rename columns to match Haidar's format
# df_ismail.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
#
# # Drop first two rows
# df_ismail = df_ismail.iloc[2:]
#
# # Convert 'Date' to datetime format
# df_ismail['Date'] = pd.to_datetime(df_ismail['Date'])
#
# # Ensure numeric columns are floats
# numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
# df_ismail[numeric_cols] = df_ismail[numeric_cols].astype(float)
#
# # Sort by 'Date'
# df_ismail = df_ismail.sort_values(by='Date')
#
# # Save cleaned file (optional)
# output_path = 'C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD.csv'
# df_ismail.to_csv(output_path, index=False)
#
# # Print result
# print(df_ismail.head())
# print("Columns in Ismail's DataFrame:", df_ismail.columns)
#

import pandas as pd

# Load Ismail's CSV
file_path_ismail = 'C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD_raw.csv'
df_ismail = pd.read_csv(file_path_ismail)

# Rename columns to match Haidar's format
df_ismail.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Drop first two rows
df_ismail = df_ismail.iloc[2:]

# Convert 'Date' to datetime format
df_ismail['Date'] = pd.to_datetime(df_ismail['Date'])

# Ensure numeric columns are floats
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
df_ismail[numeric_cols] = df_ismail[numeric_cols].astype(float)

# **New Function: Fill Volume with a small default value if 0 or NaN**
def fix_volume(df, default_value=1.0):
    """
    Fixes volume data by replacing 0 or NaN values with a default value.
    Args:
        df (pd.DataFrame): The data frame containing 'Volume'.
        default_value (float): Default value to fill in case of 0 or NaN.
    Returns:
        pd.DataFrame: Updated DataFrame with fixed volume data.
    """
    df['Volume'] = df['Volume'].replace(0, default_value)  # Replace 0 with default
    df['Volume'].fillna(default_value, inplace=True)  # Replace NaN with default
    return df

# Apply volume fix
df_ismail = fix_volume(df_ismail)

# Sort by 'Date'
df_ismail = df_ismail.sort_values(by='Date')

# Save cleaned file (optional)
output_path = 'C:/Users/ismac/PycharmProjects/forex_trading_bot/data/EURUSD.csv'
df_ismail.to_csv(output_path, index=False)

# Print result
print(df_ismail.head())
print("Columns in Ismail's DataFrame:", df_ismail.columns)
