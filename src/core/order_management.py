# src/core/order_management.py

import MetaTrader5 as mt5


def place_order(symbol, volume, order_type, price, sl, tp):
    if order_type == "buy":
        action_type = mt5.TRADE_ACTION_BUY
    elif order_type == "sell":
        action_type = mt5.TRADE_ACTION_SELL
    else:
        raise ValueError("Invalid order type")

    # Define the trade request structure
    request = {
        "action": action_type,
        "symbol": symbol,
        "volume": volume,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 20,  # Example deviation value
        "type": mt5.ORDER_TYPE_BUY if order_type == "buy" else mt5.ORDER_TYPE_SELL,
        "type_filling": mt5.ORDER_FILLING_IOC,
        "type_time": mt5.ORDER_TIME_GTC,
        "expiration": 0,
        "comment": f"Test {order_type.capitalize()} Order",
        "position": 0,
        "magic": 234000,  # Unique magic number for the EA
        "position_by": 0
    }

    # Place the order
    result = mt5.order_send(request)

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed with error code: {result.retcode}")
    else:
        print(f"Order placed successfully: {result}")

    return result  # Return the result for further analysis or logging


# src/core/order_management.py

def manage_trade(symbol, account_balance, risk_per_trade, price, sl, tp):
    """ Manages the trade logic, including risk management and order placement. """
    # Calculate the position size based on risk management (example: 1% of account balance)
    position_size = (account_balance * risk_per_trade) / (tp - sl)  # Example formula for position size
    print(f"Managing trade for {symbol} with position size: {position_size}")

    # Place the order
    order_result = place_order(symbol, position_size, "buy", price, sl, tp)  # For a buy order
    return order_result
