class Point
  constructor: (@x, @y) ->
  lefter: (p) ->
    @x < p.x
  righter: (p) ->
    @x > p.x
  upper: (p) ->
    @y > p.y
  lower: (p) ->
    @y < p.y

class Size
  constructor: (@w, @h) ->
    throw 'Error' if @w < 0 or @h < 0

class Square
  constructor: (@center, @size) ->
    @top_left = new Point(@center.x - @size.w / 2.0, @center.y + @size.h / 2.0)
    @top_right = new Point(@center.x + @size.w / 2.0, @center.y + @size.h / 2.0)
    @bottom_left = new Point(@center.x - @size.w / 2.0, @center.y - @size.h / 2.0)
    @bottom_right = new Point(@center.x + @size.w / 2.0, @center.y - @size.h / 2.0)

  half_line_ends: (square) ->
    throw 'ERROR' if @center.x is square.center.x and @center.y is square.center.y

    line = new Line(@center, square.center)
    if @top_left.upper square.top_left
      top_line = new Line(@top_left, @top_right)
    else
      top_line = new Line(square.top_left, square.top_right)
    if @bottom_left.lower square.bottom_left
      bottom_line = new Line(@bottom_left, @bottom_right)
    else
      bottom_line = new Line(square.bottom_left, square.bottom_right)


    p1 = line.intersect(top_line)
    p2 = line.intersect(bottom_line)
    if not p1?
      if @top_left.lefter square.top_left
        left_line = new Line(@top_left, @bottom_left)
      else
        left_line = new Line(square.top_left, square.bottom_left)
      if @top_right.righter square.top_right
        right_line = new Line(@top_right, @bottom_right)
      else
        right_line = new Line(square.top_right, square.bottom_right)
      p1 = line.intersect(left_line)
      p2 = line.intersect(right_line)

    [p1, p2]


class Line
  @EPSILON = 0.000000001
  constructor: (@p1, @p2) ->
    if @p1.x is @p2.x
      @slope = null
      @intersept = null
      @abs_x = @p1.x
    else
      @slope = (@p1.y - @p2.y) / (@p1.x - @p2.x)
      @intersept = @p1.y - @slope * @p1.x
      @abs_x = null

  intersect: (line) ->
    if not @slope?
      if line.p1.x <= @abs_x <= line.p2.x or line.p2.x <= @abs_x <= line.p1.x
        return new Point(@abs_x, line.p1.y + line.slope * (@abs_x - line.p1.x))
    else if not line.slope?
      y = @slope * line.abs_x + @intersept
      if line.p1.y <= y <= line.p2.y or line.p2.y <= y <= line.p1.y
        return new Point(line.abs_x, y)
    else
      if Math.abs(line.slope - @slope) > Line.EPSILON or Math.abs(line.intersept - @intersept) > Line.EPSILON
        x = -(@intersept - line.intersept) / (@slope - line.slope)
        if line.p1.x <= x <= line.p2.x or line.p2.x <= x <= line.p1.x
          return new Point(x, @slope * x + @intersept)

    null



module.exports.Point = Point
module.exports.Size = Size
module.exports.Square = Square
module.exports.Line = Line
