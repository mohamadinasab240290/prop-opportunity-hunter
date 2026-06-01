import requests
import os
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
# BTCUSDT
btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
btc_price = requests.get(btc_url).json()["price"]
# Message
message = f"""
👁 Third Eye Business
📊 Market Dashboard
₿ BTCUSDT
{btc_price}
🚀 Bot is running successfully
"""
# Send Telegram
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Message sent")