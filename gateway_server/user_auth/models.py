from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_id = models.CharField(max_length=10, primary_key=True)
    # username = models.CharField(max_length=40)
    # password = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    # email = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.user_id


class Register(models.Model):
    token = models.CharField(max_length=15, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=50)
    class Meta:
        db_table = 'register'
    def __str__(self):
        return self.token


class Device(models.Model):
    device_id = models.CharField(max_length=15, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    plate_no = models.CharField(max_length=20)
    class Meta:
        db_table = 'device'
    def __str__(self):
        return self.device_id
