import os
import requests

TOKEN = os.environ.get("TG_TOKEN")
CHAT_ID = os.environ.get("TG_CHAT")
SYMBOL = os.environ.get("SYMBOL", "XAUUSD=X")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    msg = f"Jadu monitor chalu ho gaya! Selected symbol: {SYMBOL}. Signals yahan aate rahenge."
    send_telegram_message(msg)