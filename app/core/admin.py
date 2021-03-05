from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User, \
                        InstagramAccount, \
                        InstagramMedia, \
                        InstagramComment, \
                        InstagramMediaTag, \
                        InstagramMediaLocation


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Personal info', {'fields': ('instagram_account',)}),
        ('important dates', {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'instagram_account')
        }),
    )


class InstagramAccountAdmin(admin.ModelAdmin):
    fields = (
        'id', 'counts_followed_by', 'profile_picture_url',
        'counts_media', 'counts_follow', 'user'
    )
    list_display = (
        'id', 'counts_followed_by', 'profile_picture_url',
        'counts_media', 'counts_follow', 'user'
    )
    readonly_fields = (
        'id', 'counts_followed_by', 'profile_picture_url',
        'counts_media', 'counts_follow'
    )


class InstagramMediaAdmin(admin.ModelAdmin):
    fields = (
        'id', 'created_time', 'link_to_media',
        'comments_count', 'media_type', 'links_count',
        'user'
    )
    list_display = (
        'id', 'created_time', 'link_to_media',
        'comments_count', 'media_type', 'links_count',
        'user'
    )
    readonly_fields = (
        'id', 'created_time', 'link_to_media',
        'comments_count', 'media_type', 'links_count'
    )


class InstagramCommentAdmin(admin.ModelAdmin):
    fields = (
        'id', 'from_username', 'comment',
        'created_time', 'media'
    )
    list_display = (
        'id', 'from_username', 'comment',
        'created_time', 'media'
    )
    readonly_fields = (
        'id', 'from_username', 'comment',
        'created_time', 'media'
    )


admin.site.register(User, UserAdmin)
admin.site.register(InstagramAccount, InstagramAccountAdmin)
admin.site.register(InstagramMedia, InstagramMediaAdmin)
admin.site.register(InstagramComment, InstagramCommentAdmin)
