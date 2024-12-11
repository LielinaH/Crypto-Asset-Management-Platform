import os
from binance.client import Client
from dotenv import load_dotenv

# Load API keys
load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
secret_key = os.getenv('BINANCE_SECRET_KEY')

# Check API keys
if not api_key or not secret_key:
    raise ValueError("API key and Secret key must be set in the environment variables.")

# Connect to Binance Futures Testnet
client = Client(api_key, secret_key, testnet=True)
print("Successfully connected to Binance Futures Testnet.")