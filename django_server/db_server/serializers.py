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

<<<<<<< HEAD
class RegisterSerializer(serializers.ModelSerializer):    
=======

class RegisterSerializer(serializers.ModelSerializer):
>>>>>>> 4dd1177351ba760c9aad5bf907ab760d4ed1f8c4
    class Meta:
        model = Register
        fields = ["token", "user_id"]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["device_id", "user_id", "device_name", "plate_no"]
