import os
import requests
import smtplib
from email.mime.text import MIMEText

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

def main():
    try:
        r = requests.get(URL, timeout=10)
        if r.status_code != 404:
            send_email()
            print("✅ La page est dispo, email envoyé.")
        else:
            print("❌ Toujours 404.")
    except Exception as e:
        print("⚠️ Erreur:", e)

if __name__ == "__main__":
    main()