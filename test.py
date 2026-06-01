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
    "GOLD": "GC=F",
    "OIL": "BZ=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "TESLA": "TSLA",
    "APPLE": "AAPL"
}
current_prices = {}
for name, symbol in assets.items():
    try:
        data = yf.Ticker(symbol).history(period="1d")
        price = data["Close"].iloc[-1] if not data.empty else 0
        current_prices[name] = float(price)
    except:
        current_prices[name] = 0
# load old
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r") as f:
            old_prices = json.load(f)
    except:
        old_prices = {}
else:
    old_prices = {}
changes = {}
for asset, price in current_prices.items():
    old = old_prices.get(asset, 0)
    if old and old != 0:
        changes[asset] = round(((price - old) / old) * 100, 2)
    else:
        changes[asset] = 0
# save
os.makedirs("data", exist_ok=True)
with open(DATA_FILE, "w") as f:
    json.dump(current_prices, f)
# 🧠 تحلیل حرفه‌ای
best = max(changes, key=changes.get)
worst = min(changes, key=changes.get)
alerts = []
for k, v in changes.items():
    if v >= 2:
        alerts.append(f"🚀 {k} +{v}% Strong Rise")
    elif v <= -2:
        alerts.append(f"⚠️ {k} {v}% Sharp Drop")
# پیام
message = "👁 Third Eye Business\n\n📊 Smart Market Dashboard\n\n"
for asset in assets:
    message += f"{asset}: {current_prices[asset]:.2f} ({changes[asset]:+.2f}%)\n"
message += "\n🏆 Top Gainer: " + best
message += "\n📉 Top Loser: " + worst
if alerts:
    message += "\n\n🔔 Alerts:\n" + "\n".join(alerts)
# send
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("DONE")