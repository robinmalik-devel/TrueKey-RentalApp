from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("phone", "name", "role", "status", "trust_level", "is_staff", "created_at")
    list_filter = ("role", "status", "is_staff")
    search_fields = ("phone", "name")
    readonly_fields = ("created_at", "updated_at", "last_login")
    exclude = ("password",)