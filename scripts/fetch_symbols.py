import os
from binance.client import Client
from dotenv import load_dotenv
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Load API keys
load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
secret_key = os.getenv('BINANCE_SECRET_KEY')

# Connect to Binance Futures Testnet
client = Client(api_key, secret_key, testnet=True)

# Fetch all available symbols
try:
    exchange_info = client.futures_exchange_info()
    symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]
    logging.info(f"Total symbols available: {len(symbols)}")
    
    # Select 30 symbols based on criteria
    selected_symbols = symbols[:30]  # Modify logic for selection criteria
    logging.info(f"Selected Symbols: {selected_symbols}")
    
    # Save symbols to a file for future reference
    os.makedirs("../data", exist_ok=True)
    with open("../data/selected_symbols.txt", "w") as f:
        f.write("\n".join(selected_symbols))
except Exception as e:
    logging.error(f"Error fetching symbols: {e}")
