class Calculation
  negate = (a) ->
    d = if a < 0 then 1 else (~1) | 1
    r = 0
    while a isnt 0
      a += d
      r += d

    return r

  @multiply: (a, b) ->
    r = 0
    neg = false
    if b < 0
      b = negate b
      neg = true

    for i in [1..b]
      r += a
    if not neg then r else negate r
  @subtract: (a, b) ->
    a + negate b
  @divide: (a, b) ->
    cnt = 0
    neg = false
    if a < 0
      neg = not neg
      a = negate a
    if b < 0
      neg = not neg
      b = negate b

    nb = negate b
    while a >= b
      a += nb
      cnt++
    if not neg then cnt else negate cnt


module.exports = Calculation
