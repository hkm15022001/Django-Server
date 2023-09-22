from django.shortcuts import render
from .models import User, Register, Device, TrackAndTrace
from rest_framework import generics
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, DeviceSerializer, TrackAndTraceSerializer

class UserCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new User
    queryset = (User.objects.all(),)
    serializer_class = UserSerializer

class UserCreateMany(generics.CreateAPIView):
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        # Check if the request data is a list
        if isinstance(request.data, list):
            users = []
            for user_data in request.data:
                serializer = self.get_serializer(data=user_data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                users.append(serializer.data)
            return Response(users, status=status.HTTP_201_CREATED)
        else:
            # If the request data is not a list, proceed with single user creation
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


# class TrackAndTraceCreate(generics.CreateAPIView):
#     queryset = (TrackAndTrace.objects.all(),)
#     serializer_class = TrackAndTraceSerializer


class TrackAndTraceCreate(generics.CreateAPIView):
    serializer_class = TrackAndTraceSerializer
    def create(self, request, *args, **kwargs):
        # Check if the request data is a list
        if isinstance(request.data, list):
            messages = []
            for message_data in request.data:
                serializer = self.get_serializer(data=message_data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                messages.append(serializer.data)
            return Response(messages, status=status.HTTP_201_CREATED)
        else:
            # If the request data is not a list, proceed with single user creation
            return super().create(request, *args, **kwargs)

class TrackAndTraceList(generics.ListAPIView):
    # API endpoint that allows TrackAndTrace to be viewed.
    queryset = TrackAndTrace.objects.all()
    serializer_class = TrackAndTraceSerializer


class TrackAndTraceDetailList(generics.ListAPIView):
    serializer_class = TrackAndTraceSerializer
    lookup_field = 'device_id'
    def get_queryset(self):
        queryset = TrackAndTrace.objects.all()
        queryset = queryset.order_by('-id')
        valid_field_names = [field.name for field in TrackAndTrace._meta.get_fields()]
        # Loop through all URL parameters and filter the queryset
        for param, value in self.request.query_params.items():
            if param != 'limit' and param in valid_field_names:
                queryset = queryset.filter(**{param: value})
        limit = int(self.request.query_params.get('limit', 20)) #default to 20
        total_objects = queryset.count()
        if limit > total_objects:
            limit = total_objects
        return queryset[:limit]


class TrackAndTraceUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a TrackAndTrace record to be updated.
    queryset = TrackAndTrace.objects.all()
    serializer_class = TrackAndTraceSerializer

class TrackAndTraceDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a TrackAndTrace record to be deleted.
    queryset = TrackAndTrace.objects.all()
    serializer_class = TrackAndTraceSerializer
