from kafka import KafkaConsumer
from single_consumer import save_to_database
from multiprocessing import Process


def consumer_process(topic):
    # Consumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],  # bootstrap server
        api_version=(0, 11, 3),
        auto_offset_reset='latest',
        enable_auto_commit=True,
    )

    for message in consumer:
        data = message.value.decode('utf-8')
        save_to_database(message, topic, data)


if __name__ == '__main__':
    topics = ['type1', 'type2', 'type3', 'type4', 'type5', 'type6',
          'type7', 'type8']

    for topic in topics:
        process = Process(
            target=consumer_process,
            args=(topic,)
        )
        process.start()
        # process.join()
