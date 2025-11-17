import sys
import smtplib
import datetime as dt
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

# load_dotenv()
# EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')

class ReminderEmail(BaseModel):
    destination_email: str
    date_year: int
    date_month: int
    date_day: int
    task_title: str
    task_description: str
    task_due_date: str

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/email")
async def send_email(email: ReminderEmail):
    sender = "drinktea09@gmail.com"
    # destination = "htsiang1@gmail.com"
    destination = email.destination_email

    USERNAME = "drinktea09@gmail.com"
    PASSWORD = "kglmekepakebbtrj"

    # content = "TEST"
    content = "Task: " + email.task_title + "\nDue: " + email.task_due_date + "\nDescription: " + email.task_description

    # subject = "TEST"
    subject = "Reminder: " + email.task_title

    # format is (year, month, day, hour, minute, second)
    send_time = dt.datetime(email.date_year, email.date_month, email.date_day, 4, 58, 0)
    print(send_time.timestamp()-time.time())
    time.sleep(send_time.timestamp()-time.time())

    try:
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = destination
        msg.attach(MIMEText(content))

        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(USERNAME, PASSWORD)

        try:
            mailserver.sendmail(sender, destination, msg.as_string())
        finally:
            mailserver.quit()
    except:
        sys.exit("mail failed")