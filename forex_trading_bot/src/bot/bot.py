# src/bot.py

class Bot:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance  # Starting account balance
        self.position = 0  # Current position (0 means no open position)
        self.buy_price = 0  # Price when we bought the asset
        self.data = None  # Placeholder for the market data
        self.trades = []  # List to store the trades

    def load_data(self, data):
        """ Load historical market data into the bot. """
        self.data = data

    def trade_logic(self):
        """ Implement basic buy/sell logic for the bot. """
        # For now, just a simple example: Buy when RSI is below 30, sell when above 70.
        # This will be expanded later with more complex strategies.

        for i in range(1, len(self.data)):
            # Example: Simple buy logic
            if self.data['RSI'][i] < 30 and self.position == 0:  # Buy signal
                self.buy_price = self.data['close'][i]
                self.position = self.balance / self.buy_price  # Buy the asset
                print(f"Buy at {self.buy_price}")

            # Example: Simple sell logic
            elif self.data['RSI'][i] > 70 and self.position > 0:  # Sell signal
                sell_price = self.data['close'][i]
                profit = (sell_price - self.buy_price) * self.position  # Calculate profit
                self.balance += profit  # Update the balance
                self.position = 0  # Reset position
                print(f"Sell at {sell_price} | Profit: {profit}")

            self.trades.append({
                'timestamp': self.data['timestamp'][i],
                'position': self.position,
                'balance': self.balance,
                'buy_price': self.buy_price if self.position > 0 else None,
                'sell_price': sell_price if self.position == 0 else None,
            })

    def get_balance(self):
        """ Return the current balance of the bot. """
        return self.balance

    def get_trades(self):
        """ Return the list of trades executed by the bot. """
        return self.trades
