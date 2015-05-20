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
