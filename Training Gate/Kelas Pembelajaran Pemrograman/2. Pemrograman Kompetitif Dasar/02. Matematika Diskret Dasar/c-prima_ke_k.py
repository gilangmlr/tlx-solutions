class Discreet:
  @staticmethod
  def sieve_of_erathostenes(n):
    bools = [True for i in range(n + 1)]
    bools[0] = False
    bools[1] = False
    i = 2
    while i*i <= n:
      if bools[i]:
        for j in range(i*i, n + 1, i):
          bools[j] = False
      i += 1
    return [idx for idx, val in enumerate(bools) if val]
  
if __name__ == "__main__":
  t = int(input())
  
  upper_bound_k = 77777
  upper_bound_prime = 1000000 # upper_bound_k-th prime is (989_999) less than 1_000_000
  precomputed_primes = Discreet.sieve_of_erathostenes(upper_bound_prime)

  for _ in range(t):
    k = int(input())
    print(precomputed_primes[k - 1])
