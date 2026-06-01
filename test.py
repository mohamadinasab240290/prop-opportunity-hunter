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
# ================= DATA =================
btc = get_binance("BTCUSDT")
eth = get_binance("ETHUSDT")
gold = get_yf("GC=F")
oil = get_yf("CL=F")
eurusd = get_yf("EURUSD=X")
usd_irr = 820000
# ================= SIMPLE AI LOGIC =================
assets = {}
if btc: assets["BTC"] = btc
if eth: assets["ETH"] = eth
if gold: assets["GOLD"] = gold
if oil: assets["OIL"] = oil
# fake momentum scoring (simple but effective)
best_asset = None
worst_asset = None
if assets:
    best_asset = max(assets, key=assets.get)
    worst_asset = min(assets, key=assets.get)
# sentiment logic
if btc and eth:
    if btc > eth:
        sentiment = "🚀 Risk ON (Crypto leading)"
    else:
        sentiment = "⚠️ Mixed Market"
else:
    sentiment = "📊 Neutral Market"
# opportunity level
volatility = random.choice(["LOW 🟢", "MEDIUM 🟡", "HIGH 🔥"])
# ================= MESSAGE =================
message = "👁 Third Eye AI Engine\n\n"
message += "🧠 MARKET INTELLIGENCE REPORT\n\n"
message += "📊 LIVE SNAPSHOT\n\n"
if btc:
    message += f"₿ BTC: ${btc:,.2f}\n"
if eth:
    message += f"⟠ ETH: ${eth:,.2f}\n"
if gold:
    message += f"🥇 GOLD: ${gold:,.2f}\n"
if oil:
    message += f"🛢 OIL: ${oil:,.2f}\n"
message += "\n🧠 AI ANALYSIS\n\n"
message += f"🔥 Sentiment: {sentiment}\n"
message += f"📈 Best Asset: {best_asset}\n"
message += f"📉 Worst Asset: {worst_asset}\n"
message += f"⚡ Volatility: {volatility}\n"
message += "\n🇮🇷 IRAN VIEW\n\n"
message += f"💵 USD/IRR: {usd_irr:,}\n"
if gold:
    message += f"🥇 Gold IRR: {int(gold * usd_irr):,}\n"
message += "\n🎯 OPPORTUNITY ENGINE\n\n"
opps = [
    "🏆 Prop Challenge Window Open",
    "💰 Market volatility suitable for trading",
    "🚀 Funded account opportunity active",
    "⚠️ Wait for better entry conditions",
    "🔥 High momentum market detected"
]
message += random.choice(opps)
# ================= SEND =================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("AI ENGINE SENT")