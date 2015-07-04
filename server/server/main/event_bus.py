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

import re
from threading import Thread

class EventBus:
  '''Simple event bus implementation

  Bus for event subscribtion. An event contains
  of a key and a value. The value could be any
  type. The receiver is able to distinct the value's type
  by evaluating the event key.

  The key should be a string, separated by underscores. This
  convention allows to consistently subscribe to parts of the
  keys.

  Example: user_add, user_update, user_delete.

  A event handler now could subscribe to 'user_.*'. By
  evaluating this key pattern with regex, all events that
  start with 'user_' are transmitted to the handler.

  All of these three examples have the prefix user, so
  the receiver could expect to get a user object as value.
  '''

  def __init__(self, async=True):
    '''Create a event bus

    Keyword arguments:
    async -- if true, all handlers are executed in a separate thread (default: True)
    '''
    self.handler = set()
    self.async = async

  def addHandler(self, key_pattern, func):
    '''Add a new event handler

    The func is called, when the event key machtches
    the key_pattern.

    Keyword arguments:
    key_pattern -- the regex pattern as string to filter events
    func        -- the function to be called when an event occurs
    '''
    self.handler.add(EventHandler(key_pattern, func))

  def removeHandler(self, key_pattern=None, func=None):
    '''Remove an event handler

    Remove a handler function that is associated with a key. If
    the key is not provided (None), the function is completly
    removed from the registered handlers.

    Keyword arguments:
    func        -- the registered handler function (default: None)
    key_pattern -- the registered key pattern (default: None)
    '''
    handlersToRemove = set()
    for handler in self.handler:
      if handler.matches(key_pattern, func):
        handlersToRemove.add(handler)
    self.handler -= handlersToRemove

  def __call__(self, key, value=None):
    '''Submit a new event

    Keyword arguments:
    key   -- the key, that identifies the event
    value -- a value, that should by passed to the handler
    '''
    if self.async:
      Thread(target=self.__fire, args=(key, value)).start()
    else:
      self.__fire(key, value)

  def __fire(self, key, value):
    '''Submit a new event

    Keyword arguments:
    key   -- the key, that identifies the event
    value -- a value, that should by passed to the handler
    '''
    for handler in self.handler:
      if self.async:
        Thread(target=handler, args=(key, value)).start()
      else:
        handler(key, value)

class EventHandler:
  '''Wrapper class for event handling functions'''

  def __init__(self, key_pattern, func):
    '''Create a event handler

    Keyword arguments:
    key_pattern -- the regex pattern as string to filter events
    func        -- the function to be called when an event occurs
    '''
    self.key_pattern = re.compile(key_pattern)
    self.raw_key_pattern = key_pattern
    self.func = func

  def __call__(self, key, value):
    '''Submit an event to the handler function

    Calls the handler function, if the key matches the
    configured key_pattern.

    Keyword arguments:
    key   -- the key, that identifies the event
    value -- a value, that should by passed to the handler
    '''
    if self.key_pattern.match(key):
      self.func(key, value)

  def matches(self, key_pattern=None, func=None):
    '''Checks, if the parameters matches the values of the handler

    If key_pattern or func is None, this field is ignored.

    Keyword arguments:
    key_pattern -- the key, that identifies the event
    func        -- the function to be called when an event occurs
    '''
    func_matches = not func or func == self.func
    key_matches = not key_pattern or key_pattern == self.raw_key_pattern
    return func_matches and key_matches

class EventBusLogger:
  '''A simple logger that captures all event bus events'''

  def __init__(self, event_bus):
    '''Create a new event bus logger

    Keyword arguments:
    event_bus -- the event bus to observe
    '''
    import logging
    self.logger = logging.getLogger(__name__)

    event_bus.addHandler('.*', self.log)


  def log(self, key, value):
    '''Callback method for the event bus

    Keyword arguments:
    key   -- the key, that identifies the event
    value -- a value, that is passed to the handler
    '''
    self.logger.info("%s: %s" % (key, value))
