class Discrete:
  @staticmethod
  def is_prime(n):
    if n == 2:
      return True
    i = 3
    while i * i <= n:
      if n % i == 0:
        return False
      i += 2
    return True
  
  @staticmethod
  def next_prime(n):
    n += 1
    if n % 2 == 0:
      n += 1
    while not Discrete.is_prime(n):
      n += 2
    return n

  @staticmethod
  def prime_factorization(n):
    factors = []
    if n == 1:
      factors.append(1)
    divider = 2
    while n > 1:
      if n % divider == 0:
        n //= divider
        factors.append(divider)
      else:
        if not Discrete.is_prime(n):
          divider = Discrete.next_prime(divider)
        else:
          factors.append(n)
          break
    return factors
  
  @staticmethod
  def prime_factors_to_string(factors):
    result = []
    unique_factors = sorted(set(factors))
    for factor in unique_factors:
      if factors.count(factor) > 1:
        result.append('{}^{}'.format(factor, factors.count(factor)))
      else:
        result.append(str(factor))

    return ' x '.join(result)

if __name__ == "__main__":
  n = int(input())

  factors = Discrete.prime_factorization(n)

  print(Discrete.prime_factors_to_string(factors))
