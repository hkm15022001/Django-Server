from django.urls import include, path
from .views import UserCreate, UserList, UserDetail, UserUpdate, UserDelete


urlpatterns = [
    path("create/", UserCreate.as_view(), name="create-User"),
    path("", UserList.as_view()),
    path("<str:pk>/", UserDetail.as_view(), name="retrieve-User"),
    path("update/<str:pk>/", UserUpdate.as_view(), name="update-User"),
    path("delete/<str:pk>/", UserDelete.as_view(), name="delete-User"),
]
