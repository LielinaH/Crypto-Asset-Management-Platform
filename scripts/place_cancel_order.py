import os
from binance.client import Client
from dotenv import load_dotenv

# Load API keys
load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
secret_key = os.getenv('BINANCE_SECRET_KEY')

# Connect to Binance Futures Testnet
client = Client(api_key, secret_key, testnet=True)

def place_cancel_order(symbol, side, quantity, price):
    
    try:
        # Place a LIMIT order
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'  # Good Till Cancelled
        )
        print(f"Order placed: {order}")
        
        # Cancel the order
        order_id = order['orderId']
        result = client.futures_cancel_order(symbol=symbol, orderId=order_id)
        print(f"Order cancelled: {result}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
symbol = "BTCUSDT"
side = "BUY"  # 'BUY' or 'SELL'
quantity = 0.01  # quantity
price = "30000"  # price above current market price so it pass

place_cancel_order(symbol, side, quantity, price)
