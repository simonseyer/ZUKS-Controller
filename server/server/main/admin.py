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

from django.contrib import admin
from server.main.models import *

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    pass

@admin.register(VolunteerGroup)
class VolunteerGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(POICategory)
class POICategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(POI)
class POIAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
