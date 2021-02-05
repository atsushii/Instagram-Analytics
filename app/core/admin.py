from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('important dates'), {'fileds': ('last_login',)}
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',)
            'fields'L('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
