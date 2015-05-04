from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers
from server.main import views

router = routers.DefaultRouter()
router.register(r'volunteers', views.VolunteerViewSet)
router.register(r'volunteerGroups', views.VolunteerGroupViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'pois', views.POIViewSet)
router.register(r'poiCategories', views.POICategoryViewSet)
router.register(r'messageInstructions', views.MessageInstructionViewSet)

urlpatterns = patterns('',
    url(r'%s^' % (settings.SUB_SITE,), include(router.urls)),
    url(r'^%sapi-auth/' % (settings.SUB_SITE,), include('rest_framework.urls', namespace='rest_framework')),
    url(r'^%sadmin/' % (settings.SUB_SITE,), include(admin.site.urls)),
)
