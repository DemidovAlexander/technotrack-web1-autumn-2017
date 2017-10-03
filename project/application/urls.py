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

from core.views import index
from core.views import profile
from core.views import user

from core.views import personalities
from core.views import personality

from core.views import music
from core.views import music_personality
from core.views import music_item

from core.views import movies
from core.views import movies_personality
from core.views import movies_item

from core.views import books
from core.views import books_personality
from core.views import books_item

from core.views import paintings
from core.views import paintings_personality
from core.views import paintings_item

from core.views import references
from core.views import reference


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^profile/$', profile),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/$', user),

    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/personalities/$', personalities),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/personalities/(?P<post_id>\d+)/$', personality),

    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/music/$', music),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/music/personalities/(?P<post_id>\d+)/$', music_personality),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/music/items/(?P<post_id>\d+)/$', music_item),

    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/movies/$', movies),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/movies/personalities/(?P<post_id>\d+)/$', movies_personality),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/movies/items/(?P<post_id>\d+)/$', movies_item),

    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/books/$', books),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/books/personalities/(?P<post_id>\d+)/$', books_personality),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/books/items/(?P<post_id>\d+)/$', books_item),

    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/paintings/$', paintings),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/paintings/personalities/(?P<post_id>\d+)/$', paintings_personality),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/paintings/items/(?P<post_id>\d+)/$', paintings_item),

    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/references/$', references),
    url(r'^(?P<user>([a-zA-Z][a-zA-Z0-9-_\.]{1,20}))/references/(?P<post_id>\d+)/$', reference),
]
