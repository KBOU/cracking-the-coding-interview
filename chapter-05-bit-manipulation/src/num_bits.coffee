numbits = (a, b) ->
  cnt = 0
  n = a ^ b
  while n > 0
    if (n & 1) is 1
      cnt++
    n >>= 1
    # 別解
    #cnt++
    #n &= n - 1
  cnt

module.exports = numbits
