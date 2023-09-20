from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["email", "full_name", "is_active"]
    list_filter = ["is_staff"]
    fieldsets = [(None, {"fields": ["email", "password", "first_name", "last_name"]}),
                 ("Permissions", {"fields": ['is_active', 'groups']}), ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "last_name", "password1", "password2"],
            },
        ),
        (
            "Permissions",
            {
                "fields": ["is_active", "groups"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ['groups']


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
