from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    about_user = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.id


class AbstractPost(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    is_pinned = models.BooleanField(default=False)

    text = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.id


class AbstractPersonalityPost(AbstractPost):

    fullname = models.CharField(max_length=255, verbose_name='Полное имя')

    def __str__(self):
        return self.fullname


class AbstractCategory(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название категории')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
