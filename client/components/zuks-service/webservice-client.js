define(function() {
    var root_url = "ws://localhost:8888/ws";
    return {
        ws: null,
        event_handler: {},
        initWebSocket: function() {
          var self = this;

          self.ws = new WebSocket(root_url);
          self.ws.onopen = function() {
            console.log("Webservice connected");
          };
          self.ws.onmessage = function(msg) {
            console.log("Recieved message: " + msg.data);

            object = JSON.parse(msg.data);

            var event_function = eval("self.event_handler." + object.event);
            if (event_function) {
              event_function(self, object.data);
            } else {
              console.warn("No handler registered for event: " + object.event);
            }
          };
        }
    } 
});