from datetime import datetime
import environ
import time
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import smtplib
from email.mime.text import MIMEText


BASE_DIR = Path(__file__).resolve().parent

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

SUBJECT_MAIl = "Конотопська відьма"
SENDER = env.str("FROM_EMAIL")
PASSWORD = env.str("PASSWORD")

recipients = [
    env.str("TO_EMAIL"),
    env.str("TO_EMAIL_2"),
    env.str("TO_EMAIL_7"),
    env.str("TO_EMAIL_8"),
    env.str("TO_EMAIL_9"),
    env.str("TO_EMAIL_4"),
    env.str("TO_EMAIL_5"),
    env.str("TO_EMAIL_6"),
    env.str("TO_EMAIL_3")
]

event_ids = [
    env.str("ID_2")
]

start_value = env.int("START_VALUE")
end_value = env.int("AND_VALUE")
new_event_ids = [str(i) for i in range(start_value, end_value + 1)]

start_time = time.time()
time_to_wait = 60 * 60 * 2  # 60*60*2=2 hours, 60*30=0,5 hour

page = env.str("PAGE")


def prepare_mail(body_mail, subject, sender, recipients_mail):
    msg_p = MIMEText(body_mail)
    msg_p["Subject"] = subject
    msg_p["From"] = sender
    msg_p["To"] = ', '.join(recipients_mail)
    return msg_p


def send_mail(msg_s, recipients_s):
    with smtplib.SMTP_SSL(env.str("SMTP_SERVER"), env.int("SMTP_PORT")) as smtp_server:
        smtp_server.login(SENDER, PASSWORD)
        smtp_server.sendmail(SENDER, recipients_s, msg_s.as_string())
    print(f"{datetime.now()}: message sent!")


event_count, new_event_count, new_scope, new_except = 0, 0, 0, 0
while True:
    try:
        print(f"{datetime.now()}: start cycle.")
        for event_id in event_ids:
            current_page = f"{page}{event_id}"
            try:
                response = requests.get(current_page)
                if response.status_code == 200 and event_count < 5:
                    body = f"Квитки на виставу: Конотопська відьма можна замовити за посиланням: {current_page}"
                    msg_old_scope = prepare_mail(body, SUBJECT_MAIl, SENDER, recipients)
                    send_mail(msg_old_scope, recipients)
                    event_count += 1
            except requests.exceptions.RequestException as e:
                print(f"Error pinging {current_page}: {e}")

        for new_event_id in new_event_ids:
            current_page = f"{page}{new_event_id}"
            try:
                response = requests.get(current_page)
                if response.status_code == 200:
                    print(current_page)
                    if new_scope < 20:
                        msg_new_scope = prepare_mail(
                            f"Посилання на виставу:  {current_page}",
                            "PC. З'явилась нова вистава.",
                            SENDER,
                            recipients[:5]
                        )
                        send_mail(msg_new_scope, recipients[:5])
                        new_scope += 1
                    soup = BeautifulSoup(response.content, "html.parser")
                    contents = soup.find("h1").contents
                    h1_tag = contents[0] if contents else None
                    konotop = "Конотопська відьма"
                    if new_event_count < 1 and h1_tag == konotop:
                        body = f"Квитки на виставу: {h1_tag} можна замовити за посиланням: {current_page}"
                        msg = prepare_mail(body, konotop, SENDER, recipients)
                        send_mail(msg, recipients)
                        new_event_count += 1
                        print(f"{datetime.now()}: found {h1_tag}")
            except requests.exceptions.RequestException as e:
                print(f"Error pinging {current_page}: {e}")

        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= time_to_wait:
            start_time = time.time()
            msg_revert = prepare_mail(
                "The cycle is still working.",
                "PC. The cycle is still working.",
                SENDER,
                recipients[0]
            )
            send_mail(msg_revert, recipients[0])
        print(f"{datetime.now()}: end cycle.")
        time.sleep(60)
    except Exception as e:
        print(f"{datetime.now()}: {e}")
        if new_except < 10:
            msg_except = prepare_mail(
                f"Warning. {e}",
                "PC. Warning.",
                SENDER,
                recipients[0]
            )
            send_mail(msg_except, recipients[0])
            new_except += 1
