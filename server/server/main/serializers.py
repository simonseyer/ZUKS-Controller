from server.main.models import Volunteer, VolunteerGroup
from rest_framework import serializers


class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volunteer
        depth = 1

class VolunteerGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VolunteerGroup
