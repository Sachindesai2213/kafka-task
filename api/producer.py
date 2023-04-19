from kafka import KafkaProducer

# create a producer. broker is running on localhost
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0, 11, 5),
)
