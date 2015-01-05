from server.main.models import Volunteer, Location, VolunteerGroup
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

class VolunteerSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=VolunteerGroup.objects.all())
    location = LocationSerializer()
    class Meta:
        model = Volunteer
        depth = 1

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        volunteer = Volunteer.objects.create(location=location, **validated_data)
        return volunteer

class VolunteerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerGroup
        fields = ('name', 'id', 'members')
