from fastapi import FastAPI, Body
from producer import producer

app = FastAPI()


@app.post('/api/messages')
def save_messages(messages=Body()):
    print(type(messages))
    for message in messages:
        print(message)
        producer.send('quickstart-events', value=message)
    return 'Saved Successfully'
