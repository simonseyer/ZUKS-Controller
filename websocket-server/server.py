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

import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import settings

clients = set()

class MainHandler(tornado.web.RequestHandler):

  def post(self):
    global clients
    for client in clients:
      if not client.uid or self.getUID() == client.uid:
        client.write_message(self.request.body)

    print("Forwarded message to clients: %s" % (self.request.body,))

  def getUID(self):
    data = json.loads(self.request.body.decode("utf-8"))
    event = data['event']
    try:
      return int(event.split('#')[1])
    except:
      return -1

class WebsocketHandler(tornado.websocket.WebSocketHandler):

  def check_origin(self, origin):
    return True

  def open(self):
    global clients
    self.uid = False
    clients.add(self)
    print("New client has CONNECTED. Client count: %i" % (len(clients),))

  def on_message(self, message):
    self.uid = int(message)
    print("Client has registered with id: %i" % (self.uid,))

  def on_close(self):
    global clients
    clients.remove(self)
    print("Client has DISCONNECTED. Client count: %i" % (len(clients),))

application = tornado.web.Application([
  (r"/ws", WebsocketHandler),
  (r"/notify", MainHandler),
])

if __name__ == "__main__":
  application.listen(settings.PORT)
  tornado.ioloop.IOLoop.instance().start()
