from django.urls import include, path
from .views import *


urlpatterns = [
    path('login', UserLogin.as_view(), name='login-User'),

    path("user", UserList.as_view()),
    path("user/<str:pk>", UserDetail.as_view(), name="retrieve-User"),

    path("register", RegisterList.as_view()),
    path("register/<str:pk>", RegisterDetail.as_view(), name="retrieve-Register"),


    path("device", DeviceList.as_view()),
    path("device/<str:pk>", DeviceDetail.as_view(), name="retrieve-Device"),
]
