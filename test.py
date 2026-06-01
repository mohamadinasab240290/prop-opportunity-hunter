import requests
import os
import random
import yfinance as yf
# ================= SAFE FUNCTIONS =================
def get_yf(symbol):
    try:
        return yf.Ticker(symbol).history(period="2d")["Close"].iloc[-1]
    except:
        return None
def get_binance(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        return float(requests.get(url, timeout=5).json()["price"])
    except:
        return None
# ================= USERS SUPPORT =================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# اگر چند کاربر داری اینجا اضافه کن (یا از DB بعداً می‌سازیم)
USERS = os.getenv("TELEGRAM_CHAT_ID", "").split(",")
# ================= MARKET DATA =================
btc = get_binance("BTCUSDT")
eth = get_binance("ETHUSDT")
gold = get_yf("GC=F")
oil = get_yf("CL=F")
usd_irr = 820000
# ================= SCORE =================
def score(x):
    return random.randint(45, 90)
scores = {
    "BTC": score(btc),
    "ETH": score(eth),
    "GOLD": score(gold),
    "OIL": score(oil)
}
best = max(scores, key=scores.get)
worst = min(scores, key=scores.get)
avg = sum(scores.values()) / len(scores)
if avg > 75:
    state = "🚀 STRONG MARKET"
elif avg > 55:
    state = "📊 NORMAL MARKET"
else:
    state = "⚠️ WEAK MARKET"
signal = "🚀 BUY ZONE" if avg > 75 else "⛔ WAIT"
# ================= BUILD MESSAGE =================
def build_message():
    msg = "👁 Third Eye AI V5\n\n"
    msg += "🧠 MULTI USER MARKET ENGINE\n\n"
    msg += "📊 SCORES\n\n"
    msg += f"₿ BTC: {scores['BTC']}\n"
    msg += f"⟠ ETH: {scores['ETH']}\n"
    msg += f"🥇 GOLD: {scores['GOLD']}\n"
    msg += f"🛢 OIL: {scores['OIL']}\n"
    msg += "\n🧠 ANALYSIS\n\n"
    msg += f"🔥 State: {state}\n"
    msg += f"🏆 Best: {best}\n"
    msg += f"📉 Worst: {worst}\n"
    msg += f"📊 Avg: {avg:.1f}\n"
    msg += "\n🎯 SIGNAL\n\n"
    msg += signal
    return msg
# ================= SEND TO ALL USERS =================
message = build_message()
for chat_id in USERS:
    if chat_id.strip():
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": chat_id.strip(),
                "text": message
            }
        )
print("MULTI USER SENT")