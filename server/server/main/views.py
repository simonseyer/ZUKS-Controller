from server.main.models import Volunteer, Location
from rest_framework import viewsets
from server.main.serializers import VolunteerSerializer
from server.main.message_bus import MessageBus, MessageBusLogger

default_message_bus = MessageBus()
logger = MessageBusLogger(default_message_bus)

class VolunteerViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows volunteers to be viewed or edited.
  """
  queryset = Volunteer.objects.all()
  serializer_class = VolunteerSerializer

  def create(self, request):
    result = super().create(request)
    default_message_bus('volunteer.created', result.data)
    return result

  def update(self, request, pk=None):
    result = super().update(request)
    default_message_bus('volunteer.update', result.data)
    return result

  def partial_update(self, request, pk=None):
    result = super().partial_update(request)
    default_message_bus('volunteer.update', result.data)
    return result