from django.db import models

from core.models import AbstractPost, AbstractPersonalityPost, AbstractCategory


class Genre(AbstractCategory):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(AbstractPost):

    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор')
    year = models.DateField(verbose_name='Время написания')

    status = models.SmallIntegerField(choices=((1, 'reading'), (2, 'have read'), (3, 'going to reread')))

    genres = models.ManyToManyField(Genre, related_name='books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return '{} {} (user {})'.format(self.title, self.author, self.user.id)


class BookPersonality(AbstractPersonalityPost):

    genres = models.ManyToManyField(Genre, related_name='book_personalities')
    books = models.ManyToManyField(Book, related_name='personalities')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
