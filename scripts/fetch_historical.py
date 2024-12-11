import os
from binance.client import Client
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import time

# Load API keys
load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
secret_key = os.getenv('BINANCE_SECRET_KEY')

# Connect to Binance Futures Testnet
client = Client(api_key, secret_key, testnet=True)

# Load selected symbols
with open("../data/selected_symbols.txt", "r") as f:
    symbols = f.read().splitlines()

# Create the 'data' directory if it doesn't exist
os.makedirs("../data", exist_ok=True)

def fetch_historical_data(symbol, interval, start_time):
    """Fetch historical klines for a given symbol and interval."""
    try:
        klines = client.futures_klines(symbol=symbol, interval=interval, startTime=start_time)
        columns = ['open_time', 'open', 'high', 'low', 'close', 'volume',
                   'close_time', 'quote_asset_volume', 'number_of_trades',
                   'taker_buy_base', 'taker_buy_quote', 'ignore']
        df = pd.DataFrame(klines, columns=columns)
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()

# Download data for each symbol
start_time = int((datetime.now() - timedelta(days=3*365)).timestamp() * 1000)  # Approx 3 years
for symbol in symbols:
    print(f"Fetching data for {symbol}...")
    data = fetch_historical_data(symbol, interval='1d', start_time=start_time)
    if not data.empty:
        data.to_csv(f"../data/{symbol}_historical.csv", index=False)
    time.sleep(1)  # To avoid rate limit
