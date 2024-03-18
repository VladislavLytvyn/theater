# import environ
# import time
# import requests
# from sendgrid import *
# from sendgrid.helpers.mail import *
# from pathlib import Path
#
#
# BASE_DIR = Path(__file__).resolve().parent
#
# env = environ.Env()
# environ.Env.read_env(str(BASE_DIR / ".env"))
#
# theater_sendgrid = sendgrid.SendGridAPIClient(env.str("SEND_GRID_API_CLIENT"))
# from_email = Email(env.str("FROM_EMAIL"))
# to_email = To(env.str("TO_EMAIL"))
#
# # Try to send to few emails:
# # to_email = To(env.str("TO_EMAIL"), env.str("TO_EMAIL_2"))
#
# subject = "Ping Successful!!!"
#
# pages = [
#     'http://tickets.ft.org.ua/web/event/event_id/4803',
#     'http://tickets.ft.org.ua/web/event/event_id/4855',
#     'http://tickets.ft.org.ua/web/event/event_id/4868'
# ]
#
# while True:
#     for page in pages:
#         try:
#             response = requests.get(page)
#             if not response.ok:
#                 content = Content("text/plain", f'Ping to {page} was successful!')
#                 mail = Mail(from_email, to_email, subject, content)
#                 mail_json = mail.get()
#                 response = theater_sendgrid.client.mail.send.post(request_body=mail_json)
#                 print(response.status_code)
#                 print(response.headers)
#
#                 # Try to send to few emails:
#                 # emails = [env.str("TO_EMAIL"), env.str("TO_EMAIL_2")]
#                 # for email in emails:
#                 #     to_email = To(email)
#                 #     mail = Mail(from_email, to_email, subject, content)
#                 #     mail_json = mail.get()
#                 #     response = theater_sendgrid.client.mail.send.post(request_body=mail_json)
#                 #     print(response.status_code)
#                 #     print(response.headers)
#         except requests.exceptions.RequestException as e:
#             print(f"Error pinging {page}: {e}")
#     time.sleep(60)


# ##############################
# TRY WITHOUT SENDGRID

# import environ
# import time
# import requests
# from sendgrid import *
# from sendgrid.helpers.mail import *
# from pathlib import Path
#
#
# BASE_DIR = Path(__file__).resolve().parent
#
# env = environ.Env()
# environ.Env.read_env(str(BASE_DIR / ".env"))
#
# sg = sendgrid.SendGridAPIClient(env.str("SEND_GRID_API_CLIENT"))
# from_email = Email("apoints96@gmail.com")
# to_email = To("vladyslav.lytvyn96@gmail.com")
# subject = "Ping Successful!!!"
#
# pages = [
#     'http://tickets.ft.org.ua/web/event/event_id/4803',
#     'http://tickets.ft.org.ua/web/event/event_id/4855',
#     'http://tickets.ft.org.ua/web/event/event_id/4868'
# ]
#
# while True:
#     for page in pages:
#         try:
#             response = requests.get(page)
#             if not response.ok:
#                 print("Ping to {page} was't successful!")
#         except requests.exceptions.RequestException as e:
#             print(f"Error pinging {page}: {e}")


# ##############################
# TRY SEND WITH OLD API_KEY. FAILED TO SEND EMAIL

# import environ
# import time
# import requests
# from sendgrid import *
# from sendgrid.helpers.mail import *
# from pathlib import Path
#
#
# BASE_DIR = Path(__file__).resolve().parent
#
# env = environ.Env()
# environ.Env.read_env(str(BASE_DIR / ".env"))
#
# theater_sendgrid = sendgrid.SendGridAPIClient(api_key = env.str("SendGridAPIClient"))
# from_email = Email("apoints96@gmail.com")
# to_email = To("vladyslav.lytvyn96@gmail.com")
# subject = "Ping Successful!!!"
#
# pages = [
#     'http://tickets.ft.org.ua/web/event/event_id/4803'
# ]
#
# for page in pages:
#     try:
#         response = requests.get(page)
#         if not response.ok:
#             content = Content("text/plain", f'Ping to {page} was successful!')
#             mail = Mail(from_email, to_email, subject, content)
#             mail_json = mail.get()
#             response = theater_sendgrid.client.mail.send.post(request_body=mail_json)
#             print(response.status_code)
#             print(response.headers)
#     except requests.exceptions.RequestException as e:
#         print(f"Error pinging {page}: {e}")


# ##############################
# Try send to few emails. And not while:
# import environ
# import requests
# from sendgrid import *
# from sendgrid.helpers.mail import *
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
#
# env = environ.Env()
# environ.Env.read_env(str(BASE_DIR / ".env"))
#
# theater_sendgrid = sendgrid.SendGridAPIClient(env.str("SEND_GRID_API_CLIENT"))
# from_email = Email(env.str("FROM_EMAIL"))
# to_email = To(env.str("TO_EMAIL"))
#
# # Try to send to few emails:
# # to_email = To(
# #     env.str("TO_EMAIL"),
# #     env.str("TO_EMAIL_2")
# # )
#
# subject = "Ping Successful!!!"
#
# pages = [
#     'http://tickets.ft.org.ua/web/event/event_id/4803'
# ]
#
#
# for page in pages:
#     try:
#         response = requests.get(page)
#         if not response.ok:
#             content = Content("text/plain", f'Ping to {page} was successful!')
#             mail = Mail(from_email, to_email, subject, content)
#             mail_json = mail.get()
#             response = theater_sendgrid.client.mail.send.post(request_body=mail_json)
#             print(response.status_code)
#             print(response.headers)
#
#             # Try to send to few emails:
#             # emails = [
#             #     env.str("TO_EMAIL"),
#             #     env.str("TO_EMAIL_2")
#             # ]
#             # for email in emails:
#             #     to_email = To(email)
#             #     mail = Mail(from_email, to_email, subject, content)
#             #     mail_json = mail.get()
#             #     response = theater_sendgrid.client.mail.send.post(request_body=mail_json)
#             #     print(response.status_code)
#             #     print(response.headers)
#     except requests.exceptions.RequestException as e:
#         print(f"Error pinging {page}: {e}")


# ##############################
# SendGrid not found.
# Try send with Gmail.
# Good try. Was needed to install password for app in Gmail settings.

# For future:
# If h1 is not equal to "404" then send email.
# Make list brtter. Add more pages. Add more emails.
# Find site for my script. And run it there. And check if it works. And if it works then it's good.
# And if it's good then it's good.

# from datetime import datetime
# import environ
# import time
# import requests
# from bs4 import BeautifulSoup
# from pathlib import Path
# import smtplib
# from email.mime.text import MIMEText
#
#
# BASE_DIR = Path(__file__).resolve().parent
#
# env = environ.Env()
# environ.Env.read_env(str(BASE_DIR / ".env"))
#
# SUBJECT_MAIl = "Ping Successful!!!"
# SENDER = env.str("FROM_EMAIL")
# PASSWORD = env.str("PASSWORD")
#
# recipients = [
#     env.str("TO_EMAIL"),
#     env.str("TO_EMAIL_2")
# ]
#
# event_ids = [
#     env.str("ID_2"),
#     env.str("ID_3")
# ]
#
# start_value = env.int("START_VALUE")
# end_value = env.int("AND_VALUE")
# new_event_ids = [str(i) for i in range(start_value, end_value + 1)]
#
# start_time = time.time()
# time_to_wait = 60 * 30
#
# page = env.str("PAGE")
#
#
# def prepare_mail(body_mail, subject, sender, recipients_mail):
#     msg_p = MIMEText(body_mail)
#     msg_p["Subject"] = subject
#     msg_p["From"] = sender
#     msg_p["To"] = ', '.join(recipients_mail)
#     return msg_p
#
#
# def send_mail(msg_s):
#     with smtplib.SMTP_SSL(env.str("SMTP_SERVER"), env.int("SMTP_PORT")) as smtp_server:
#         smtp_server.login(SENDER, PASSWORD)
#         smtp_server.sendmail(SENDER, recipients, msg_s.as_string())
#     print(f"{datetime.now()}: message sent!")
#
#
# event_count, new_event_count = 0, 0
# while True:
#     for event_id in event_ids:
#         current_page = f"{page}{event_id}"
#         try:
#             response = requests.get(current_page)
#             if response.status_code == 200 and event_count < 10:
#                 body = f"Ping to {current_page} was successful!"
#                 msg = prepare_mail(body, SUBJECT_MAIl, SENDER, recipients)
#                 send_mail(msg)
#                 event_count += 1
#         except requests.exceptions.RequestException as e:
#             print(f"Error pinging {current_page}: {e}")
#
#     for new_event_id in new_event_ids:
#         current_page = f"{page}{new_event_id}"
#         try:
#             response = requests.get(current_page)
#             if response.status_code == 200:
#                 soup = BeautifulSoup(response.content, "html.parser")
#                 contents = soup.find("h1").contents
#                 h1_tag = contents[0] if contents else None
#                 if h1_tag == "Конотопська відьма" or h1_tag == "Безталанна" and new_event_count < 20:
#                     body = f"Ping to {current_page} was successful!"
#                     msg = prepare_mail(body, SUBJECT_MAIl, SENDER, recipients)
#                     print(f"{datetime.now()}: found {h1_tag}")
#                     send_mail(msg)
#                     new_event_count += 1
#         except requests.exceptions.RequestException as e:
#             print(f"Error pinging {current_page}: {e}")
#
#     current_time = time.time()
#     elapsed_time = current_time - start_time
#     if elapsed_time >= time_to_wait:
#         start_time = time.time()
#         revert_sender = env.str("TO_EMAIL")
#         revert_recipients = env.str("FROM_EMAIL")
#         msg = prepare_mail("Cycle is still working.", "Cycle is still working.", revert_sender, revert_recipients)
#         send_mail(msg)
#     print(f"{datetime.now()}: end cycle.")
#     time.sleep(60)


# ###############################
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

SUBJECT_MAIl = "Ping Successful!!!"
SENDER = env.str("FROM_EMAIL")
PASSWORD = env.str("PASSWORD")

recipients = [
    env.str("TO_EMAIL"),
    env.str("TO_EMAIL_2")
]

event_ids = [
    env.str("ID_2"),
    env.str("ID_3")
]

start_value = env.int("START_VALUE")
end_value = env.int("AND_VALUE")
new_event_ids = [str(i) for i in range(start_value, end_value + 1)]

start_time = time.time()
time_to_wait = 60 * 30 * 2

page = env.str("PAGE")


def prepare_mail(body_mail, subject, sender, recipients_mail):
    msg_p = MIMEText(body_mail)
    msg_p["Subject"] = subject
    msg_p["From"] = sender
    msg_p["To"] = ', '.join(recipients_mail)
    return msg_p


def send_mail(msg_s):
    with smtplib.SMTP_SSL(env.str("SMTP_SERVER"), env.int("SMTP_PORT")) as smtp_server:
        smtp_server.login(SENDER, PASSWORD)
        smtp_server.sendmail(SENDER, recipients, msg_s.as_string())
    print(f"{datetime.now()}: message sent!")


event_count, new_event_count = 0, 0
while True:
    for event_id in event_ids:
        current_page = f"{page}{event_id}"
        try:
            response = requests.get(current_page)
            if response.status_code == 200 and event_count < 10:
                body = f"Ping to {current_page} was successful!"
                msg = prepare_mail(body, SUBJECT_MAIl, SENDER, recipients)
                send_mail(msg)
                event_count += 1
        except requests.exceptions.RequestException as e:
            print(f"Error pinging {current_page}: {e}")

    for new_event_id in new_event_ids:
        current_page = f"{page}{new_event_id}"
        try:
            response = requests.get(current_page)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                contents = soup.find("h1").contents
                h1_tag = contents[0] if contents else None
                if h1_tag == "Конотопська відьма" or h1_tag == "Безталанна" and new_event_count < 20:
                    body = f"Ping to {current_page} was successful!"
                    msg = prepare_mail(body, SUBJECT_MAIl, SENDER, recipients)
                    print(f"{datetime.now()}: found {h1_tag}")
                    send_mail(msg)
                    new_event_count += 1
        except requests.exceptions.RequestException as e:
            print(f"Error pinging {current_page}: {e}")

    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= time_to_wait:
        start_time = time.time()
        revert_sender = env.str("TO_EMAIL")
        revert_recipients = env.str("FROM_EMAIL")
        msg = prepare_mail("Cycle is still working.", "Cycle is still working.", revert_sender, revert_recipients)
        send_mail(msg)
    print(f"{datetime.now()}: end cycle.")
    time.sleep(300)
