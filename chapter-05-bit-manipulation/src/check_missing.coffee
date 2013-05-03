do_check_missing = (arr, col, res) ->
  return if arr.length is 0

  czero = []
  cone = []
  for el in arr
    if (el & (1 << col)) > 0
      cone.push(el)
    else
      czero.push(el)

  if czero.length <= cone.length
    res.push(0)
    do_check_missing(czero, col+1, res)
  else
    res.push(1)
    do_check_missing(cone, col+1, res)

  res

check_missing = (arr) ->
  res = []
  do_check_missing(arr, 0, res)

  result = null
  for el, i in res
    result = 0 if i is 0
    result |= (el & 1) << i

  result

module.exports = check_missing
