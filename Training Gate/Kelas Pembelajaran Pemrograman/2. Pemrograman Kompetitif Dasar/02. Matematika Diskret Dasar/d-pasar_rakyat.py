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
    all_factors = [Discrete.prime_factorization(n) for n in operand]

    result_factors = []
    for factors in all_factors:
      unique_factors = set(factors)
      for factor in unique_factors:
        if factor not in result_factors:
          for _ in range(factors.count(factor)):
            result_factors.append(factor)
        else:
          old_count = result_factors.count(factor)
          new_count = factors.count(factor)
          count = min(old_count, new_count) if gcd else max(old_count, new_count)
          count_diff = abs(result_factors.count(factor) - count)
          if gcd:
            for _ in range(count_diff):
              result_factors.remove(factor)
          else:
            for _ in range(count_diff):
              result_factors.append(factor)

    product = 1
    for factor in result_factors:
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
    return Discrete.common_helper(operand, False)
  
  @staticmethod
  def fraction_simplification(fraction):
    gcd = Discrete.greatest_common_divisor(fraction)
    a, b = fraction
    if gcd > 1:
      a //= gcd
      b //= gcd
    return (a, b)


if __name__ == "__main__":
  n = int(input())
  
  ds = []
  for _ in range(n):
    d = int(input())
    ds.append(d)
  
  print(Discrete.least_common_multiple(ds))

