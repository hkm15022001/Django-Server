from django.apps import AppConfig
from .signal import startup_signal

class DbServerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "db_server"
    def ready(self):
        # Gửi signal khi ứng dụng khởi động
        startup_signal.send(sender=self)