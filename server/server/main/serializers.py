from server.main.models import Volunteer
from rest_framework import serializers


class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volunteer
        depth = 1