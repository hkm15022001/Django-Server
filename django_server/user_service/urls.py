from django.urls import include, path
from .views import *


urlpatterns = [
    path("user/create", UserCreate.as_view(), name="create-User"),
    path("user", UserList.as_view()),
    path("user/<str:pk>", UserDetail.as_view(), name="retrieve-User"),
    path("user/update/<str:pk>", UserUpdate.as_view(), name="update-User"),
    path("user/delete/<str:pk>", UserDelete.as_view(), name="delete-User"),

    path("register/create", RegisterCreate.as_view(), name="create-Register"),
    path("register", RegisterList.as_view()),
    path("register/<str:pk>", RegisterDetail.as_view(), name="retrieve-Register"),
    path("register/update/<str:pk>", RegisterUpdate.as_view(), name="update-Register"),
    path("register/delete/<str:pk>", RegisterDelete.as_view(), name="delete-Register"),

    path("device/create", DeviceCreate.as_view(), name="create-Device"),
    path("device", DeviceList.as_view()),
    path("device/<str:pk>", DeviceDetail.as_view(), name="retrieve-Device"),
    path("device/update/<str:pk>", DeviceUpdate.as_view(), name="update-Device"),
    path("device/delete/<str:pk>", DeviceDelete.as_view(), name="delete-Device"),
]
