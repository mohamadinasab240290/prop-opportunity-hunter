import yfinance as yf
import requests
import os
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
btc_price = yf.Ticker("BTC-USD").history(period="1d").tail(1)["Close"].iloc[0]
eth_price = yf.Ticker("ETH-USD").history(period="1d").tail(1)["Close"].iloc[0]
eurusd_price = yf.Ticker("EURUSD=X").history(period="1d").tail(1)["Close"].iloc[0]
gold_price = yf.Ticker("GC=F").history(period="1d").tail(1)["Close"].iloc[0]
message = f"""
👁 Third Eye Business
📊 Market Dashboard
₿ BTCUSD
{btc_price:.2f}
⟠ ETHUSD
{eth_price:.2f}
🥇 Gold
{gold_price:.2f}
💶 EURUSD
{eurusd_price:.5f}
"""
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
print(response.text)
print("Telegram message sent")