from django.db import models
from core.models import User


class Blog(models.Model):

    user = models.ForeignKey(User)

    title = models.CharField(max_length=255, default='')
    about_user = models.TextField(default='')


class Comment(models.Model):

    post = models.ForeignKey(Blog)
