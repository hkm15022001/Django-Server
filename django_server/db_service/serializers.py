from rest_framework import serializers
from .models import TrackAndTrace


class TrackAndTraceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackAndTrace
        fields = "__all__"








