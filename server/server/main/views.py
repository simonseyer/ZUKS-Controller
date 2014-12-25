from server.main.models import Volunteer, VolunteerGroup, Location
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from server.main.serializers import VolunteerSerializer, VolunteerGroupSerializer
from server.main.event_bus import EventBus, EventBusLogger
from server.main.web_notifier import WebNotifier

default_event_bus = EventBus()
logger = EventBusLogger(default_event_bus)
web_notifier = WebNotifier(default_event_bus)

class EventViewSet(viewsets.ModelViewSet):
  '''
  ModelViewSet that fires events, when the model
  is changed. 

  The events are published to the global 
  default_event_bus.
  '''

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    self.fire_response('create', response)
    return response

  def update(self, request, *args, **kwargs):
    response = super().update(request, *args, **kwargs)
    self.fire_response('update', response)
    return response

  def destroy(self, request, *args, **kwargs):
    response = super().destroy(request, *args, **kwargs)
    self.fire_response('delete', response)
    return response

  def fire_response(self, event, response):
    '''
    Creates a new event and publishes that event
    to the global default_event_bus.

    As prefix for the event name the class variable
    event_key is used.

    Keyword arguments:
    event -- the event name, used to create the event_key
    response -- the reponse object
    '''
    if status.is_success(response.status_code):
      key = "%s_%s" % (self.__class__.event_key, event)
      default_event_bus(key, response.data)

class VolunteerViewSet(EventViewSet):
  """
  API endpoint for volunteers
  """
  queryset = Volunteer.objects.all()
  serializer_class = VolunteerSerializer
  event_key = "volunteer"

class VolunteerGroupViewSet(EventViewSet):
  """
  API endpoint for volunteer groups
  """
  queryset = VolunteerGroup.objects.all()
  serializer_class = VolunteerGroupSerializer
  event_key = "volunteerGroup"

  @detail_route()
  def members(self, request, pk=None):
    volunteers = self.get_object().members.all()
    serializer = VolunteerSerializer(volunteers, many=True)
    return Response(serializer.data)
