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
    url(r'^index/$', index),
    url(r'^profile/$', profile),
    url(r'^user/(?P<user>\d+)/$', user),

    url(r'^user/(?P<user>\d+)/personalities/$', personalities),
    url(r'^user/(?P<user>\d+)/personalities/(?P<post_id>\d+)/$', personality),

    url(r'^user/(?P<user>\d+)/music/$', music),
    url(r'^user/(?P<user>\d+)/music/personalities/(?P<post_id>\d+)/$', music_personality),
    url(r'^user/(?P<user>\d+)/music/items/(?P<post_id>\d+)/$', music_item),

    url(r'^user/(?P<user>\d+)/movies/$', movies),
    url(r'^user/(?P<user>\d+)/movies/personalities/(?P<post_id>\d+)/$', movies_personality),
    url(r'^user/(?P<user>\d+)/movies/items/(?P<post_id>\d+)/$', movies_item),

    url(r'^user/(?P<user>\d+)/books/$', books),
    url(r'^user/(?P<user>\d+)/books/personalities/(?P<post_id>\d+)/$', books_personality),
    url(r'^user/(?P<user>\d+)/books/items/(?P<post_id>\d+)/$', books_item),

    url(r'^user/(?P<user>\d+)/paintings/$', paintings),
    url(r'^user/(?P<user>\d+)/paintings/personalities/(?P<post_id>\d+)/$', paintings_personality),
    url(r'^user/(?P<user>\d+)/paintings/items/(?P<post_id>\d+)/$', paintings_item),

    url(r'^user/(?P<user>\d+)/references/$', references),
    url(r'^user/(?P<user>\d+)/references/(?P<post_id>\d+)/$', reference),
]
