class Line
  @EPSILON = 0.000001
  constructor: (@slope, @intercept) ->
  intersect: (line) ->
    not (Math.abs(@slope - line.slope) < Line.EPSILON or Math.abs(@intercept - line.intercept) < Line.EPSILON)



module.exports = Line
