import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sched
import time

# Ändere das Arbeitsverzeichnis zum Verzeichnis dieser Datei
os.chdir(os.path.dirname(os.path.realpath(__file__)))
load_dotenv()

# Lade Umgebungsvariablen aus der .env-Datei
password = os.getenv("APP_PW")
username = os.getenv("MAIL_USER")

# Verbinde mit der SQLite-Datenbank oder erstelle sie, wenn sie nicht existiert
conn = sqlite3.connect('events.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS posts
            (title TEXT, links TEXT)""")

# URL der Seite, die gescannt werden soll
url = "https://replit.com/community-hub"

# HTML von der Webseite abrufen und parsen
response = requests.get(url, timeout=5)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Ereignisse auf der Seite finden
events = soup.find_all("a", {"class": "css-epm014"})

# Suchbegriffe für die Ereignisse
search = ["Startup", "ModelFarm"]

# Funktion zum Abrufen und Speichern neuer Ereignisse
def get_new_events():
    new_events = []
    for event in events:
        event_title = event.find("span", {"class": "css-scxoy8"})
        for term in search:
            if event and term in event_title.text:
                title = event_title.text
                link = event["href"]
                c.execute("SELECT * FROM posts WHERE title = ? OR links = ?", (title, link))
                existing_data = c.fetchone()
                if not existing_data:
                    with conn:
                        c.execute("INSERT INTO posts VALUES (?, ?)", (title, link))
                    new_events.append([title, link])
    return new_events

# Funktion zum Erstellen des E-Mail-Inhalts
def get_title_link(data):
    return "\n".join([f"{thing[0]}: {thing[1]}" for thing in data])

# Erstelle einen Scheduler für wiederkehrende Aufgaben
scheduler = sched.scheduler(time.time, time.sleep)

# Funktion zum Senden der E-Mail
def send_mail(email_content):
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)
    msg = MIMEMultipart()
    msg['To'] = username
    msg['From'] = username
    msg['Subject'] = "Found These Interesting New Posts"
    msg.attach(MIMEText(email_content, 'html'))
    s.send_message(msg)
    del msg
    s.quit()

# Funktion, die Wrapper für den E-Mail-Versand und die erneute Planung des Schedulers enthält
def send_mail_wrapper(sc):
    new_events = get_new_events()
    if new_events:
        email_content = get_title_link(new_events)
        send_mail(email_content)
    # Wiederholen Sie die Überprüfung alle 6 Stunden
    scheduler.enter(6 * 3600, 1, send_mail_wrapper, (sc,))

# Starten Sie den Scheduler und planen Sie die erste Ausführung der Wrapper-Funktion
scheduler.enter(0, 1, send_mail_wrapper, (scheduler,))
scheduler.run()
