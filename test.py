import yfinance as yf
import requests
import os
import json

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

DATA_FILE = "data/prices.json"

assets = {
    "BTCUSD": "BTC-USD",
    "ETHUSD": "ETH-USD",
    "EURUSD": "EURUSD=X",
    "GOLD": "GC=F"
}

# دریافت قیمت‌های فعلی
current_prices = {}

for name, symbol in assets.items():
    try:
        price = yf.Ticker(symbol).history(period="1d").tail(1)["Close"].iloc[0]
        current_prices[name] = float(price)
    except:
        current_prices[name] = 0

# خواندن قیمت‌های قبلی
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        old_prices = json.load(f)
else:
    old_prices = {}

changes = {}

for asset, current_price in current_prices.items():
    old_price = old_prices.get(asset, None)

    if old_price and old_price != 0:
        change = ((current_price - old_price) / old_price) * 100
        changes[asset] = round(change, 2)
    else:
        changes[asset] = 0

# ذخیره قیمت‌های جدید
with open(DATA_FILE, "w") as f:
    json.dump(current_prices, f)

best_asset = max(changes, key=changes.get)
worst_asset = min(changes, key=changes.get)

message = "👁 Third Eye Business\n\n"
message += "📊 Market Dashboard\n\n"

for asset in current_prices:
    message += f"{asset}: {current_prices[asset]:.2f} ({changes[asset]:+.2f}%)\n"

message += "\n"
message += f"🏆 Best Performer: {best_asset} ({changes[best_asset]:+.2f}%)\n"
message += f"📉 Worst Performer: {worst_asset} ({changes[worst_asset]:+.2f}%)"

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Telegram message sent")