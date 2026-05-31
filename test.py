import os
import requests
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
message = """
🚀 Prop Opportunity Hunter
✅ سیستم آنلاین است
✅ GitHub Actions فعال است
✅ ربات تلگرام متصل است
تاریخ گزارش: 2026-06-01
"""
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
print("Message sent")