from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10,primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=255)
    date_of_birth = models.DateField
    phone_number = models.CharField(max_length=20)
    balance = models.IntegerField
    user_role=models.CharField(max_length=50)

    def __str__(self):
        return self.user_id
    

class Register(models.Model):
    token = models.CharField(max_length=15,primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.token
    


class Device(models.Model):
    device_id=models.CharField(max_length=15,primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    plate_no=models.CharField(max_length=20)
    def __str__(self):
        return self.device_id
    
