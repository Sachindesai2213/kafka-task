from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'quickstart-events',
    group_id=None,
    bootstrap_servers=['127.0.0.1:9092'],  # bootstrap server
    # api_version=(0, 11, 3),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
print(consumer.config)
print(consumer.bootstrap_connected())

for msg in consumer:
    print(msg)
