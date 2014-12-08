from django.test import TestCase

from server.main.event_bus import EventBus

class EventBusTestCase(TestCase):
  def setUp(self):
    self.event_bus = EventBus()
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