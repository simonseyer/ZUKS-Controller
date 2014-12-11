import requests
import json
from decimal import Decimal
from django.conf import settings

class WebNotifier:
  ''' Forwards events to web clients over an websocket service

  Listens to all events, that are relevant for web clients and
  forwards to a second server, that handles the connection to
  the clients.
  '''

  WEB_SOCKET_SERVICE_URL = getattr(settings, "WEB_SOCKET_SERVICE_URL", None)

  def __init__(self, event_bus):
    '''Create a new web notifier

    Keyword arguments:
    event_bus -- the event bus to observe
    '''
    event_bus.addHandler('.*', self.handleEvent)

  def handleEvent(self, key, value):
    '''Callback method for the event bus

    Converts the data into a json string sends this 
    string to the websocket server.

    Keyword arguments:
    key   -- the key, that identifies the event
    value -- a value, that is passed to the handler. Has to be serializable to JSON:
    '''
    jsonContent = json.dumps(value, default=WebNotifier.decimal_default)
    requests.post(WebNotifier.WEB_SOCKET_SERVICE_URL, data=jsonContent)

  def decimal_default(obj):
    '''Converter rule for Decimals

    Handles the conversion of decimals to string.
    Is needed for the conversion of decimal into the JSON format.

    Keyword arguments:
    obj -- The object, that should be converted
    '''
    if isinstance(obj, Decimal):
      return str(obj)
    raise TypeError
