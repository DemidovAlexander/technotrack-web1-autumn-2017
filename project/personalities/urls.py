from django.conf.urls import url

from .views import personalities, personality


urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', personalities),
    url(r'^items/(?P<post_id>\d+)/$', personality),
]
