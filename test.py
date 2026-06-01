import requests
import os
import yfinance as yf
import random
message = "👁 Third Eye Business\n\n"
message += "🔔 Pro Market Alerts\n\n"
# LIVE MARKETS
btc = yf.Ticker("BTC-USD")
btc_price = btc.history(period="1d").tail(1)["Close"].iloc[0]
eth = yf.Ticker("ETH-USD")
eth_price = eth.history(period="1d").tail(1)["Close"].iloc[0]
message += "📊 LIVE MARKETS\n\n"
message += f"₿ BTCUSD: ${btc_price:,.2f}\n"
message += f"⟠ ETHUSD: ${eth_price:,.2f}\n\n"
# PROP OPPORTUNITIES
prop_opps = [
    "🏆 Demo Trading Contest - Free Entry Prop Competitions",
    "🏆 Monthly Trading Challenges with funded prizes",
    "💼 FTMO / FundedNext discount campaigns",
    "🎁 No Deposit Bonus offers",
    "💰 Evaluation fee discounts",
    "🚀 Free funded account giveaways"
]
message += "💼 PROP OPPORTUNITIES\n"
for opp in prop_opps:
    message += f"{opp}\n"
# EXCHANGES
message += "\n\n🏦 EXCHANGES OVERVIEW\n"
exchanges = [
    "Binance",
    "Bybit",
    "OKX",
    "KuCoin",
    "Bitget",
    "MEXC",
    "BingX"
]
for ex in exchanges:
    message += f"• {ex} 🟢 Active\n"
# BROKERS
message += "\n\n🏛 BROKERS WATCHLIST\n"
brokers = [
    "Exness",
    "XM",
    "FBS",
    "RoboForex",
    "HFM"
]
for broker in brokers:
    message += f"• {broker}\n"
# IRANIAN PROP WATCHLIST
message += "\n\n📢 IRANIAN PROP WATCHLIST\n"
iran_prop_channels = [
    "PropCheck",
    "PropKadeh",
    "PropLogy",
    "ProopCo",
    "PropChi"
]
for channel in iran_prop_channels:
    message += f"• {channel}\n"
# TODAY FREE OPPORTUNITY
today_opportunities = [
    "🎁 Prop Discount Campaign Watch",
    "🏆 Demo Competition Watch",
    "🚀 Funded Giveaway Watch",
    "💰 Evaluation Discount Alert",
    "🎯 Free Challenge Opportunity",
    "🏦 Exchange Reward Campaign",
    "🎁 Broker Bonus Event Watch",
    "🔥 Limited-Time Prop Promotion",
    "💵 Cashback Campaign Alert",
    "🎉 New User Reward Program"
]
message += "\n\n🔥 TODAY FREE OPPORTUNITY\n"
message += random.choice(today_opportunities)
# TELEGRAM SEND
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
print("Status Code:", response.status_code)
print("Response:", response.text)