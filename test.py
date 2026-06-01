import yfinance as yf
import requests
import os
import json
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DATA_FILE = "data/prices.json"
# ---------------- GLOBAL MARKETS ----------------
global_assets = {
    "BTCUSD": "BTC-USD",
    "ETHUSD": "ETH-USD",
    "GOLD": "GC=F",
    "OIL": "BZ=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "TESLA": "TSLA",
    "APPLE": "AAPL"
}
# ---------------- IRAN MARKET (simplified proxy data) ----------------
iran_assets = {
    "IRAN_INDEX": "138021",   # placeholder index code
    "IRAN_WEIGHTED": "138001"
}
# چون API رسمی نداریم، اینجا شبیه‌سازی می‌کنیم
# (بعداً می‌تونیم واقعی از TSETMC بگیریم)
iran_data = {
    "IRAN_INDEX": 2150000,
    "IRAN_WEIGHTED": 680000
}
iran_changes = {
    "IRAN_INDEX": 1.2,
    "IRAN_WEIGHTED": -0.4
}
# ---------------- FETCH GLOBAL ----------------
current_prices = {}
for name, symbol in global_assets.items():
    try:
        data = yf.Ticker(symbol).history(period="1d")
        price = data["Close"].iloc[-1] if not data.empty else 0
        current_prices[name] = float(price)
    except:
        current_prices[name] = 0
# ---------------- LOAD OLD ----------------
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
# ---------------- GLOBAL ANALYSIS ----------------
best = max(changes, key=changes.get)
worst = min(changes, key=changes.get)
# ---------------- IRAN ANALYSIS ----------------
iran_best = max(iran_changes, key=iran_changes.get)
# ---------------- AI SENTIMENT ----------------
positive = sum(1 for x in changes.values() if x > 0)
negative = sum(1 for x in changes.values() if x < 0)
if positive > negative:
    sentiment = "🟢 Global Market Bullish"
elif negative > positive:
    sentiment = "🔴 Global Market Bearish"
else:
    sentiment = "🟡 Global Market Neutral"
# ---------------- MESSAGE ----------------
message = "👁 Third Eye Business\n\n"
message += "🌍 GLOBAL MARKETS\n"
for a in global_assets:
    message += f"{a}: {current_prices[a]:.2f} ({changes[a]:+.2f}%)\n"
message += "\n🏆 Global Top: " + best
message += "\n📉 Global Worst: " + worst
message += "\n\n🇮🇷 IRAN MARKET\n"
message += f"IRAN INDEX: {iran_data['IRAN_INDEX']} ({iran_changes['IRAN_INDEX']:+.2f}%)\n"
message += f"WEIGHTED INDEX: {iran_data['IRAN_WEIGHTED']} ({iran_changes['IRAN_WEIGHTED']:+.2f}%)\n"
message += f"Best Sector Move: {iran_best}\n"
message += "\n🧠 AI:\n" + sentiment
# ---------------- SEND ----------------
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("DONE")