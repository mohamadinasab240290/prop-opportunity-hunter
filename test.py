import yfinance as yf
import requests
import os
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
btc = yf.Ticker("BTC-USD")
btc_price = btc.history(period="1d").tail(1)["Close"].iloc[0]
message = f"""
👁 Third Eye Business
📊 Market Dashboard
₿ BTCUSD
{btc_price:.2f}
✅ Data received successfully
"""
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
print("Telegram message sent")