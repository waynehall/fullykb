from django.conf.urls import url
from kb import views
import os
from django.contrib import admin
from cBot import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^kb/$', views.index),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)