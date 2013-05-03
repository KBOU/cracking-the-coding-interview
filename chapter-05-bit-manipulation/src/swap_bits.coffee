even_mask = odd_mask = 0

for i in [0..31] by 2
  even_mask |= 1 << i
  odd_mask |= 1 << (i + 1)

swap_bits = (a) ->
  e = (a >>> 1) & even_mask
  o = (a << 1) & odd_mask
  e | o


module.exports = swap_bits
