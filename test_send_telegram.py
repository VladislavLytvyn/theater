import requests
import environ
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

bot_token = env.str("BOT_TOKEN")
url = env.str("URL_SEND_TELEGRAM")
chat_id = env.str("TO_TELEGRAM")

message = f"привіт)"
params = {
    'chat_id': chat_id,
    'text': message
}

requests.get(url, params=params)

response = requests.get(url, params=params)
if response.status_code == 200:
    print("Message was sent.")
else:
    print("Error", response.text)


# send for few chat_ids
# chat_ids = [
#     env.str("TO_TELEGRAM"),
#     env.str("TO_TELEGRAM_I")
# ]
#
# for chat_id in chat_ids:
#     params = {
#         'chat_id': chat_id,
#         'text': str(chat_id)
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         print("Message was sent.")
#     else:
#         print("Error", response.text)
