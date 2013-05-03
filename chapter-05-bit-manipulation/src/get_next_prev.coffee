bit_ary = (a) ->
  ary = []
  while a isnt 0
    ary.push(a & 1)
    a >>>= 1
  ary.reverse().join('')

get_next = (a) ->
  tzero = cnt_trailing_block a, 0
  tone = cnt_trailing_block a >> tzero, 1
  pos = tzero + tone

  allone = ~0
  mask = allone ^ ((1 << pos) - 1)

  a |= (1 << pos)
  a &= mask
  a |= (1 << (tone - 1)) - 1


get_prev = (a) ->
  tone = cnt_trailing_block a, 1
  tzero = cnt_trailing_block a >> tone, 0
  pos = tzero + tone

  mask = (1 << pos) - 1

  a &= ~(1 << pos)
  a |= mask
  a &= ~((1 << (tzero - 1)) - 1)
  a

cnt_trailing_block = (a, bit) ->
  cnt = 0
  while (a & 1) is bit
    cnt++
    a >>= 1
  cnt

module.exports =
  bit_ary: bit_ary
  get_next: get_next
  get_prev: get_prev
