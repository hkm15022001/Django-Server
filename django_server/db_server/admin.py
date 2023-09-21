from django.contrib import admin


from .models import User, Register, Device
class UserAdmin(admin.ModelAdmin): # cấu hình form admin
    fieldsets = [
        (None, {"fields": ["user_id"]}),
        ("Date information", {"fields": ["username"]}),
    ]


admin.site.register(User)
