from confluent_kafka import Consumer, KafkaError

# Cấu hình Kafka
kafka_config = {
    'bootstrap.servers': 'your_kafka_broker_url',
    'group.id': 'your_consumer_group_id',
    'auto.offset.reset': 'earliest'
}

# Tạo Kafka Consumer
consumer = Consumer(kafka_config)

# Subscribe đối tượng Consumer đến các topic bạn quan tâm
consumer.subscribe(['your_topic_name'])

# Lặp để lắng nghe tin nhắn từ Kafka
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

# Đừng quên đóng consumer khi bạn đã hoàn thành
consumer.close()