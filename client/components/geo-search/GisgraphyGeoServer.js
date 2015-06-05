if (typeof GisgraphyGeoServer === 'undefined') {
  (function() {

    var GisgraphyGeoServer = function(reverse) {
      this.root_url = "http://localhost:8080/";
      this.root_url += reverse ? 'street/streetsearch' : '/fulltext/fulltextsearch';
      this.setDelay(0);
    };

    GisgraphyGeoServer.prototype = {
      setDelay: function(delay) {
        this.delay = delay;
        this.throtteledRequest = Cowboy.throttle(delay, this._sendRequest);
      },
      sendRequest: function(parameters, callback) {
        this.throtteledRequest(parameters, callback);
      },
      _sendRequest: function(parameters, callback) {
        xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == XMLHttpRequest.DONE &&
                xmlhttp.status == 200) {
                callback(JSON.parse(xmlhttp.responseText));
            }
        };

        var params = {
          format: 'json',
        };
        // Merge external and internal params
        Object.assign(params, parameters);

        // Create url
        var urlParams = Object.keys(params).map(function(key) {
            return key + '=' + params[key];
        }).join('&');
        var url = this.root_url + '?' + urlParams;

        xmlhttp.open("GET", url, true);
        xmlhttp.setRequestHeader('content-type',
                                 'application/json; charset=utf-8');
        xmlhttp.send();
      }
    }

    window.GisgraphyGeoServer = GisgraphyGeoServer;
  })();
}
