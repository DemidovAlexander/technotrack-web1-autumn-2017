from django.db import models
from application import settings


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('core.AbstractPost', related_name='comments')

    text = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
