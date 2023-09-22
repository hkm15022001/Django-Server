from django.shortcuts import render
from rest_framework import generics
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Register, Device
from .serializers import UserSerializer, RegisterSerializer, DeviceSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserLogin(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Đăng nhập không thành công.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    # API endpoint that allows User to be viewed.
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single User by pk.
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterList(generics.ListAPIView):
    # API endpoint that allows Register to be viewed.
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class RegisterDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Register by pk.
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class DeviceList(generics.ListAPIView):
    # API endpoint that allows Device to be viewed.
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Device by pk.
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
