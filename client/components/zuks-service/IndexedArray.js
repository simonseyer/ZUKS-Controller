if (typeof IndexedArray === 'undefined') {
  (function() {
    /*
    An indexed array.
    It allows to efficiently retrieve a list of all values (which
    is not possible with an object) and retrieve an object based on
    an indexed key (which is not possible with arrays).

    The indexVariable parameter defines which variable of the objects
    should be indexed. Only this index could be used when calling get.
    Each object added has to have this variable.
    */
    var IndexedArray = function(indexVariable) {
      this._indexVariable = indexVariable;
      this.values = [];
      this._index = {};
      this._init();
    };

    IndexedArray.prototype = {
      /*
      Get an object that was added to the values
      array by passing it's indexVariable's value.
      */
      get: function(index) {
        return this._index[index];
      },
      /*
      Initialize the IndexedArray
      */
      _init: function() {
        /*
        Observe the values variable for the case it
        is overriden. If this happens, the array is
        reinitialized.
        */
        Object.observe(this, function(changes) {
          changes.forEach(function(change) {
            if (change.name == 'values') {
              self._initArrayObservation();
            }
          });
        });
        self._initArrayObservation();
      },
      /*
      Starts observer the values array and rebuilds
      the index.
      */
      _initArrayObservation: function() {
        // Build initial index
        this._index = {};
        this.values.forEach(function(value) {
          this._addToIndex(value);
        }.bind(this));

        // Observe changes in the values array
        Array.observe(this.values, function(changes) {
          self._refreshIndex(changes);
        });
      },
      /*
      Refreshes the index, when the values array changes. All cases
      of change are handeled: add, remove and update.
      */
      _refreshIndex: function(changes) {
        var self = this;
        changes.forEach(function(change) {
          if (change.type == 'update') {
            self._removeFromIndex(change.oldValue);
            self._addToIndex(self.values[change.name]);
          } else if (change.type == 'delete') {
            self._removeFromIndex(change.oldValue);
          } 
          if (change.removed && change.removed.length > 0) {
            change.removed.forEach(_removeFromIndex);
          }
          if (change.addedCount && change.addedCount > 0) {
            for(var i=0; i < change.addedCount; i++) {
              self._addToIndex(self.values[change.index + i]);
            }
          }
        });
      },
      /*
      Removes an object from the index, if it is indexed.
      */
      _removeFromIndex: function(object) {
        var key = object[this._indexVariable];
        if (key in this._index) {
          delete this._index[key];
        }
      },
      /*
      Adds an object to the index.

      If there is already an object in the index with an equal
      indexVariable's value, then the new value is added.

      If the object doesn't have a variable named with the value
      of indexVariable, then the object is not added to the index.

      In both cases, this size of the values array and the index
      is different. This should be prevented by the caller.
      */
      _addToIndex: function(object) {
        if (!(this._indexVariable in object)) {
          console.warn("Missing index variable ", this._indexVariable, " on object ", object);
          return;
        }
        if (this._index[object[this._indexVariable]] !== undefined) {
          console.warn("Duplicate key in IndexedArray:", object);
        }
        this._index[object[this._indexVariable]] = object;
      }
    }

    window.IndexedArray = IndexedArray;
  })();
}
