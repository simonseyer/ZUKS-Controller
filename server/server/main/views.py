from server.main.models import Volunteer, Location
from rest_framework import viewsets, status
from server.main.serializers import VolunteerSerializer
from server.main.event_bus import EventBus, EventBusLogger
from server.main.web_notifier import WebNotifier

default_event_bus = EventBus()
logger = EventBusLogger(default_event_bus)
web_notifier = WebNotifier(default_event_bus)

class VolunteerViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows volunteers to be viewed or edited.
  """
  queryset = Volunteer.objects.all()
  serializer_class = VolunteerSerializer

  def create(self, request):
    result = super().create(request)
    if status.is_success(result.status_code):
      default_event_bus('volunteer_create', result.data)
    return result

  def update(self, request, pk=None):
    result = super().update(request)
    if status.is_success(result.status_code):
      default_event_bus('volunteer_update', result.data)
    return result

  def partial_update(self, request, pk=None):
    result = super().partial_update(request)
    if status.is_success(result.status_code):
      default_event_bus('volunteer_update', result.data)
    return result
