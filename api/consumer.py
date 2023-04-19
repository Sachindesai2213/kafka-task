import uuid
from datetime import datetime

import mysql.connector
from kafka import KafkaConsumer

connection = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='kafka_task'
)
cursor = connection.cursor()

consumer = KafkaConsumer(
    'quickstart-events',
    group_id=None,
    bootstrap_servers=['localhost:9092'],  # bootstrap server
    api_version=(0, 11, 3),
    auto_offset_reset='latest',
    enable_auto_commit=True
)
print(consumer.config)
print(consumer.bootstrap_connected())

for message in consumer:
    data = message.value.decode('utf-8')
    headers = message.headers
    type = headers[0][1].decode('utf-8')
    if type == 'type1':
        query = "INSERT INTO defective_products \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    elif type == 'type2':
        query = "INSERT INTO good_condition_products \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    elif type == 'type3':
        query = "INSERT INTO broken_products \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    elif type == 'type4':
        query = "INSERT INTO delivery_delay \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    elif type == 'type5':
        query = "INSERT INTO motor_issue \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    elif type == 'type6':
        query = "INSERT INTO size_incorrect \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    elif type == 'type7':
        query = "INSERT INTO color_incorrect \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    elif type == 'type8':
        query = "INSERT INTO rude_delivery_person \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               message.timestamp, str(datetime.now())))
    # Commit the changes to the database
    connection.commit()
