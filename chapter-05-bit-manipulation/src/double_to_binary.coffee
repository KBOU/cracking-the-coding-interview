double2Binary = (x) ->
  tmp = x
  a = []
  for i in [0..31]
    tmp *= 2
    if tmp >= 1
      a[i] = 1
      tmp -= 1
    else
      a[i] = 0

  if (tmp *= 2) isnt 0
    return 'Error'

  str = ''
  for i in [0..31]
    str += a[i].toString()

  str

module.exports = double2Binary
