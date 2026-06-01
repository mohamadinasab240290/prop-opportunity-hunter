import requests
import os
import yfinance as yf

message = "👁 Third Eye Business\n\n"
message += "🔔 Pro Market Alerts\n\n"
message += "✅ yfinance loaded successfully\n\n"

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

message += "\n\n🏦 EXCHANGES OVERVIEW\n"
message += "• Binance 🟢 Active\n"
message += "• Bybit 🟢 Active\n"
message += "• OKX 🟢 Active\n"
message += "• KuCoin 🟢 Active\n"

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