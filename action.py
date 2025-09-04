import os
import requests
import smtplib
from email.mime.text import MIMEText
import time

URL = "https://evenements.elysee.fr/jep"

EMAIL_USER = os.getenv("ELYSEE_EMAIL_USER")
EMAIL_PASS = os.getenv("ELYSEE_EMAIL_PASS")
EMAIL_TO = os.getenv("ELYSEE_EMAIL_TO")

def send_email():
    msg = MIMEText(f"La page {URL} est maintenant disponible !")
    msg["Subject"] = "Page Elysee JEP disponible"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

try:
    r = requests.get(URL)
    if r.status_code != 404:
        send_email()
except Exception as e:
    print("Erreur:", e)
