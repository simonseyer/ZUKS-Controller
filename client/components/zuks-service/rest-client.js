define(function() {
    var root_url = "http://localhost:8000/";
    return {
        errorHandler: null,
        put: function(type, object) {
          this.send(type, object, "PUT");
        },
        post: function(type, object) {
          this.send(type, object, "POST");
        },
        send: function(type, object, method) {
          var self = this;
          $.ajax({
            url:root_url + type + "/",
            type:method,
            data:JSON.stringify(object),
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            error: self.errorHandler
          });
        },
        get: function(url, callback) {
          var self = this;
          $.ajax({
            url:root_url + url + "/",
            type:"GET",
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            success: callback,
            error: self.errorHandler
          });
        },
    }   
});