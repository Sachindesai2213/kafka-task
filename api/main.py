from datetime import datetime, timedelta

import mysql.connector
from fastapi import Body, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from producer import producer
# from consumer import save_to_database
import time

app = FastAPI()

templates = Jinja2Templates(directory='templates')


connection = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='kafka_task'
)
cursor = connection.cursor()

messages_list = [
    {'id': 'type1', 'message': 'Defective Product',
     'table': 'defective_products'},
    {'id': 'type2', 'message': 'Product in good condition',
     'table': 'good_condition_products'},
    {'id': 'type3', 'message': 'Broken product received',
     'table': 'broken_products'},
    {'id': 'type4', 'message': 'Delay in delivery', 'table': 'delivery_delay'},
    {'id': 'type5', 'message': 'Motor not working', 'table': 'motor_issue'},
    {'id': 'type6', 'message': 'Incorrect Color', 'table': 'size_incorrect'},
    {'id': 'type7', 'message': 'Incorrect Size', 'table': 'color_incorrect'},
    {'id': 'type8', 'message': 'Rude delivery person',
     'table': 'rude_delivery_person'},
]


@app.post('/api/messages')
def save_messages(messages=Body()):
    timer = time.time()
    for message in messages:
        # save_to_database(message, f'type{str(message["id"])}',
        #                  message['message'])
        # producer.send(
        #     'quickstart-events',
        #     value=message['message'].encode('utf-8'),
        #     headers=[('key', str(message['id']).encode('utf-8'))]
        # )
        topic = f'type{str(message["id"])}'
        producer.send(
            topic,
            value=message['message'].encode('utf-8'),
            headers=[('key', str(message['id']).encode('utf-8'))]
        )
        ''' Time taken for a producer to send messages to diff topics
        consumes more time than sending messages to same topic '''
    print(time.time() - timer)
    return 'Saved Successfully'


@app.get('/messages', response_class=HTMLResponse)
def get_messages(request: Request):
    data = []
    start_time = datetime(2023, 4, 19, 23, 40, 0)
    end_time = start_time + timedelta(minutes=10)
    while start_time < end_time:
        temp = {
            'start': str(start_time),
            'end': str(start_time + timedelta(seconds=30))
        }
        for message_type in messages_list:
            query = "SELECT * FROM " + message_type['table'] + \
                " WHERE timestamp BETWEEN %s AND %s"
            cursor.execute(
                query,
                (temp['start'], temp['end'])
            )
            temp[message_type['table']] = len(cursor.fetchall())
        data.append(temp)
        start_time += timedelta(seconds=30)
    print(data)
    context = {
        'request': request,
        'data': data
    }
    return templates.TemplateResponse('messages.html', context)
