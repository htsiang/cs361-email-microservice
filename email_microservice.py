import sys
import smtplib
import datetime as dt
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
USERNAME = os.getenv('EMAIL_USERNAME')
PASSWORD = os.getenv('EMAIL_PASSWORD')
SUCCESS = {"message":"email notification successful"}
FAILED = {"message": "failed to send email notification"}

class ReminderEmail(BaseModel):
    destination_email: str
    date_year: int
    date_month: int
    date_day: int
    date_hour: int
    date_min: int
    task_title: str
    task_description: str
    task_due_date: str

app = FastAPI()

async def send_email(destination_email, subject, content):
    sender = "drinktea09@gmail.com"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = destination_email
    msg.attach(MIMEText(content))

    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(USERNAME, PASSWORD)

    try:
        mailserver.sendmail(sender, destination_email, msg.as_string())
    finally:
        mailserver.quit()

@app.post("/email/task_reminder", status_code=201)
async def send_task_reminder_email(email: ReminderEmail):
    content = "Task: " + email.task_title + "\nDue: " + email.task_due_date + "\nDescription: " + email.task_description
    subject = "Reminder: " + email.task_title

    # format is (year, month, day, hour, minute, second)
    send_time = dt.datetime(email.date_year, email.date_month, email.date_day, email.date_hour, email.date_min, 0)
    print(send_time.timestamp()-time.time())
    time.sleep(send_time.timestamp()-time.time())

    try:
        await send_email(email.destination_email, subject, content)
        return SUCCESS
    except:
        sys.exit("mail failed")