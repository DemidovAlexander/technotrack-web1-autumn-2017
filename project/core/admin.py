# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, AbstractPost, AbstractPersonalityPost, AbstractCategory


class UserAdmin(BaseUserAdmin):

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('admin_avatar', 'avatar')}),
    )
    readonly_fields = ('admin_avatar', )

    def admin_avatar(self, instance):
        return instance.avatar and '<img src="{0}" width="100px" />'.format(
            instance.avatar.url
        )
    admin_avatar.allow_tags = True
    admin_avatar.short_description = 'Аватар'


admin.site.register(User, UserAdmin)


@admin.register(AbstractPost)
class AbstractPostAdmin(admin.ModelAdmin):

    list_display = ('id', )


@admin.register(AbstractPersonalityPost)
class AbstractPersonalityPostAdmin(admin.ModelAdmin):

    list_display = ('id', )


@admin.register(AbstractCategory)
class AbstractCategoryAdmin(admin.ModelAdmin):

    list_display = ('id', )
