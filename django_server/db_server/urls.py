from django.urls import include, path
from .views import *


urlpatterns = [
    path("user/create/", UserCreate.as_view(), name="create-User"),
    path("user", UserList.as_view()),
    path("user/<str:pk>/", UserDetail.as_view(), name="retrieve-User"),
    path("user/update/<str:pk>/", UserUpdate.as_view(), name="update-User"),
    path("user/delete/<str:pk>/", UserDelete.as_view(), name="delete-User"),

    path("device/create/", DeviceCreate.as_view(), name="create-Device"),
    path("device", DeviceList.as_view()),
    path("device/<str:pk>/", DeviceDetail.as_view(), name="retrieve-Device"),
    path("device/update/<str:pk>/", DeviceUpdate.as_view(), name="update-Device"),
    path("device/delete/<str:pk>/", DeviceDelete.as_view(), name="delete-Device"),

    path("msg/create/", TrackAndTraceCreate.as_view(), name="create-msg"),
    path("msg", TrackAndTraceList.as_view()),
    path("msg/<str:pk>/", TrackAndTraceDetail.as_view(), name="retrieve-msg"),
    path("msg/update/<str:pk>/", TrackAndTraceUpdate.as_view(), name="update-msg"),
    path("msg/delete/<str:pk>/", TrackAndTraceDelete.as_view(), name="delete-msg"),
]
