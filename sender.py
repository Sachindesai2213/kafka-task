from apscheduler.schedulers.background import BlockingScheduler
import random
import requests
import json
import time

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

counter = 0
timer = time.time()

def random_messages():
    global counter
    global timer
    messages_counter = random.randint(1, 101)
    messages = random.choices(messages_list, k=100)
    response = requests.post('http://127.0.0.1:8000/api/messages',
                             json.dumps(messages))
    counter += messages_counter
    timer += time.time() - timer
    print(counter, response, timer)


sched = BlockingScheduler()
sched.add_job(random_messages, 'interval', seconds=1)

sched.start()
