from confluent_kafka import Consumer, KafkaError
def kafka_consumer():
    kafka_config = {
        'bootstrap.servers': 'localhost:29092',
        'group.id': 'django-server',
        'auto.offset.reset': 'earliest'
    }

    topic = "alo"

    consumer = Consumer(kafka_config)

    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Reached end of partition')
            else:
                print('Error: %s' % msg.error())
        else:
            print('Received message: %s' % msg.value())

    consumer.close()

if __name__ == '__main__':
    kafka_consumer()