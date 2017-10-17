from django.conf.urls import url

from .views import books, books_personality, books_item


urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', books),
    url(r'^personalities/(?P<post_id>\d+)/$', books_personality),
    url(r'^items/(?P<post_id>\d+)/$', books_item),
]
