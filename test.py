import requests
import json
import os
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DATA_FILE = "data/prices.json"
# ---------------- GLOBAL (keep yfinance optional later) ----------------
global_assets = {
    "BTCUSD": "BTC-USD",
    "GOLD": "GC=F",
    "OIL": "BZ=F"
}
# ---------------- IRAN REAL DATA ----------------
def get_iran_indices():
    url = "https://brsapi.ir/Api/Indices.php?type=1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        data = res.json()
        return {
            "IRAN_INDEX": float(data["index"]),
            "IRAN_EQUAL_WEIGHT": float(data["index_equalWeight"]),
            "IRAN_CHANGE": float(data["index_change_percent"])
        }
    except:
        return {
            "IRAN_INDEX": 0,
            "IRAN_EQUAL_WEIGHT": 0,
            "IRAN_CHANGE": 0
        }
iran = get_iran_indices()
# ---------------- GLOBAL SIMPLE ----------------
global_prices = {}
for k, v in global_assets.items():
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{v}")
        result = r.json()
        price = result["chart"]["result"][0]["meta"]["regularMarketPrice"]
        global_prices[k] = float(price)
    except:
        global_prices[k] = 0
# ---------------- LOAD OLD ----------------
if os.path.exists(DATA_FILE):
    try:
        old = json.load(open(DATA_FILE))
    except:
        old = {}
else:
    old = {}
# ---------------- SAVE ----------------
os.makedirs("data", exist_ok=True)
new_data = {**global_prices, **iran}
json.dump(new_data, open(DATA_FILE, "w"))
# ---------------- SIMPLE ANALYSIS ----------------
message = "👁 Third Eye Business\n\n"
message += "🇮🇷 IRAN MARKET (REAL)\n"
message += f"📊 Index: {iran['IRAN_INDEX']}\n"
message += f"⚖️ Equal Weight: {iran['IRAN_EQUAL_WEIGHT']}\n"
message += f"📈 Change: {iran['IRAN_CHANGE']}%\n\n"
message += "🌍 GLOBAL MARKET\n"
for k, v in global_prices.items():
    message += f"{k}: {v}\n"
# ---------------- SEND ----------------
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
print("DONE")