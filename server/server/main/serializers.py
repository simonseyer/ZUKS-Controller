from server.main.models import Volunteer, Location, VolunteerGroup
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

class VolunteerSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=VolunteerGroup.objects.all())
    class Meta:
        model = Volunteer
        depth = 1

class VolunteerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerGroup
        fields = ('name', 'id', 'members')
