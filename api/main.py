from fastapi import FastAPI, Body
from producer import producer

app = FastAPI()


@app.post('/api/messages')
def save_messages(messages=Body()):
    for message in messages:
        producer.send('quickstart-events', value=message)
    return 'Saved Successfully'
