import requests
import json
from decimal import Decimal
from django.conf import settings

class WebsocketService:
  '''Interface to reach the websocket service'''

  def send(self, data):
    '''Send data to the websocket service

    Keyword arguments:
    data -- the encoded data that should be sent
    '''
    raise NotImplementedError("Should have implemented this")

class DefaultWebsocketService(WebsocketService):
  '''Default implemention of the websocket service interface

  This implementation send the data via post request to the url
  configured in the settings.py.
  '''

  WEB_SOCKET_SERVICE_URL = getattr(settings, "WEB_SOCKET_SERVICE_URL", None)

  def send(self, data):
    '''Send data to the websocket service

    Keyword arguments:
    data -- the encoded data that should be sent
    '''
    requests.post(DefaultWebsocketService.WEB_SOCKET_SERVICE_URL, data=data)

class WebNotifier:
  ''' Forwards events to web clients over an websocket service

  Listens to all events, that are relevant for web clients and
  forwards to a second server, that handles the connection to
  the clients.
  '''

  def __init__(self, event_bus, websocket_service=DefaultWebsocketService()):
    '''Create a new web notifier

    Keyword arguments:
    event_bus -- the event bus to observe
    websocket_service -- the interface to send messages to the websocket service
    '''
    event_bus.addHandler('.*', self.handleEvent)
    self.websocket_service = websocket_service

  def handleEvent(self, key, value):
    '''Callback method for the event bus

    Converts the data into a json string sends this 
    string to the websocket server.

    Keyword arguments:
    key   -- the key, that identifies the event
    value -- a value, that is passed to the handler. Has to be serializable to JSON:
    '''
    jsonContent = {
      'event' : key,
      'data' : value
    }
    jsonData = json.dumps(jsonContent, default=WebNotifier.decimal_default)
    self.websocket_service.send(jsonData)

  def decimal_default(obj):
    '''Converter rule for Decimals

    Handles the conversion of decimals to string.
    Is needed for the conversion of decimal into the JSON format.

    Keyword arguments:
    obj -- The object, that should be converted
    '''
    if isinstance(obj, Decimal):
      return float(obj)
    raise TypeError
