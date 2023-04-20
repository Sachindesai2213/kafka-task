from kafka import KafkaAdminClient
from kafka.admin import NewTopic

admin = KafkaAdminClient(
    bootstrap_servers=['localhost:9092']
)

topics = ['type1', 'type2', 'type3', 'type4', 'type5', 'type6',
          'type7', 'type8']

admin.delete_topics(topics=['type6type7'])

for topic in topics:
    try:
        admin.create_topics([NewTopic(name=topic, num_partitions=1,
                                      replication_factor=1)])
    except Exception:
        print('Error while creating topics')
    finally:
        print('Done')

print(admin.list_topics())
