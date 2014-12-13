from django.db import models

class Location(models.Model):
  latitude = models.DecimalField(decimal_places=18, max_digits=20)
  longitude = models.DecimalField(decimal_places=18, max_digits=20)

class Volunteer(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  location = models.OneToOneField(Location)

  def __unicode__(self):
    return u"%s %s" % (self.first_name, self.last_name)