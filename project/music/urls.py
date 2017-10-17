from django.conf.urls import url

from .views import music, music_personality, music_item


urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', music),
    url(r'^personalities/(?P<post_id>\d+)/$', music_personality),
    url(r'^items/(?P<post_id>\d+)/$', music_item),
]
