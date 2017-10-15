"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from core.views import index, profile, user, personalities, personality, music, music_personality,\
    music_item, movies, movies_personality, movies_item, books, books_personality, books_item,\
    paintings, paintings_personality, paintings_item, references, reference


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index),
    url(r'^profile/$', profile),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/$', user),

    url(r'^personalities/(?P<list_id>\d+)/$', personalities),
    url(r'^personalities/items/(?P<post_id>\d+)/$', personality),

    url(r'^music/(?P<list_id>\d+)/$', music),
    url(r'^music/personalities/(?P<post_id>\d+)/$', music_personality),
    url(r'^music/items/(?P<post_id>\d+)/$', music_item),

    url(r'^movies/(?P<list_id>\d+)/$', movies),
    url(r'^movies/personalities/(?P<post_id>\d+)/$', movies_personality),
    url(r'^movies/items/(?P<post_id>\d+)/$', movies_item),

    url(r'^books/(?P<list_id>\d+)/$', books),
    url(r'^books/personalities/(?P<post_id>\d+)/$', books_personality),
    url(r'^books/items/(?P<post_id>\d+)/$', books_item),

    url(r'^paintings/(?P<list_id>\d+)/$', paintings),
    url(r'^paintings/personalities/(?P<post_id>\d+)/$', paintings_personality),
    url(r'^paintings/items/(?P<post_id>\d+)/$', paintings_item),

    url(r'^references/(?P<list_id>\d+)/$', references),
    url(r'^references/items/(?P<post_id>\d+)/$', reference),
]
