from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from server.main import views

router = routers.DefaultRouter()
router.register(r'volunteers', views.VolunteerViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
