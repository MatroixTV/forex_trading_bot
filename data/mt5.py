# import MetaTrader5 as mt5
#
# # Initialize the MetaTrader5 connection
# if not mt5.initialize():
#     print("MetaTrader5 initialization failed")
#     mt5.shutdown()
# else:
#     print("MetaTrader5 initialized successfully")
#
# # Define order type using correct constant
# order_type = mt5.ORDER_TYPE_BUY  # Correct way to reference buy order type
#
# # Now, place an order (buy order)
# symbol = "EURUSD"
# lot_size = 1.0
# price = mt5.symbol_info_tick(symbol).ask  # Getting current ask price
# slippage = 10
# stop_loss = price - 0.0010
# take_profit = price + 0.0010
#
# # Prepare the order request
# request = {
#     "action": mt5.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": lot_size,
#     "type": order_type,
#     "price": price,
#     "slippage": slippage,
#     "stoploss": stop_loss,
#     "takeprofit": take_profit,
#     "deviation": 20,
#     "magic": 234000,
#     "comment": "Test Buy Order",
#     "type_filling": mt5.ORDER_FILLING_IOC,
#     "type_time": mt5.ORDER_TIME_GTC
# }
#
# # Place a buy order
# order_result = mt5.order_send(request)
#
# # Check if the order was placed successfully
# if order_result is not None:
#     if order_result.retcode == mt5.TRADE_RETCODE_DONE:
#         print(f"Order placed successfully: {order_result}")
#     else:
#         print(f"Failed to place order. Error code: {order_result.retcode}")
#         print(f"Error details: {mt5.last_error()}")
# else:
#     print("Order send failed. Error: ", mt5.last_error())
#
# # Shutdown MT5 connection
# mt5.shutdown()

import MetaTrader5 as mt5
import time

def place_order(symbol, volume, order_type, price, sl, tp, deviation=20, magic_number=234000, comment="Test Order"):
    """
    Places an order and sets stop loss and take profit.
    :param symbol: Currency pair symbol (e.g., "EURUSD")
    :param volume: Volume of the trade
    :param order_type: Either 'buy' or 'sell'
    :param price: Order price
    :param sl: Stop Loss price
    :param tp: Take Profit price
    :param deviation: Slippage allowance in pips
    :param magic_number: Unique identifier for the order
    :param comment: Custom comment for the order
    :return: Order result
    """

    # Define action type based on order type
    action_type = mt5.ORDER_BUY if order_type == "buy" else mt5.ORDER_SELL

    # Prepare the order request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": action_type,
        "price": price,
        "sl": sl,  # Stop loss price
        "tp": tp,  # Take profit price
        "deviation": deviation,
        "magic": magic_number,
        "comment": comment,
        "type_filling": mt5.ORDER_FILLING_IOC,  # Immediate or cancel
        "type_time": mt5.ORDER_TIME_GTC  # Good until canceled
    }

    # Send the order
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed with error code: {result.retcode}")
    else:
        print(f"Order placed successfully: {result}")
    return result


# Example: Place a buy order for EURUSD with SL and TP
symbol = "EURUSD"
volume = 1.0
order_type = "buy"
price = 1.03814
sl = 1.03700  # Stop loss (example value)
tp = 1.04000  # Take profit (example value)

# Place the order
place_order(symbol, volume, order_type, price, sl, tp)
