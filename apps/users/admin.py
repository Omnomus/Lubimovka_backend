from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group

from ..content_pages.models import Text
from .forms import GroupAdminForm, TextAdminForm, UserAdminForm

User = get_user_model()


class UserAdmin(DjangoUserAdmin):
    form = UserAdminForm
    list_display = (
        "id",
        "username",
        "is_active",
        "role",
    )
    list_filter = ["email", "username"]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ["is_superuser"]
        return super().get_readonly_fields(request, obj)

    def role(self, obj):
        return obj.groups.first()

    role.short_description = "Роль"


class GroupAdmin(admin.ModelAdmin):

    form = GroupAdminForm
    list_display = ["name"]
    filter_horizontal = ("permissions",)


class TextAdmin(admin.ModelAdmin):

    form = TextAdminForm


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Text, TextAdmin)
