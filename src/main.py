import pandas as pd
from src.backtesting.backtest import backtest
from src.indicators.indicators_setup import add_indicators

# Main script execution
if __name__ == "__main__":
    # Load your data
    data_file_path = "path/to/your/data.csv"  # Replace with actual file path
    data = pd.read_csv(data_file_path)

    # Add indicators to data
    data = add_indicators(data)

    # Run the backtest
    final_balance = backtest(data)
    print(f"Final Balance: ${final_balance:.2f}")
