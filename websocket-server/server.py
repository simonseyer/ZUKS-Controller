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
