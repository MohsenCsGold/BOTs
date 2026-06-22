import requests
import time

BOT_TOKEN = "51205423:Y8rb0kJwjEGJYInrKJLLLh1yCzBKP32dLqI"
CHANNEL_ID = "4315994987"

LAST_PRICE = None


def get_gold_price():
     # url = "https://www.gold-api.com/price/XAU"
    url_gold = "https://api.gold-api.com/price/XAU/USD"
    r = requests.get(url_gold, timeout=10)
    data = r.json()
    return data["price"]

def get_btc_price():
     # url = "https://www.gold-api.com/price/XAU"
    url_btc = "https://api.gold-api.com/price/BTC/USD"
    r = requests.get(url_btc, timeout=10)
    data = r.json()
    return data["price"]


def send_message(text):
    url = f"https://tapi.bale.ai/{BOT_TOKEN}/sendMessage"
    #url = f"https://tapi.bale.ai/{BOT_TOKEN}/getUpdates"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "📈 چارت بیت کوین",
                        "url": "https://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT"
                    },
                    {
                        "text": "🥇 چارت انس جهانی طلا",
                        "url": "https://www.tradingview.com/chart/yEiQgDpV/?symbol=TVC%3AGOLD"

                    }
                ]
            ]
        }
    }
    requests.post(url, json=payload, timeout=10)
    #print("status:", r.status_code)
    #print("response:", r.text)



while True:
    try:
        gold_price = get_gold_price()
        btc_price = get_btc_price()

        #if price != LAST_PRICE:
        #    msg = (
        #        "🟡 انس جهانی طلا (XAU/USD)\n\n"
        #        f"💰 {price:,.2f} USD\n\n"
        #        f"⏰ {time.strftime('%Y-%m-%d %H:%M:%S')}"
        #    )

        msg = (
            "GOLD: "
            f"{gold_price:,.2f} | BTC: "
            f"{btc_price:,.2f}"
            )
            #f"⏰ {time.strftime('%Y-%m-%d %H:%M:%S')}"

        send_message(msg)
        print (msg)
        #LAST_PRICE = price
        time.sleep(60)
    except Exception as e:
        print(e)
        time.sleep(60)
