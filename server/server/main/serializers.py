from server.main.models import *
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    '''Handles Location object serialization'''

    class Meta:
        model = Location

class LocationHandler:
    '''Helper class to handle creation and update of Location objects'''

    def create(data):
        '''Return a new Location object based on the given data.

        Keyword arguments:
        data -- dictionary filled with location data
        '''
        return Location.objects.create(**data)

    def update(location, data):
        '''Updates an existing Location object based on the given data.

        Keyword arguments:
        instance -- an existing Location object
        data -- dictionary filled with location data
        '''
        location.latitude = data.get('latitude', location.latitude)
        location.longitude = data.get('longitude', location.longitude)
        location.save()


class VolunteerSerializer(serializers.ModelSerializer):
    '''Handles Volunteer object serialization'''
    group = serializers.PrimaryKeyRelatedField(queryset=VolunteerGroup.objects.all())
    location = LocationSerializer()
    targetLocation = LocationSerializer(allow_null=True)
    class Meta:
        model = Volunteer
        depth = 1

    def create(self, validated_data):
        location = LocationHandler.create(validated_data.pop('location'))
        targetLocation = LocationHandler.create(validated_data.pop('targetLocation'))
        volunteer = Volunteer.objects.create(location=location, targetLocation=targetLocation, **validated_data)
        return volunteer

    def update(self, instance, validated_data):
        LocationHandler.update(instance.location, validated_data.pop('location'))

        if validated_data['targetLocation']:
            locationData = validated_data.pop('targetLocation')
            if instance.targetLocation:
                LocationHandler.update(instance.targetLocation, locationData)
            else:
                instance.targetLocation = LocationHandler.create(locationData)
        else:
            instance.targetLocation = None

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.group = validated_data.get('group', instance.group)
        instance.save()

        return instance


class VolunteerGroupSerializer(serializers.ModelSerializer):
    '''Handles VolunteerGroup object serialization'''
    class Meta:
        model = VolunteerGroup
        fields = ('name', 'id')

class POICategorySerializer(serializers.ModelSerializer):
    '''Handles POICategory object serialization'''
    class Meta:
        model = POICategory

class POISerializer(serializers.ModelSerializer):
    '''Handles POI object serialization'''
    category = serializers.PrimaryKeyRelatedField(queryset=POICategory.objects.all())
    location = LocationSerializer()
    class Meta:
        model = POI
        depth = 1

    def create(self, validated_data):
        location = LocationHandler.create(validated_data.pop('location'))
        poi = POI.objects.create(location=location, **validated_data)
        return poi

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        LocationHandler.update(instance.location, validated_data.pop('location'))

        return instance
