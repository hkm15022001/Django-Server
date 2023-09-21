from django.db.models.signals import Signal
from django.dispatch import receiver
from kafka_service.consumer import kafka_consumer  # Import Kafka consumer function

startup_signal = Signal()

# register revicer function
@receiver(startup_signal)
def on_startup(sender, **kwargs):
    # call reciever funciton
    kafka_consumer()