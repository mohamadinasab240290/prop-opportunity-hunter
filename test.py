import requests
import os
import random
import yfinance as yf
# ================= SAFE START =================
message = "👁 Third Eye Business\n\n"
message += "🔔 REAL-TIME MARKET ENGINE\n\n"
# ================= SAFE FUNCTION =================
def get_yf_price(symbol):
    try:
        return yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]
    except:
        return None
def get_binance(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        return float(requests.get(url, timeout=5).json()["price"])
    except:
        return None
# ================= CRYPTO (REAL-TIME) =================
btc = get_binance("BTCUSDT")
eth = get_binance("ETHUSDT")
message += "📊 CRYPTO\n\n"
if btc:
    message += f"₿ BTC: ${btc:,.2f}\n"
if eth:
    message += f"⟠ ETH: ${eth:,.2f}\n"
# ================= FOREX =================
eurusd = get_yf_price("EURUSD=X")
gbpusd = get_yf_price("GBPUSD=X")
usdjpy = get_yf_price("JPY=X")
message += "\n💱 FOREX\n\n"
if eurusd:
    message += f"💶 EUR/USD: {eurusd:.4f}\n"
if gbpusd:
    message += f"💷 GBP/USD: {gbpusd:.4f}\n"
if usdjpy:
    message += f"💴 USD/JPY: {usdjpy:.2f}\n"
# ================= STOCKS & COMMODITIES =================
gold = get_yf_price("GC=F")
apple = get_yf_price("AAPL")
tesla = get_yf_price("TSLA")
oil = get_yf_price("CL=F")
message += "\n📈 STOCKS & COMMODITIES\n\n"
if gold:
    message += f"🥇 GOLD: ${gold:,.2f}\n"
if apple:
    message += f"🍎 APPLE: ${apple:,.2f}\n"
if tesla:
    message += f"🚗 TESLA: ${tesla:,.2f}\n"
if oil:
    message += f"🛢 OIL: ${oil:,.2f}\n"
# ================= IRAN MARKET =================
usd_irr = 820000
message += "\n🇮🇷 IRAN MARKET\n\n"
if gold:
    message += f"🥇 GOLD IRAN: {int(gold * usd_irr):,} IRR\n"
message += f"💵 USD/IRR: {usd_irr:,}\n"
# ================= REGIONAL FX =================
regional = {
    "🇦🇪 AED": 113000,
    "🇨🇳 CNY": 115000,
    "🇹🇷 TRY": 29000,
    "🇴🇲 OMR": 3800000
}
message += "\n🌍 REGIONAL FX\n\n"
for k, v in regional.items():
    message += f"{k}: {v:,} IRR\n"
# ================= PROP OPPORTUNITIES =================
props = [
    "🏆 Demo Contest",
    "💼 Funded Challenge",
    "🎁 No Deposit Bonus",
    "💰 Fee Discount",
    "🚀 Free Funded Account"
]
message += "\n💼 PROP OPPORTUNITIES\n\n"
for p in props:
    message += f"• {p}\n"
# ================= EXCHANGES =================
exchanges = ["Binance", "Bybit", "OKX", "KuCoin", "Bitget", "MEXC", "BingX"]
message += "\n🏦 EXCHANGES\n\n"
for e in exchanges:
    message += f"• {e}\n"
# ================= BROKERS =================
brokers = ["Exness", "XM", "FBS", "RoboForex", "HFM"]
message += "\n🏛 BROKERS\n\n"
for b in brokers:
    message += f"• {b}\n"
# ================= IRAN PROP WATCHLIST =================
iran_props = ["PropCheck", "PropKadeh", "PropLogy", "ProopCo", "PropChi"]
message += "\n📢 IRAN PROP WATCHLIST\n\n"
for i in iran_props:
    message += f"• {i}\n"
# ================= TODAY OPPORTUNITY =================
today = [
    "🎁 Prop Discount Campaign",
    "🏆 Demo Competition",
    "🚀 Funded Giveaway",
    "💰 Evaluation Discount",
    "🔥 Limited Time Event"
]
message += "\n🔥 TODAY OPPORTUNITY\n\n"
message += random.choice(today)
# ================= SEND =================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
print(response.status_code)
print(response.text)