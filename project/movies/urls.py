from django.conf.urls import url

from .views import movies, movies_personality, movies_item


urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', movies),
    url(r'^personalities/(?P<post_id>\d+)/$', movies_personality),
    url(r'^items/(?P<post_id>\d+)/$', movies_item),
]
