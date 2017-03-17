from django.conf.urls import url
from medals import views
import os
from django.contrib import admin

urlpatterns = [
    url(r'^medals/$', views.FullyUser_list),
    url(r'^medals/(?P<pk>[0-9]+)/$', views.FullyUser_detail),
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]