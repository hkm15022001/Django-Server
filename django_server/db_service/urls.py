from django.urls import include, path
from .views import *


urlpatterns = [
    path("msg/create/", TrackAndTraceCreate.as_view(), name="create-msg"),
    path("msg", TrackAndTraceList.as_view()),
    path("msg/<str:device_id>", TrackAndTraceDetailList.as_view(), name="retrieve-msg"),
    path("msg/update/<str:device_id>", TrackAndTraceUpdate.as_view(), name="update-msg"),
    path("msg/delete/<str:device_id>", TrackAndTraceDelete.as_view(), name="delete-msg"),
]
