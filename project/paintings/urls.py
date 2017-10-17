from django.conf.urls import url

from .views import paintings, paintings_personality, paintings_item


urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', paintings),
    url(r'^personalities/(?P<post_id>\d+)/$', paintings_personality),
    url(r'^items/(?P<post_id>\d+)/$', paintings_item),
]
