import requests

btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(btc_url)

print("RESULT:")
print(response.text)