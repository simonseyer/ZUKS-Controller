from server.main.models import Volunteer, Location
from rest_framework import viewsets
from server.main.serializers import VolunteerSerializer

class VolunteerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows volunteers to be viewed or edited.
    """
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
