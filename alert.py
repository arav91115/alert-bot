import requests

# Get BTC price from Binance
data = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
price = float(data["price"])

print("Current price:", price)

# Condition
if price > 50000:
    print("ALERT: Price crossed 50000")
