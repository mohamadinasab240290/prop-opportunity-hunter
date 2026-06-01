import requests
import os
import yfinance as yf
import random
# ================= MESSAGE START =================
message = "👁 Third Eye Business\n\n"
message += "🔔 Pro Market Alerts\n\n"
# ================= LIVE MARKETS =================
def get_price(ticker):
    try:
        return yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1]
    except:
        return None
btc_price = get_price("BTC-USD")
eth_price = get_price("ETH-USD")
gold_price = get_price("GC=F")
apple_price = get_price("AAPL")
tesla_price = get_price("TSLA")
oil_price = get_price("CL=F")
message += "📊 LIVE MARKETS\n\n"
if btc_price:
    message += f"₿ BTC: ${btc_price:,.2f}\n"
if eth_price:
    message += f"⟠ ETH: ${eth_price:,.2f}\n"
if gold_price:
    message += f"🥇 GOLD: ${gold_price:,.2f}\n"
if apple_price:
    message += f"🍎 APPLE: ${apple_price:,.2f}\n"
if tesla_price:
    message += f"🚗 TESLA: ${tesla_price:,.2f}\n"
if oil_price:
    message += f"🛢 OIL: ${oil_price:,.2f}\n"
message += "\n"
# ================= FOREX =================
eurusd = get_price("EURUSD=X")
gbpusd = get_price("GBPUSD=X")
usdjpy = get_price("JPY=X")
message += "💱 FOREX\n\n"
if eurusd:
    message += f"💶 EUR/USD: {eurusd:.4f}\n"
if gbpusd:
    message += f"💷 GBP/USD: {gbpusd:.4f}\n"
if usdjpy:
    message += f"💴 USD/JPY: {usdjpy:.2f}\n"
message += "\n"
# ================= IRAN FX =================
usd_irr = 820000
message += "🇮🇷 IRAN FX\n\n"
message += f"💵 USD/IRR: {usd_irr:,}\n"
if gold_price:
    gold_iran = gold_price * usd_irr
    message += f"🥇 GOLD IRAN (est): {int(gold_iran):,} IRR\n"
message += "\n"
# ================= REGIONAL FX =================
message += "🌍 REGIONAL FX\n\n"
regional_fx = {
    "🇦🇪 AED": 113000,
    "🇨🇳 CNY": 115000,
    "🇹🇷 TRY": 29000,
    "🇴🇲 OMR": 3800000
}
for name, value in regional_fx.items():
    message += f"{name}: {value:,} IRR\n"
message += "\n"
# ================= PROP OPPORTUNITIES =================
prop_opps = [
    "🏆 Demo Trading Contest",
    "💼 Funded Challenge Discounts",
    "🎁 No Deposit Bonus",
    "💰 Evaluation Fee Discount",
    "🚀 Free Funded Account Giveaway"
]
message += "💼 PROP OPPORTUNITIES\n\n"
for opp in prop_opps:
    message += f"• {opp}\n"
message += "\n"
# ================= EXCHANGES =================
exchanges = ["Binance", "Bybit", "OKX", "KuCoin", "Bitget", "MEXC", "BingX"]
message += "🏦 EXCHANGES\n\n"
for ex in exchanges:
    message += f"• {ex}\n"
message += "\n"
# ================= BROKERS =================
brokers = ["Exness", "XM", "FBS", "RoboForex", "HFM"]
message += "🏛 BROKERS\n\n"
for b in brokers:
    message += f"• {b}\n"
message += "\n"
# ================= IRAN PROP WATCHLIST =================
iran_props = ["PropCheck", "PropKadeh", "PropLogy", "ProopCo", "PropChi"]
message += "📢 IRAN PROP WATCHLIST\n\n"
for p in iran_props:
    message += f"• {p}\n"
message += "\n"
# ================= TODAY OPPORTUNITY =================
today_opps = [
    "🎁 Prop Discount Campaign",
    "🏆 Demo Competition",
    "🚀 Funded Giveaway",
    "💰 Evaluation Discount",
    "🎯 Free Challenge",
    "🔥 Limited Time Prop Event"
]
message += "🔥 TODAY OPPORTUNITY\n\n"
message += random.choice(today_opps)
# ================= TELEGRAM =================
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