from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from server.main import views

router = routers.DefaultRouter()
router.register(r'volunteers', views.VolunteerViewSet)
router.register(r'volunteerGroups', views.VolunteerGroupViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'pois', views.POIViewSet)
router.register(r'poiCategories', views.POICategoryViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
