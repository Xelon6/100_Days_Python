import os
import sched
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import random

os.chdir(os.path.dirname(os.path.realpath(__file__)))
load_dotenv()



FILENAME = "motivational_quotes.txt"
password = os.getenv("APP_PW")
username = os.getenv("MAIL_USER")

scheduler = sched.scheduler(time.time, time.sleep)

def get_quote(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        quotes = f.readlines()
    return random.choice(quotes)

def send_mail(sc):
    email = get_quote(FILENAME)
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)
    msg = MIMEMultipart()
    msg['To'] = username
    msg['From'] = username
    msg['Subject'] = "Your Daily Motivational Quote"
    msg.attach(MIMEText(email, 'html'))
    s.send_message(msg)
    del msg
    s.quit()

    # Planen Sie den nächsten E-Mail-Versand in 24 Stunden.
    scheduler.enter(24 * 60 * 60, 1, send_mail, (sc,))

# Sende die erste E-Mail sofort.
scheduler.enter(0, 1, send_mail, (scheduler,))

scheduler.run()
