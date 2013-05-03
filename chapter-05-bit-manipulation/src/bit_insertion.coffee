bit_insertion = (n, m, i, j) ->
  upper = (~0) << j
  lower = (1 << i) - 1
  mask = upper | lower

  n &= mask
  n |= (m << i)
  str = ''
  for x in [31..0]
    if (n & 1 << x) isnt 0
      str += '1'
    else
      str += '0'
  str
module.exports = bit_insertion
