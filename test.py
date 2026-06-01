import requests
import os
# ---------------- MESSAGE START ----------------
message = "👁 Third Eye Business\n\n"
message += "🔔 Pro Market Alerts\n\n"
# ---------------- PROP OPPORTUNITIES ----------------
prop_opps = [
    "🏆 Demo Trading Contest - Free Entry Prop Competitions",
    "🏆 Monthly Trading Challenges with funded prizes",
    "💼 FTMO / FundedNext discount campaigns (seasonal)",
    "🎁 No Deposit Bonus offers (broker dependent)",
    "💰 Evaluation fee discounts in prop firms",
    "🚀 Free funded account giveaways (limited seats)"
]
message += "💼 PROP OPPORTUNITIES\n"
for opp in prop_opps:
    message += f"{opp}\n"
# ---------------- EXCHANGES MODULE ----------------
global_exchanges = [
    "Binance",
    "Bybit",
    "OKX",
    "KuCoin"
]
iran_exchanges = [
    "Nobitex",
    "Wallex",
    "Bitpin"
]
message += "\n\n🏦 EXCHANGES OVERVIEW\n"
message += "🌍 Global Exchanges:\n"
for ex in global_exchanges:
    message += f"• {ex} 🟢 Active\n"
message += "\n🇮🇷 Iranian Exchanges:\n"
for ex in iran_exchanges:
    message += f"• {ex} 🟡 Local Market\n"
# ---------------- MARKET SUMMARY ----------------
message += "\n\n🔔 MARKET SUMMARY\n"
message += "AI analysis will be displayed here.\n"
# ---------------- TELEGRAM SEND ----------------
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