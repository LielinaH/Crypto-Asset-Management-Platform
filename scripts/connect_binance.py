import os
from binance.client import Client
from dotenv import load_dotenv

# Load API keys
load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
secret_key = os.getenv('BINANCE_SECRET_KEY')

# Connect to Binance Futures Testnet
client = Client(api_key, secret_key, testnet=True)

# Fetch symbols
exchange_info = client.futures_exchange_info()
symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]
print(f"Available Symbols: {symbols}")

# 30 symbols
symbols = symbols[:30]
print(f"Available Symbols: {symbols}")

