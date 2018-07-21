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
  
  @staticmethod
  def common_helper(operand, gcd):
    a = operand[0]
    b = operand[1]

    a_factors = Discrete.prime_factorization(a)
    b_factors = Discrete.prime_factorization(b)

    factors = set(a_factors + b_factors)
    product = 1
    for factor in factors:
      a_count = a_factors.count(factor)
      b_count = b_factors.count(factor)
      count = min(a_count, b_count) if gcd else max(a_count, b_count)
      for _ in range(count):
        product *= factor
    return product
  
  @staticmethod
  def euclidian(a, b):
    if b == 0:
      return a
    else:
      return Discrete.euclidian(b, a % b)
  
  @staticmethod
  def greatest_common_divisor(operand):
    a, b = operand
    return Discrete.euclidian(a, b)

  @staticmethod
  def least_common_multiple(operand):
    gcd = Discrete.greatest_common_divisor(operand)
    a = max(operand)
    b = min(operand)
    return (a // gcd) * b
  
  @staticmethod
  def fraction_simplification(fraction):
    gcd = Discrete.greatest_common_divisor(fraction)
    a, b = fraction
    if gcd > 1:
      a //= gcd
      b //= gcd
    return (a, b)


if __name__ == "__main__":
  abcd = input().split()
  temp = input().split()
  abcd = abcd + temp
  a, b, c, d = [int(i) for i in abcd]

  a, b = Discrete.fraction_simplification((a, b))
  c, d = Discrete.fraction_simplification((c, d))

  f = Discrete.least_common_multiple((b, d))
  e = (f // b * a) + (f // d * c)
  e, f = Discrete.fraction_simplification((e, f))

  print('{} {}'.format(e, f))
