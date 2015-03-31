if (typeof NominatimGeoServer === 'undefined') {
  (function() {

    var NominatimGeoServer = function(reverse) {
      this.root_url = "http://nominatim.openstreetmap.org/";
      this.root_url += reverse ? 'reverse' : '';
      this.email = "simon.seyer@zuks.org";
      this.setDelay(1000);
    };

    NominatimGeoServer.prototype = {
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
          email: this.email
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

    window.NominatimGeoServer = NominatimGeoServer;
  })();
}
