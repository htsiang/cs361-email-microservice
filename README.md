# cs361-email-microservice
A FastAPI based microservice for CS361 for email reminders.

## Install dependencies
pip install -r requirements.txt

## Start service
fastapi dev email_microservice.py<br>
The service will run on http://127.0.0.1:8000/

To start the program
**USE THIS:** uvicorn email_microservice:app --reload

# Communication Contract
## Function to Send Email for Task Reminder
### Endpoint POST/email/task_reminder
#### How to REQUEST Data:
Send a POST request with a JSON body to the endpoint.<br>
Request body (JSON): <br>
```
{
    "destination_email": string,
    "date_year": int,
    "date_month": int,
    "date_day": int,
    "date_hour": int,
    "date_min": int,
    "task_title": string,
    "task_description": string,
    "task_due_date": string
}
```

#### How to RECEIVE Data:
The service returns a JSON response with a message confirming that the email was successfully sent.<br>
Response (JSON): <br>
```
{
    "message": "email notification successful"
}
```

#### Send Email for Task Reminder Example (Javascript using Fetch)
```
fetch('http://127.0.0.1:8000/email/task_reminder', {
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify(body)
}).then(res => {
    return res.json();
}).then(obj => {
    // sample code dealing with response body
    console.log(obj);
})
```

# UML Sequence Diagram

<img width="648" height="585" alt="Screenshot 2025-11-18 at 7 24 49 PM" src="https://github.com/user-attachments/assets/b9bcd092-4152-455a-a7a3-3e0c5f00cc32" />