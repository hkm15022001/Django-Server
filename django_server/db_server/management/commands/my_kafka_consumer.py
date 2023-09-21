from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaError
from db_server.serializers import TrackAndTraceSerializer
import json
class Command(BaseCommand):
    help = 'Starts Kafka consumer'

    def handle(self, *args, **kwargs):
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
                # Chuyển đổi chuỗi bytes thành từ điển JSON
                try:
                    message_data = json.loads(msg.value().decode('utf-8'))  # Giả sử dữ liệu là UTF-8 encoded
                except json.JSONDecodeError as e:
                    print(f'Error decoding JSON: {str(e)}')
                    continue

                # Sử dụng dữ liệu để khởi tạo serializer và lưu vào cơ sở dữ liệu
                serializer = TrackAndTraceSerializer(data=message_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(f'Error validating serializer: {serializer.errors}')

        consumer.close()
