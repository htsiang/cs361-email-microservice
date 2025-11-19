const body = {
    "destination_email": "htsiang1@gmail.com",
    "date_year": 2025,
    "date_month": 11,
    "date_day": 18,
    "task_title": "testing this reminder",
    "task_description": "description test",
    "task_due_date": "2025-11-18"
}

// try {
// const response = await 
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
    console.log(obj);
}).catch(err => {
    console.log(err.message);
});

    // const result = response.json()
    // console.log(result)
// } catch (err) {
//     console.log(err.message);
// };