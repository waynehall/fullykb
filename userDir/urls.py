from django.conf.urls import url
from userDir.views import user_login, update_profile
from django.contrib.auth import urls
from django.conf.urls import url, include

urlpatterns = [
    url('^accounts/', include('django.contrib.auth.urls')),
    url('^profile', update_profile)
]