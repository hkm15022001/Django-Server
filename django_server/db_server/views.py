from django.shortcuts import render
from .models import User, Register, Device
from rest_framework import generics
from .serializers import UserSerializer, RegisterSerializer, DeviceSerializer


class UserCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new User
    queryset = (User.objects.all(),)
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    # API endpoint that allows User to be viewed.
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single User by pk.
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a User record to be updated.
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a User record to be deleted.
    queryset = User.objects.all()
    serializer_class = UserSerializer



class DeviceCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Device
    queryset = (Device.objects.all(),)
    serializer_class = DeviceSerializer


class DeviceList(generics.ListAPIView):
    # API endpoint that allows Device to be viewed.
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Device by pk.
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Device record to be updated.
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Device record to be deleted.
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer