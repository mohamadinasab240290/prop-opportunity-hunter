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
# ---------------- AI LOGIC ----------------
positive = sum(1 for x in changes.values() if x > 0)
negative = sum(1 for x in changes.values() if x < 0)
flat = len(changes) - positive - negative
# Trend Strength
if positive >= 6:
    trend = "🟢 Strong Bullish Market"
elif positive >= 4:
    trend = "🟡 Mild Bullish Market"
elif negative >= 6:
    trend = "🔴 Strong Bearish Market"
elif negative >= 4:
    trend = "🟠 Mild Bearish Market"
else:
    trend = "⚪ Neutral Market"
# Risk Level
volatility = sum(abs(x) for x in changes.values()) / len(changes)
if volatility > 2:
    risk = "🔴 High Risk"
elif volatility > 1:
    risk = "🟡 Medium Risk"
else:
    risk = "🟢 Low Risk"
# AI Summary
if positive > negative:
    summary = "Markets are showing overall upward momentum with selective strength in risk assets."
elif negative > positive:
    summary = "Market sentiment is weak with pressure across multiple asset classes."
else:
    summary = "Markets are balanced with no clear directional bias."
# ---------------- BEST / WORST ----------------
best = max(changes, key=changes.get)
worst = min(changes, key=changes.get)
# ---------------- MESSAGE ----------------
message = "👁 Third Eye Business\n\n"
message += "🧠 AI Market Intelligence Report\n\n"
message += f"{trend}\n"
message += f"⚠️ Risk Level: {risk}\n\n"
message += "📊 Assets:\n"
for a in assets:
    message += f"{a}: {current_prices[a]:.2f} ({changes[a]:+.2f}%)\n"
message += f"\n🏆 Top Gainer: {best}"
message += f"\n📉 Top Loser: {worst}\n"
message += "\n🧠 AI Summary:\n" + summary
# ---------------- SEND ----------------
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("DONE")