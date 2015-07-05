# This file is part of ZUKS-Controller.
#
# ZUKS-Controller is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ZUKS-Controller is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ZUKS-Controller. If not, see <http://www.gnu.org/licenses/>.

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
