from .models import User, Register, Device
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        

class RegisterSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Register
        fields = ["token", "user_id"]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["device_id", "user_id", "device_name", "plate_no"]
