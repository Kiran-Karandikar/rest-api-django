from django.contrib import admin

from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    """
    Class to create custom admin options for class `UserProfile`.
    """
    list_per_page = 10
    list_display = ("email", "name", "is_active", "is_superuser")
    list_editable = ("is_active", "is_superuser")
    search_fields = ["name", "email"]


admin.site.register(UserProfile, UserProfileAdmin)
