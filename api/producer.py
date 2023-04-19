from kafka import KafkaProducer
import json

# create a producer. broker is running on localhost
producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'],
    api_version=(0, 11, 5),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
