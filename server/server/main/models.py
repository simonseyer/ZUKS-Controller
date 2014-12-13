from django.db import models

class VolunteerGroup(models.Model):
  name = models.CharField(max_length=30)

  def __unicode__(self):
    return self.name

class Location(models.Model):
  latitude = models.DecimalField(decimal_places=18, max_digits=20)
  longitude = models.DecimalField(decimal_places=18, max_digits=20)

class Volunteer(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  location = models.OneToOneField(Location)
  group = models.ForeignKey(VolunteerGroup, null=True, related_name='member')

  def __unicode__(self):
    return u"%s %s" % (self.first_name, self.last_name)