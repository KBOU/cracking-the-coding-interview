
class KthPrime
  @getKthPrime: (index) ->
    q3 = []
    q5 = []
    q7 = []
    q3.push 1
    min = Number.MAX_VALUE
    for i in [1..index]
      m3 = if q3[0]? then q3[0] else Number.MAX_VALUE
      m5 = if q5[0]? then q5[0] else Number.MAX_VALUE
      m7 = if q7[0]? then q7[0] else Number.MAX_VALUE

      min = Math.min(m3, m5, m7)
      if min is m3
        q3.shift()
        q3.push(m3 * 3)
        q5.push(m3 * 5)
      else if min is m5
        q5.shift()
        q5.push(m5 * 5)
      else if min is m7
        q7.shift()
      q7.push(min * 7)

    min
    
module.exports = KthPrime
