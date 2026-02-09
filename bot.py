import requests
import schedule
import time

# --- သတ်မှတ်ချက်များ ---
TOKEN = "8132455544:AAGhjdfo3DvXlosgWuBWSJHAh9g1-mY11Fg"
CHAT_ID = "-1003628384777"

# မနက်ခင်းအတွက် စာသား
MORNING_MSG = """မောနင်းးပါခမျ

သတ္တဝါများစွာ ဘေးရန်ကွာ ချမ်းသာကြပါစေ။

မေတ္တာရေချမ်း သွန်းကာဖြန်း ငြိမ်းချမ်းကြပါစေ။

သက်ရှည် ကျန်းမာ စိတ်ချမ်းသာ လိုရာဆန္ဒပြည့်ပါစေ။



"""

# ညဘက်အတွက် စာသား
NIGHT_MSG = """GN ပါ အားလုံးကိုချစ်တယ်နော် 😘

ဘယ်တော့မှထားမသွား"""

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"စာပို့ပြီးပါပြီ - {time.strftime('%H:%M:%S')}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error occurred: {e}")

# အချိန်ဇယား သတ်မှတ်ခြင်း
# မနက် ၆ နာရီ
schedule.every().day.at("06:00").do(send_telegram_msg, message=MORNING_MSG)

# ည ၁၀ နာရီ (22:00)
schedule.every().day.at("22:00").do(send_telegram_msg, message=NIGHT_MSG)

# အခုချက်ချင်း စမ်းသပ်ဖို့ တစ်ခါပို့ကြည့်မည် (မလိုချင်ရင် အောက်က line ကို ဖျက်နိုင်ပါတယ်)
send_telegram_msg("Bot စတင်အလုပ်လုပ်ပါပြီ။ အချိန်မှန် စာပို့ပေးပါ့မယ်။")

print("Bot စတင်နေပါပြီ... မနက် ၆ နာရီ နှင့် ည ၁၀ နာရီတိုင်း စာပို့ပါမယ်။")

while True:
    schedule.run_pending()
    time.sleep(30)
