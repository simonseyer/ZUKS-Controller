import tornado.ioloop
import tornado.web
import tornado.websocket

clients = set()

class MainHandler(tornado.web.RequestHandler):

  def post(self):
    global clients
    for client in clients:
      client.write_message(self.request.body)
    print("Forwarded message to %i clients: %s" % 
          (len(clients), self.request.body))

class WebsocketHandler(tornado.websocket.WebSocketHandler):

  def check_origin(self, origin):
    return True

  def open(self):
    global clients
    clients.add(self)
    print("New client has CONNECTED. Client count: %i" % 
          (len(clients),))

  def on_close(self):
    global clients
    clients.remove(self)
    print("Client has DISCONNECTED. Client count: %i" % 
          (len(clients),))

application = tornado.web.Application([
  (r"/ws", WebsocketHandler),
  (r"/notify", MainHandler),
])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
