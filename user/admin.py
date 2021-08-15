from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from user import models


class UserAdminCustom(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('name', 'gender', 'address', 'card_id', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'password1', 'password2'),
        }),
    )
    list_display = ('name', 'phone')
    list_per_page = 10
    list_filter = ('gender', )
    search_fields = ('name', 'phone', 'card_id')
    ordering = ('name',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(models.User, UserAdminCustom)
