from django.contrib import admin

from .models import Book, BookPersonality, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = ('id', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('id', )


@admin.register(BookPersonality)
class BookPersonalityAdmin(admin.ModelAdmin):

    list_display = ('id', )
