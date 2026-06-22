
import requests
import time

BOT_TOKEN = "51205423:Y8rb0kJwjEGJYInrKJLLLh1yCzBKP32dLqI"
CHANNEL_ID = "@Gold_XAUUSD_LIVE"

LAST_PRICE = None


def get_gold_price():
     # url = "https://www.gold-api.com/price/XAU"
    url = "https://api.gold-api.com/price/XAU/USD"

    r = requests.get(url, timeout=10)
    data = r.json()

    return data["price"]


def send_message(text):
    url = f"https://tapi.bale.ai/{BOT_TOKEN}/getMe"

    payload = {
        "chat_id": "Gold_XAUUSD_Live",
        "text": "text"
    }

    r = requests.post(url, json=payload, timeout=10)

    print("status:", r.status_code)
    print("response:", r.text)

while True:
    try:
        price = get_gold_price()

        if price != LAST_PRICE:
            msg = (
                "🟡 انس جهانی طلا (XAU/USD)\n\n"
                f"💰 {price:,.2f} USD\n\n"
                f"⏰ {time.strftime('%Y-%m-%d %H:%M:%S')}"
            )

            send_message(msg)
            LAST_PRICE = price

        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(60)
