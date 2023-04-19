from apscheduler.schedulers.background import BlockingScheduler
import random
import requests
import json

messages_list = [
    {'id': 1, 'message': 'Defective Product'},
    {'id': 2, 'message': 'Product in good condition'},
    {'id': 3, 'message': 'Broken product received'},
    {'id': 4, 'message': 'Delay in delivery'},
    {'id': 5, 'message': 'Motor not working'},
    {'id': 6, 'message': 'Incorrect Color'},
    {'id': 7, 'message': 'Incorrect Size'},
    {'id': 8, 'message': 'Rude delivery person'},
]


def random_messages():
    messages = random.choices(messages_list, k=random.randint(1, 101))
    response = requests.post('http://127.0.0.1:8000/api/messages',
                             json.dumps(messages))
    print(response)


sched = BlockingScheduler()
sched.add_job(random_messages, 'interval', seconds=1)

sched.start()
