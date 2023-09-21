from django.shortcuts import render
from .models import User, Register, Device
from rest_framework import generics
from .serializers import UserSerializer, RegisterSerializer, DeviceSerializer


class UserCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new User
    queryset = User.objects.all(),
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



