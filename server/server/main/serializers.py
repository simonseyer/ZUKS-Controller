# This file is part of ZUKS-Controller.
#
# ZUKS-Controller is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ZUKS-Controller is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ZUKS-Controller. If not, see <http://www.gnu.org/licenses/>.

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
        targetLocationData = validated_data.pop('targetLocation')
        if targetLocationData:
            targetLocation = LocationHandler.create()
        else:
            targetLocation = None
        volunteer = Volunteer.objects.create(location=location, targetLocation=targetLocation, **validated_data)
        return volunteer

    def update(self, instance, validated_data):
        LocationHandler.update(instance.location, validated_data.pop('location'))

        if validated_data['targetLocation']:
            locationData = validated_data.pop('targetLocation')
            if instance.targetLocation:
                LocationHandler.update(instance.targetLocation, locationData)
                instruction = LocationInstruction(location=instance.targetLocation, receiver=instance);
                instruction.save()
                instance.lastInstruction = instruction
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

class MessageInstructionSerializer(serializers.ModelSerializer):
    '''Handles MessageInstruction object serialization'''
    receiver = serializers.PrimaryKeyRelatedField(queryset=Volunteer.objects.all())
    class Meta:
        model = MessageInstruction
