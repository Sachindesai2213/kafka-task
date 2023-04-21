import uuid
from datetime import datetime

import mysql.connector
from kafka import KafkaConsumer
from multiprocessing import Process
import pytz

# set timezone to IST
timezone = pytz.timezone('Asia/Kolkata')

connection = mysql.connector.connect(
    user='root',
    password='Root@123',
    host='localhost',
    database='kafka_task'
)
cursor = connection.cursor()


def save_to_database(message, type, data):
    print(message, type, data)
    timestamp = datetime.fromtimestamp(message.timestamp / 1000.0, timezone)
    # timestamp = datetime.now()
    if type == 'type1':
        query = "INSERT INTO defective_products \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    elif type == 'type2':
        query = "INSERT INTO good_condition_products \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    elif type == 'type3':
        query = "INSERT INTO broken_products \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    elif type == 'type4':
        query = "INSERT INTO delivery_delay \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    elif type == 'type5':
        query = "INSERT INTO motor_issue \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    elif type == 'type6':
        query = "INSERT INTO size_incorrect \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    elif type == 'type7':
        query = "INSERT INTO color_incorrect \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    elif type == 'type8':
        query = "INSERT INTO rude_delivery_person \
            (`type`, `user_id`, `timestamp`, `inserted_on`) \
            VALUES (%s, %s, %s, %s)"
        # Execute the INSERT query
        cursor.execute(query, (data, str(uuid.uuid1()),
                               timestamp, str(datetime.now())))
    # Commit the changes to the database
    connection.commit()
    print('Done')


if __name__ == '__main__':
    consumer = KafkaConsumer(
        'quickstart-events',
        group_id=None,
        bootstrap_servers=['localhost:9092'],  # bootstrap server
        api_version=(0, 11, 3),
        auto_offset_reset='latest',
        enable_auto_commit=True,
    )

    print(consumer.config)
    print(consumer.bootstrap_connected())

    for message in consumer:
        data = message.value.decode('utf-8')
        headers = message.headers
        type = headers[0][1].decode('utf-8')
        save_to_database(message, f'type{type}', data)
        # process = Process(
        #     target=save_to_database,
        #     args=(message, f'type{type}', data,)
        # )
        # process.start()
        # process.join()
