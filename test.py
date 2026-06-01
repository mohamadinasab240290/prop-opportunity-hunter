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
# ---------------- DATA ----------------
current_prices = {}
for name, symbol in assets.items():
    try:
        data = yf.Ticker(symbol).history(period="1d")
        price = data["Close"].iloc[-1] if not data.empty else 0
        current_prices[name] = float(price)
    except:
        current_prices[name] = 0
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r") as f:
            old_prices = json.load(f)
    except:
        old_prices = {}
else:
    old_prices = {}
changes = {}
for k, v in current_prices.items():
    old = old_prices.get(k, 0)
    if old and old != 0:
        changes[k] = round(((v - old) / old) * 100, 2)
    else:
        changes[k] = 0
os.makedirs("data", exist_ok=True)
with open(DATA_FILE, "w") as f:
    json.dump(current_prices, f)
# ---------------- ANALYSIS ----------------
best = max(changes, key=changes.get)
worst = min(changes, key=changes.get)
# AI Insight (simple but powerful)
bullish = sum(1 for x in changes.values() if x > 0)
bearish = sum(1 for x in changes.values() if x < 0)
if bullish > bearish:
    sentiment = "🟢 Market is Bullish"
elif bearish > bullish:
    sentiment = "🔴 Market is Bearish"
else:
    sentiment = "🟡 Market is Neutral"
# ---------------- MESSAGE ----------------
message = "👁 Third Eye Business\n\n"
message += "📊 Global Market Dashboard\n\n"
for a in assets:
    message += f"{a}: {current_prices[a]:.2f} ({changes[a]:+.2f}%)\n"
message += "\n🏆 Top Gainer: " + best
message += "\n📉 Top Loser: " + worst
message += "\n\n🧠 AI Insight:\n" + sentiment
# ---------------- SEND ----------------
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("DONE")