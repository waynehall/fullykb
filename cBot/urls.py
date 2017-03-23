from django.conf.urls import url, include
from rest_framework import routers
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from cBot import settings
# router = routers.DefaultRouter()
"""
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'fullyusers', views.FullyUserViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
"""
urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('medals.urls')),
    url(r'^', include('kb.urls')),
    url(r'^', include('userDir.urls')),
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)