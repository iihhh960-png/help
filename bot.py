import requests
import schedule
import time
from flask import Flask
from threading import Thread

# --- Flask Server ဆောက်ခြင်း (Render Web Service အတွက်) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# --- Bot ရဲ့ အဓိက အလုပ်များ ---
TOKEN = "8132455544:AAGhjdfo3DvXlosgWuBWSJHAh9g1-mY11Fg"
CHAT_ID = "-1003628384777"

MORNING_MSG = """မောနင်းးပါခမျ
သတ္တဝါများစွာ ဘေးရန်ကွာ ချမ်းသာကြပါစေ။
မေတ္တာရေချမ်း သွန်းကာဖြန်း ငြိမ်းချမ်းကြပါစေ။
သက်ရှည် ကျန်းမာ စိတ်ချမ်းသာ လိုရာဆန္ဒပြည့်ပါစေ။

"""

NIGHT_MSG = """GN ပါ အားလုံးကိုချစ်တယ်နော် 😘
ဘယ်တော့မှထားမသွား"""

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
        print(f"Message Sent: {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error: {e}")

# Render Timezone (UTC) နဲ့ ညှိရန်
# မြန်မာစံတော်ချိန် (မနက် ၆) = UTC (ည ၁၁:၃၀)
# မြန်မာစံတော်ချိန် (ည ၁၀) = UTC (နေ့လယ် ၃:၃၀)
schedule.every().day.at("23:30").do(send_telegram_msg, message=MORNING_MSG)
schedule.every().day.at("15:30").do(send_telegram_msg, message=NIGHT_MSG)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    # Flask ကို Thread နဲ့ Background မှာ ပေးမောင်းထားခြင်း
    t = Thread(target=run_schedule)
    t.start()
    run_flask()
