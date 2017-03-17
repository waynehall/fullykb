from django.conf.urls import url
from kb import views
import os
from django.contrib import admin

urlpatterns = [
    url(r'^kb/$', views.index),
]