from rest_framework import serializers
from .models import User, Register, Device


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "username",
            "password",
            "gender",
            "email",
            "date_of_birth",
            "phone_number",
            "balance",
            "user_role",
        ]

class RegisterSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Register
        fields = ["token", "user_id"]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["device_id", "user_id", "device_name", "plate_no"]
