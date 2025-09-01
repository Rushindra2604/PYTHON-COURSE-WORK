import smtplib # Simple mail transfer protocol for sending emails
import os # For File path ans file existence checks
import csv # To read email addresses from CSV files
from email.mime.multipart import MIMEMultipart # To create a multipart email
from email.mime.text import MIMEText # For adding plain text to email body

# https://myaccount.google.com/apppasswords

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 # Port used for TLS (encryption)
SENDER_EMAIL = "dasarirushindrareddy@gmail.com"
SENDER_PASSWORD = "wagl tcux ennc gdao" # Use App Passwords for Gmail

def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Error sending email to {to_email}. Error: {e}")

def send_bulk_emails(csv_file, subject, body):
    try:
        csv_path = os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f"Error: CSV file '{csv_file}' not found.")
            return
        
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader,None) # Skip header row if present
            print(reader,"reader")
            for row in reader:
                if row:
                    email = row[0]
                    send_email(email, subject, body)

    except Exception as e:
        print(f"Error reading CSV file. Error: {e}")