from django.conf.urls import url

from .views import index, profile, user


urlpatterns = [
    url(r'^$', index),
    url(r'^profile/$', profile),
    url(r'^(?P<user_name>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/$', User.as_view(), name="blog_list"),
]
