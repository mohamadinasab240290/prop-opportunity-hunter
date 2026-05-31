import os
import requests
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
print("TOKEN OK:", bool(TOKEN))
print("CHAT OK:", bool(CHAT_ID))
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": "🚀 تست موفق! ربات چشم سوم فعال شد"
}
res = requests.post(url, data=data)
print("Response:", res.text)
