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
# ------------------------
# دریافت قیمت‌ها
# ------------------------
current_prices = {}
for name, symbol in assets.items():
    try:
        data = yf.Ticker(symbol).history(period="1d")
        price = data["Close"].iloc[-1] if not data.empty else 0
        current_prices[name] = float(price)
    except:
        current_prices[name] = 0
# ------------------------
# خواندن قیمت قبلی
# ------------------------
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r") as f:
            old_prices = json.load(f)
    except:
        old_prices = {}
else:
    old_prices = {}
# ------------------------
# محاسبه تغییرات
# ------------------------
changes = {}
for asset, price in current_prices.items():
    old_price = old_prices.get(asset, 0)
    if old_price and old_price != 0:
        changes[asset] = round(((price - old_price) / old_price) * 100, 2)
    else:
        changes[asset] = 0
# ------------------------
# ذخیره داده جدید
# ------------------------
os.makedirs("data", exist_ok=True)

with open(DATA_FILE, "w") as f:
    json.dump(current_prices, f)
# ------------------------
# تحلیل‌ها
# ------------------------
best = max(changes, key=changes.get)
worst = min(changes, key=changes.get)
volatility = max(current_prices, key=lambda x: abs(changes[x]))
# ------------------------
# پیام تلگرام
# ------------------------
message = "👁 Third Eye Business\n\n📊 Professional Market Dashboard\n\n"
for asset in assets:
    price = current_prices[asset]
    change = changes[asset]
    message += f"{asset}: {price:.2f} ({change:+.2f}%)\n"
message += "\n🏆 Top Gainer: " + best + f" ({changes[best]:+.2f}%)"
message += "\n📉 Top Loser: " + worst + f" ({changes[worst]:+.2f}%)"
message += "\n📊 Most Volatile: " + volatility + f" ({changes[volatility]:+.2f}%)"
# ------------------------
# ارسال به تلگرام
# ------------------------
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
print("DONE")