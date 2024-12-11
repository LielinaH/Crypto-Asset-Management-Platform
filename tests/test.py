from binance.client import Client
import os
from dotenv import load_dotenv

# Load API/Secret keys
load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
secret_key = os.getenv('BINANCE_SECRET_KEY')

# Connect to Binance(Testnet)
client = Client(api_key, secret_key, testnet=True)

# Test if the API keys are working by fetching server time
try:
    server_time = client.get_server_time()
    print("Server time:", server_time)
except Exception as e:
    print(f"Error: {e}")
