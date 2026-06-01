import requests
import os
import random
import yfinance as yf
# ================= SAFE FUNCTIONS =================
def get_yf(symbol):
    try:
        return yf.Ticker(symbol).history(period="5d")["Close"]
    except:
        return None
def get_binance(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        return float(requests.get(url, timeout=5).json()["price"])
    except:
        return None
# ================= DATA =================
btc = get_binance("BTCUSDT")
eth = get_binance("ETHUSDT")
gold = get_yf("GC=F")
oil = get_yf("CL=F")
usd_irr = 820000
# ================= SCORE ENGINE =================
def score_asset(series):
    try:
        if series is None or len(series) < 2:
            return 50
        change = (series.iloc[-1] - series.iloc[-2]) / series.iloc[-2] * 100
        if change > 2:
            return 85
        elif change > 0:
            return 70
        elif change > -2:
            return 50
        else:
            return 30
    except:
        return 50
# ================= SCORES =================
scores = {}
if btc: scores["BTC"] = 80 if btc > 0 else 50
if eth: scores["ETH"] = 75 if eth > 0 else 50
if gold is not None:
    scores["GOLD"] = score_asset(gold)
if oil is not None:
    scores["OIL"] = score_asset(oil)
# ================= BEST / WORST =================
best = max(scores, key=scores.get) if scores else None
worst = min(scores, key=scores.get) if scores else None
avg_score = sum(scores.values()) / len(scores) if scores else 50
# ================= MARKET STATE =================
if avg_score > 75:
    state = "🚀 STRONG BULL MARKET"
elif avg_score > 55:
    state = "📊 NEUTRAL TO POSITIVE"
else:
    state = "⚠️ WEAK / SIDEWAYS MARKET"
# ================= MESSAGE =================
message = "👁 Third Eye AI Engine V4\n\n"
message += "🧠 ADVANCED MARKET SCORING SYSTEM\n\n"
message += "📊 LIVE SCORES\n\n"
if btc:
    message += f"₿ BTC: ${btc:,.2f} | Score: 80\n"
if eth:
    message += f"⟠ ETH: ${eth:,.2f} | Score: 75\n"
if gold is not None:
    message += f"🥇 GOLD Score: {scores.get('GOLD',50)}\n"
if oil is not None:
    message += f"🛢 OIL Score: {scores.get('OIL',50)}\n"
message += "\n🧠 AI DECISION\n\n"
message += f"🔥 Market State: {state}\n"
message += f"🏆 Best Asset: {best}\n"
message += f"📉 Worst Asset: {worst}\n"
message += f"📊 Avg Score: {avg_score:.1f}/100\n"
# ================= OPPORTUNITY SIGNAL =================
if avg_score > 75:
    signal = "🚀 HIGH PROBABILITY TRADE WINDOW"
elif avg_score > 55:
    signal = "⚖️ WAIT FOR CONFIRMATION"
else:
    signal = "⛔ NO TRADE - RISKY MARKET"
message += "\n🎯 SIGNAL\n\n"
message += signal
# ================= IRAN =================
message += "\n\n🇮🇷 IRAN VIEW\n\n"
message += f"💵 USD/IRR: {usd_irr:,}\n"
# ================= SEND =================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("V4 SENT")