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

from django.test import TestCase

from server.main.event_bus import EventBus
from server.main.web_notifier import WebsocketService, WebNotifier

import json
from decimal import Decimal

class EventBusTestCase(TestCase):
  def setUp(self):
    self.event_bus = EventBus(False)
    self.eventKey = None
    self.eventObject = None

  def test_simple_key(self):
    self.event_bus.addHandler('test', self.simple_key_handler)

    self.event_bus('test', None)

    self.assertEqual(self.eventKey, 'test')

  def simple_key_handler(self, key, value):
    self.eventKey = key
    self.eventObject = value

  def test_regex_key(self):
    self.event_bus.addHandler('test_.*', self.simple_key_handler)

    self.event_bus('test_fu', None)

    self.assertEqual(self.eventKey, 'test_fu')

  def test_value_parameter(self):
    self.event_bus.addHandler('test', self.simple_key_handler)

    self.event_bus('test', self)

    self.assertEqual(self.eventObject, self)

  def test_remove_handler(self):
    self.event_bus.addHandler('test', self.simple_key_handler)
    self.event_bus.removeHandler('test', self.simple_key_handler)

    self.event_bus('test', None)

    self.assertEqual(self.eventKey, None)

  def test_remove_handler_func(self):
    self.event_bus.addHandler('test', self.simple_key_handler)
    self.event_bus.addHandler('fu', self.simple_key_handler)

    self.event_bus.removeHandler(None, self.simple_key_handler)

    self.event_bus('test', None)
    self.assertEqual(self.eventKey, None)

    self.event_bus('fu', None)
    self.assertEqual(self.eventKey, None)

class WebNotifierTestCase(TestCase):

  class WebsocketServiceMock(WebsocketService):

    def __init__(self, callback):
      self.callback = callback

    def send(self, data):
      self.callback(data)

  def setUp(self):
    self.event_bus = EventBus(False)
    self.websocket_service = WebNotifierTestCase.WebsocketServiceMock(self.setData)
    self.web_notifier = WebNotifier(self.event_bus, self.websocket_service)

  def setData(self, data):
    self.data = data

  def test_empty_message(self):
    self.event_bus('test', None)

    dataObject = json.loads(self.data)

    self.assertEqual(dataObject['event'], 'test')
    self.assertEqual(len(dataObject), 1)

  def test_simple_message(self):
    self.event_bus('test', {'data' : 'test-data'})

    dataObject = json.loads(self.data)

    self.assertEqual(dataObject['event'], 'test')
    self.assertEqual(dataObject['data'], 'test-data')

  def test_complex_message(self):
    test_data = {
      'a' : {
        'b' : 'nested'
      },
      'b' : 1,
      'c' : Decimal(1.5)
    }

    self.event_bus('test', test_data)

    dataObject = json.loads(self.data)

    self.assertEqual(dataObject['a']['b'], 'nested')
    self.assertEqual(dataObject['b'], 1)
    self.assertEqual(dataObject['c'], 1.5)
