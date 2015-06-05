
module.exports = class FakeImageRetriever
  constructor: () ->
    null

  retrieveImage: (tileInfo, callback, error) ->
    callback(tileInfo)
