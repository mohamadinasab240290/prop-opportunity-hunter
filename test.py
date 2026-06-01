_engine"}
import requests
import os
import random
# ================= SAFE GET =================
def safe_get(url):
    try:
        return requests.get(url, timeout=5).json()
    except:
        return None
# ================= CRYPTO (BINANCE REAL-TIME) =================
def get_crypto(symbol):
    data = safe_get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    return float(data["price"]) if data else None
btc_price = get_crypto("BTCUSDT")
eth_price = get_crypto("ETHUSDT")
# ================= FOREX (REAL-TIME API) =================
fx = safe_get("https://api.exchangerate.host/latest?base=USD")
eurusd = fx["rates"]["EUR"] if fx else None
gbpusd = fx["rates"]["GBP"] if fx else None
usdjpy = fx["rates"]["JPY"] if fx else None
# ================= STOCKS / GOLD (YFINANCE FALLBACK) =================
import yfinance as yf
def get_yf(t):
    try:
        return yf.Ticker(t).history(period="1d")["Close"].iloc[-1]
    except:
        return None
gold_price = get_yf("GC=F")
apple_price = get_yf("AAPL")
tesla_price = get_yf("TSLA")
oil_price = get_yf("CL=F")
# ================= IRAN FX =================
usd_irr = 820000
# ================= MESSAGE =================
message = "👁 Third Eye Business\n\n"
message += "🔔 REAL-TIME MARKET ENGINE\n\n"
message += "📊 CRYPTO\n\n"
if btc_price:
    message += f"₿ BTC: ${btc_price:,.2f}\n"
if eth_price:
    message += f"⟠ ETH: ${eth_price:,.2f}\n"
message += "\n💱 FOREX\n\n"
if eurusd:
    message += f"💶 EUR/USD: {eurusd:.4f}\n"
if gbpusd:
    message += f"💷 GBP/USD: {gbpusd:.4f}\n"
if usdjpy:
    message += f"💴 USD/JPY: {usdjpy:.2f}\n"
message += "\n📈 STOCKS & COMMODITIES\n\n"
if gold_price:
    message += f"🥇 GOLD: ${gold_price:,.2f}\n"
if apple_price:
    message += f"🍎 APPLE: ${apple_price:,.2f}\n"
if tesla_price:
    message += f"🚗 TESLA: ${tesla_price:,.2f}\n"
if oil_price:
    message += f"🛢 OIL: ${oil_price:,.2f}\n"
# ================= IRAN MARKET =================
message += "\n🇮🇷 IRAN MARKET\n\n"
if gold_price:
    message += f"🥇 Gold Iran: {int(gold_price * usd_irr):,} IRR\n"
message += f"💵 USD/IRR: {usd_irr:,}\n"
# ================= REGIONAL FX =================
message += "\n🌍 REGIONAL FX\n\n"
regional = {
    "🇦🇪 AED": 113000,
    "🇨🇳 CNY": 115000,
    "🇹🇷 TRY": 29000,
    "🇴🇲 OMR": 3800000
}
for k, v in regional.items():
    message += f"{k}: {v:,} IRR\n"
# ================= PROP =================
message += "\n💼 PROP OPPORTUNITIES\n"
props = ["Demo Contest", "Funded Challenge", "No Deposit Bonus", "Fee Discount", "Free Account Giveaway"]
for p in props:
    message += f"• {p}\n"
# ================= EXCHANGES =================
message += "\n🏦 EXCHANGES\n"
for e in ["Binance","Bybit","OKX","KuCoin","Bitget","MEXC","BingX"]:
    message += f"• {e}\n"
# ================= BROKERS =================
message += "\n🏛 BROKERS\n"
for b in ["Exness","XM","FBS","RoboForex","HFM"]:
    message += f"• {b}\n"
# ================= IRAN PROP =================
message += "\n📢 IRAN PROP WATCHLIST\n"
for c in ["PropCheck","PropKadeh","PropLogy","ProopCo","PropChi"]:
    message += f"• {c}\n"
# ================= OPPORTUNITY =================
opps = [
    "🏆 Demo Competition",
    "🚀 Funded Giveaway",
    "💰 Discount Campaign",
    "🎁 Broker Bonus Event",
    "🔥 Limited Prop Deal"
]
message += "\n🔥 TODAY OPPORTUNITY\n"
message += random.choice(opps)
# ================= SEND =================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)