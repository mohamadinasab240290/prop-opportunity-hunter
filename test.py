import requests
import json
import os
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DATA_FILE = "data/prices.json"
# ---------------- IRAN DATA ----------------
def get_iran():
    try:
        url = "https://brsapi.ir/Api/Indices.php?type=1"
        data = requests.get(url, timeout=10).json()
        return {
            "index": float(data["index"]),
            "change": float(data["index_change_percent"])
        }
    except:
        return {"index": 0, "change": 0}
iran = get_iran()
# ---------------- GLOBAL DATA ----------------
symbols = {
    "BTC": "BTC-USD",
    "GOLD": "GC=F",
    "OIL": "BZ=F"
}
global_changes = {}
for k, v in symbols.items():
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{v}")
        price = r.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
        # fake change calc (simple momentum proxy)
        prev = 100
        change = ((price - prev) / prev) * 100
        global_changes[k] = round(change, 2)
    except:
        global_changes[k] = 0
# ---------------- ALERTS ----------------
alerts = []
# IRAN ALERT
if iran["change"] >= 1.5:
    alerts.append(f"🇮🇷 🚀 Iran Market Strong Bullish ({iran['change']}%)")
elif iran["change"] <= -1.5:
    alerts.append(f"🇮🇷 ⚠️ Iran Market Strong Bearish ({iran['change']}%)")
# GLOBAL ALERT
for k, v in global_changes.items():
    if v >= 2:
        alerts.append(f"🌍 🚀 {k} Strong Rise (+{v}%)")
    elif v <= -2:
        alerts.append(f"🌍 ⚠️ {k} Strong Drop ({v}%)")
# MARKET SYNC
if iran["change"] > 1 and any(v > 1 for v in global_changes.values()):
    alerts.append("🚨 Global + Iran Market Moving Together (Risk-On Mode)")
elif iran["change"] < -1 and any(v < -1 for v in global_changes.values()):
    alerts.append("🚨 Global + Iran Market Falling Together (Risk-Off Mode)")
# ---------------- MESSAGE ----------------
message = "👁 Third Eye Business\n\n"
message += "🔔 Pro Market Alerts\n\n"
if alerts:
    message += "\n".join(alerts)
else:
    message += "🟡 No strong signals detected"
message += f"\n\n🇮🇷 Iran Change: {iran['change']}%"
# ---------------- SEND ----------------
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("DONE")