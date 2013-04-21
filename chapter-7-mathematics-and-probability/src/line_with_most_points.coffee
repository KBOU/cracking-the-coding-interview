class Point
  constructor: (@x, @y) ->


class Line
  @EPSILON = 0.00001
  constructor: (@p1, @p2) ->
    if Math.abs(@p1.x - @p2.x) < Line.EPSILON
      @slope = null
      @intercept = null
      @fixed_x = floor_to_nearest @p1.x
    else
      @slope = floor_to_nearest((@p1.y - @p2.y) / (@p1.x - @p2.x))
      @intercept = floor_to_nearest(@p1.y - @slope * @p1.x)
      @fixed_x = null

  is_infinite: ->
    not @fixed_x?

  floor_to_nearest = (a) ->
    r = +(a / Line.EPSILON)
    r * Line.EPSILON


class Main
  constructor: (arr) ->
    @points = []
    @lines = []
    for el in arr
      @points.push new Point(el[0], el[1])

    if @points.length < 2
     return
    for i in [0..(@points.length - 2)]
      for j in [(i + 1)..(@points.length - 1)]
        ln = new Line(@points[i], @points[j])
        @lines.push ln

  calc_max_count: () ->
    max_cnt = 0
    map = {}
    for ln in @lines
      key = ln.slope.toString() + '_' + ln.intercept.toString()
      if map[key]?
        if not (ln.p1 in map[key].points)
          console.log ln.p1, ln.p2, map[key].points
          map[key].points.push(ln.p1)
          map[key].cnt++
        if not (ln.p2 in map[key].points)
          map[key].points.push(ln.p2)
          map[key].cnt++
      else
        map[key] = {
          cnt: 2
          points: [ln.p1, ln.p2]
        }
      max_cnt = map[key].cnt if max_cnt < map[key].cnt

    max_cnt

module.exports = Main
