import requests
from datetime import datetime , time as dt_time
import time
import jdatetime


bale_BOT_TOKEN = "51205423:Y8rb0kJwjEGJYInrKJLLLh1yCzBKP32dLqI"
# Bitcoin and Gold Live price
bale_CHANNEL_ID = "4315994987"
#Daily Today Message
bale_Emruz_CHANNEL_ID = "5774042077"
telegram_BOT_TOKEN = "8824001694:AAHmsfRoFl_QE2I_VR6dfO9OED6ydtxFX_Y"
telegram_CHANNEL_ID = "-1003824337954"

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
    bale_url = f"https://tapi.bale.ai/{bale_BOT_TOKEN}/sendMessage"
    telegram_url = f"https://api.telegram.org/bot{telegram_BOT_TOKEN}/sendMessage"

    #for Bale
    bale_payload = {
        "chat_id": bale_CHANNEL_ID,
        "text": text,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "📈 چارت بیت کوین",
                        "url": "https://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT"
                    },
                    {
                        "text": "🥇 چارت طلا",
                        "url": "https://www.tradingview.com/chart/yEiQgDpV/?symbol=TVC%3AGOLD"

                    }
                ]
            ]
        }
    }
    #for Telegram
    telegram_payload = {
        "chat_id": telegram_CHANNEL_ID,
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
    requests.post(bale_url, json=bale_payload, timeout=10)
    #requests.post(telegram_url, json=telegram_payload , timeout = 10)
    #print("status:", r.status_code)
    #print("response:", r.text)

def send_daily_message(msg):
    bale_url = f"https://tapi.bale.ai/{bale_BOT_TOKEN}/sendMessage"

    #for Bale
    bale_emruz_payload = {
        "chat_id": bale_Emruz_CHANNEL_ID,
        "text": msg,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "مشاهده تقویم",
                        "url": "https://time.ir"
                    }
                ]
            ]
        }
    }
    requests.post(bale_url, json=bale_emruz_payload, timeout=10)


def persianWeekDay(dayofweek):
    WEEK_DAYS = {
    0: "دوشنبه",
    1: "سه‌شنبه",
    2: "چهارشنبه",
    3: "پنجشنبه",
    4: "جمعه",
    5: "شنبه",
    6: "یکشنبه"
    }
    return WEEK_DAYS[dayofweek]
dayPrinted = False
while True:
    try:
        gold_price = get_gold_price()
        btc_price = get_btc_price()
        theDay = datetime.now()
        msg = (
            "GOLD: "
            f"{gold_price:,.2f} | BTC: "
            f"{btc_price:,.2f}"
            )
            #f"⏰ {time.strftime('%Y-%m-%d %H:%M:%S')}"

        send_message(msg)
        print (msg)

        # Emruz Channel
        if theDay.hour ==0 and theDay.minute == 5:
            #send_daily_message(msg)
            print (theDay.time())
            msg = persianWeekDay(theDay.weekday()) + jdatetime.datetime.now().strftime(" %d-%m-%Y ")
            send_daily_message(msg)
            print(msg)
            dayPrinted = True

        time.sleep(60)
    except Exception as e:
        print(e)
        time.sleep(60)
