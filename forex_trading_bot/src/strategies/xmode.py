import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class XModeAlgorithm:
    def __init__(self, lookbacks=[128, 32, 16, 8]):
        self.lookbacks = lookbacks

    def calculate_levels(self, data, lookback):
        high = data['High']
        low = data['Low']
        v_low = low.rolling(window=lookback).min()
        v_high = high.rolling(window=lookback).max()
        v_dist = v_high - v_low

        tmp_high = np.where(v_low < 0, 0 - v_low, v_high)
        tmp_low = np.where(v_low < 0, 0 - v_low - v_dist, v_low)

        sf_var = np.log(0.4 * tmp_high) / np.log(10)
        SR = np.where(tmp_high > 25, np.exp(np.log(10) * (np.floor(sf_var) + 1)),
                      100 * np.exp(np.log(8) * np.floor(np.log(0.005 * tmp_high) / np.log(8))))

        N = np.floor(np.log(SR / (tmp_high - tmp_low)) / np.log(8))
        SI = SR * np.exp(-N * np.log(8))
        M = np.floor(np.log((tmp_high - tmp_low) / SI) / np.log(2))
        I = np.round((tmp_high + tmp_low) * 0.5 / (SI * np.exp((M - 1) * np.log(2))))

        Bot = (I - 1) * SI * np.exp((M - 1) * np.log(2))
        Top = (I + 1) * SI * np.exp((M - 1) * np.log(2))

        Increment = (Top - Bot) / 8
        absTop = Top + 3 * Increment

        levels = {
            'Plus28': absTop - Increment,
            'Plus18': absTop - 2 * Increment,
            'EightEight': absTop - 3 * Increment,
            'FiveEight': absTop - 6 * Increment,
            'FourEight': absTop - 7 * Increment,
            'ThreeEight': absTop - 8 * Increment,
            'ZeroEight': absTop - 11 * Increment,
            'Minus18': absTop - 12 * Increment,
            'Minus28': absTop - 13 * Increment
        }
        return levels

    def plot_levels(self, data, levels, label):
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Price')
        for level_name, level_value in levels.items():
            plt.axhline(y=level_value, linestyle='--', label=f'{label} - {level_name}')
        plt.title(f'Murrey Math Levels - {label}')
        plt.legend()
        plt.show()

    def run(self, data):
        for lookback in self.lookbacks:
            levels = self.calculate_levels(data, lookback)
            self.plot_levels(data, levels, label=f'Lookback {lookback}')


# x_mode_check function for generating trading signals based on the levels
def x_mode_check(df):
    # Initialize the XModeAlgorithm class with the desired lookback periods
    x_mode = XModeAlgorithm(lookbacks=[128, 32, 16, 8])

    # Run the algorithm on the data to calculate the levels
    x_mode.run(df)

    # Example logic to check whether to buy or sell
    # You can modify this logic based on your strategy needs
    latest_data = df.iloc[-1]

    # Example: If the price is above the 'Plus28' level, consider it a buy signal
    if latest_data['Close'] > x_mode.calculate_levels(df, 128)['Plus28']:
        print("Buy Signal: Price is above the Plus28 level")
        return 'Buy'
    # Example: If the price is below the 'Minus28' level, consider it a sell signal
    elif latest_data['Close'] < x_mode.calculate_levels(df, 128)['Minus28']:
        print("Sell Signal: Price is below the Minus28 level")
        return 'Sell'
    else:
        print("No Signal: Price is within range")
        return 'Hold'


