from django.db import models

class VolunteerGroup(models.Model):
  name = models.CharField(max_length=30)

  class Meta:
    ordering = ['name']

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
  location = models.ForeignKey(Location)
  targetLocation = models.ForeignKey(Location, blank=True, null=True, related_name='target')
  group = models.ForeignKey(VolunteerGroup, null=True, related_name='members')

  class Meta:
    ordering = ['first_name', 'last_name']
    unique_together = ("first_name", "last_name")

  def __str__(self):
    return "%s %s" % (self.first_name, self.last_name)

class POICategory(models.Model):
  name = models.CharField(max_length=60)
  icon = models.CharField(max_length=20)

  class Meta:
    ordering = ['name']
    verbose_name = "Point of interest category"
    verbose_name_plural = "Point of interest categories"

  def __str__(self):
    return  self.name

class POI(models.Model):
  name = models.CharField(max_length=60)
  description = models.TextField()
  location = models.ForeignKey(Location)
  address = models.TextField()
  category = models.ForeignKey(POICategory)

  class Meta:
    ordering = ['category', 'name']
    verbose_name = "Point of interest"
    verbose_name_plural = "Points of interest"

  def __str__(self):
    return "%s [%s]" % (self.name, self.category.name)

class Instruction(models.Model):
  receiver = models.ForeignKey(Volunteer)

  class Meta:
    abstract = True

class LocationInstruction(Instruction):
  location = models.ForeignKey(Location)

  def __str__(self):
    return "Go to: %s [%s]" % (self.location, self.receiver)

class MessageInstruction(Instruction):
  subject = models.CharField(max_length=100)
  content = models.TextField()

  def __str__(self):
    return "%s [%s]" % (self.content, self.receiver)
