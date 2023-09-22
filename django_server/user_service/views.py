from django.shortcuts import render
from rest_framework import generics
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, Register, Device
from .serializers import UserSerializer, RegisterSerializer, DeviceSerializer


# class UserCreate(generics.CreateAPIView):
#     # API endpoint that allows creation of a new User
#     queryset = (User.objects.all(),)
#     serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            users = []
            for user_data in request.data:
                serializer = self.get_serializer(data=user_data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                users.append(serializer.data)
            return Response(users, status=status.HTTP_201_CREATED)
        else:
            return super().create(request, *args, **kwargs)

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


class RegisterCreate(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            Registers = []
            for Register_data in request.data:
                serializer = self.get_serializer(data=Register_data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                Registers.append(serializer.data)
            return Response(Registers, status=status.HTTP_201_CREATED)
        else:
            return super().create(request, *args, **kwargs)

class RegisterList(generics.ListAPIView):
    # API endpoint that allows Register to be viewed.
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class RegisterDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Register by pk.
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class RegisterUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Register record to be updated.
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class RegisterDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Register record to be deleted.
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class DeviceCreate(generics.CreateAPIView):
    serializer_class = DeviceSerializer
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            Devices = []
            for Device_data in request.data:
                serializer = self.get_serializer(data=Device_data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                Devices.append(serializer.data)
            return Response(Devices, status=status.HTTP_201_CREATED)
        else:
            return super().create(request, *args, **kwargs)


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
