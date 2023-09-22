from django.db import models


    
class TrackAndTrace(models.Model):
    device_id = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    speed = models.FloatField(max_length=10)
    direction = models.CharField(max_length=50)
    longitude = models.FloatField(max_length=10)
    latitude = models.FloatField(max_length=10)
    extra_info = models.JSONField()
    def __str__(self):
        return self.track_and_trace_id
