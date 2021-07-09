from django.contrib import admin

from .models import UserFeedItem, UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    """
    Class to create custom admin options for class `UserProfile`.
    """
    list_per_page = 10
    list_display = ("email", "name", "is_active", "is_superuser")
    list_editable = ("is_active", "is_superuser")
    search_fields = ["name", "email"]


class UserFeedAdmin(admin.ModelAdmin):
    """
    Class to create custom admin options for class `UserProfile`.
    """
    list_per_page = 10
    list_display = ("user_profile", "status_text", "created_on")
    list_editable = ("status_text",)
    search_fields = ["user_profile"]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserFeedItem, UserFeedAdmin)
