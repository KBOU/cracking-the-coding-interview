sieve_of_eratosthenes = (max) ->
  flags = init_flags(max)
  prime = 2

  while prime <= max
    cross_off(flags, prime)
    try
      prime = get_next_prime(flags, prime)
    catch e
      break

  print_primes flags

init_flags = (max) ->
  flags = []
  for i in [0..max]
    if i < 2
      flags[i] = false
    else
      flags[i] = true

cross_off = (flags, prime) ->
  for i in [(prime * prime)..(flags.length - 1)] by prime
    flags[i] = false

get_next_prime = (flags, prime) ->
  for i in [(prime + 1)..(flags.length - 1)]
    return i if flags[i] is true

print_primes = (flags) ->
  primes = []
  for i in [1..(flags.length - 1)]
    primes.push(i) if flags[i] is true

  console.log(primes.join(' '))


if process.argv[2]?
  sieve_of_eratosthenes +(process.argv[2])
