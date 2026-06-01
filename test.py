import os
import requests
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
message = """
🔥 Third Eye Prop Scanner
Scanning Prop Opportunities...
FTMO
FundedNext
Funding Pips
The Funded Trader
Bot Online ✅
"""
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})