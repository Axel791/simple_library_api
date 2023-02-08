from django.contrib import admin
from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ['last_action', 'created_at', 'user_status']
    list_display = [
        'id',
        'full_name',
        'user_status',
        'address',
        'created_at',
        'last_action'
    ]

    @admin.display(description="full_name")
    def full_name(self, obj):
        if (obj.user.first_name is None) or (obj.user.last_name is None):
            return "%s" % obj.user.username
        return "%s %s" % (obj.user.first_name, obj.user.last_name)
