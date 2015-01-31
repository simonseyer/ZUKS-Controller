from django.db import models

class VolunteerGroup(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Location(models.Model):
  latitude = models.DecimalField(decimal_places=18, max_digits=20)
  longitude = models.DecimalField(decimal_places=18, max_digits=20)

  def __str__(self):
    return "%f %f" % (self.latitude, self.longitude)

class Volunteer(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  location = models.OneToOneField(Location)
  group = models.ForeignKey(VolunteerGroup, null=True, related_name='members')

  def __str__(self):
    return "%s %s" % (self.first_name, self.last_name)

class POICategory(models.Model):
  name = models.CharField(max_length=60)
  icon = models.CharField(max_length=20)

  def __str__(self):
    return  self.name

class POI(models.Model):
  name = models.CharField(max_length=60)
  description = models.TextField()
  location = models.OneToOneField(Location)
  address = models.TextField()
  category = models.ForeignKey(POICategory)

  def __str__(self):
    return "%s [%s]" % (self.name, self.category.name)