from django.conf.urls import url

from .views import references, reference


urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', references),
    url(r'^items/(?P<post_id>\d+)/$', reference),
]
