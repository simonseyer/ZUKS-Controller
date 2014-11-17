from django.db import models

class Location(models.Model):
  latitude = models.DecimalField(decimal_places=8, max_digits=11, required=True)
  longitude = models.DecimalField(decimal_places=8, max_digits=11, required=True)

class Volunteer(models.Model):
  first_name = models.CharField(max_length=30, required=True)
  last_name = models.CharField(max_length=30, required=True)
  location = models.OneToOneField(Location, required=True)

