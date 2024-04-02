import requests
import environ
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import time


BASE_DIR = Path(__file__).resolve().parent

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

bot_token = env.str("BOT_TOKEN")
url = env.str("URL_SEND_TELEGRAM")

recipients = [
    env.str("TO_TELEGRAM"),
    env.str("TO_TELEGRAM_2"),
    env.str("TO_TELEGRAM_I"),
    env.str("TO_TELEGRAM_4")
]

start_value = env.int("START_VALUE")
end_value = env.int("AND_VALUE")
new_event_ids = [str(i) for i in range(start_value, end_value + 1)]

start_time = time.time()
time_to_wait = 60 * 60 * 2  # 60*60*2=2 hours, 60*30=0,5 hour

page = env.str("PAGE")
konotop = env.str("KONOTOP")


def prepare_message(spectacle, current_url):
    message = f"Квитки на {spectacle} можна замовити за посиланням: {current_url}"
    return message


def send_mail(telegram_chat_id, message):
    params = {
        'chat_id': telegram_chat_id,
        'text': message
    }
    return requests.get(url, params=params)


new_event_count, new_scope, new_except = 0, 0, 0
while True:
    try:
        print(f"{datetime.now()}: start cycle.")
        for new_event_id in new_event_ids:
            current_page = f"{page}{new_event_id}"
            try:
                response = requests.get(current_page)
                if response.status_code == 200:
                    print(current_page)
                    soup = BeautifulSoup(response.content, "html.parser")
                    contents = soup.find("h1").contents
                    h1_tag = contents[0] if contents else None
                    if new_scope < 20:
                        msg_new_scope = prepare_message(h1_tag, current_page)
                        for chat_id in recipients[:2]:
                            send_mail(chat_id, msg_new_scope)
                        new_scope += 1
                    if new_event_count < 1 and h1_tag == konotop:
                        msg = prepare_message(h1_tag, current_page)
                        for chat_id in recipients:
                            send_mail(chat_id, msg)
                        new_event_count += 1
                        print(f"{datetime.now()}: found {h1_tag}")
            except requests.exceptions.RequestException as e:
                print(f"Error pinging {current_page}: {e}")
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= time_to_wait:
            start_time = time.time()
            send_mail(recipients[0], "The cycle is still working.")
        print(f"{datetime.now()}: end cycle.")
        time.sleep(120)
    except Exception as e:
        print(f"{datetime.now()}: {e}")
        if new_except < 10:
            send_mail(recipients[0], f"Warning. {e}")
            new_except += 1
