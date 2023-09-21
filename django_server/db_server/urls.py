from django.urls import include, path
from .views import UserCreate, UserList, UserDetail, UserUpdate, UserDelete,DeviceCreate,DeviceList,DeviceDetail,DeviceUpdate,DeviceDelete


urlpatterns = [
    path("create/", UserCreate.as_view(), name="create-User"),
    path("", UserList.as_view()),
    path("<str:pk>/", UserDetail.as_view(), name="retrieve-User"),
    path("update/<str:pk>/", UserUpdate.as_view(), name="update-User"),
    path("delete/<str:pk>/", UserDelete.as_view(), name="delete-User"),

    path("create/", DeviceCreate.as_view(), name="create-Device"),
    path("", DeviceList.as_view()),
    path("<str:pk>/", DeviceDetail.as_view(), name="retrieve-Device"),
    path("update/<str:pk>/", DeviceUpdate.as_view(), name="update-Device"),
    path("delete/<str:pk>/", DeviceDelete.as_view(), name="delete-Device"),
]
