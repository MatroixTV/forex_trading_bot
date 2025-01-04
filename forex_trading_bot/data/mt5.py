import MetaTrader5 as mt5

account = ACC_NUM  # Your account number (integer)
password = "PASSWORD"  # Your password (string)
server = "SERVER"  # Your broker's server (string)

# Log in to the account
if not mt5.initialize():
    print("Initialization failed, error code:", mt5.last_error())
    quit()

# Log in to MetaTrader 5 account
authorized = mt5.login(account, password=password, server=server)

if authorized:
    print("Logged in successfully!")
else:
    print("Login failed, error code:", mt5.last_error())
    quit()
