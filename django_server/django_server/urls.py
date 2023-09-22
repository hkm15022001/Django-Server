from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("db_service/", include("db_service.urls")),
    path("user_service/", include("user_service.urls"))
]
