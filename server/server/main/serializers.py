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

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        location = instance.location

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.group = validated_data.get('group', instance.group)
        instance.save()

        location.latitude = location_data.get('latitude', location.latitude)
        location.longitude = location_data.get('longitude', location.longitude)
        location.save()

        return instance


class VolunteerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerGroup
        fields = ('name', 'id')
