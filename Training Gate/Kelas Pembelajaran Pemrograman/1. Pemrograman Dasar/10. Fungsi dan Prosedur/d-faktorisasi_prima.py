import sys
from math import sqrt, floor

def sieve_of_erathostenes(n):
    bools = [True for i in range(n + 1)]
    bools[0] = False
    bools[1] = False
    for i in range(2, floor(sqrt(n) + 1)):
        if bools[i]:
            for j in range(i*i, n + 1, i):
                bools[j] = False
    return [idx for idx, val in enumerate(bools) if val]

def prime_factorization(n):
    primes = sieve_of_erathostenes(int(1e6))
    factors = []

    idx = 0
    while n > 1:
        while n % primes[idx] != 0:
            idx += 1
        factors.append(primes[idx])
        n //= primes[idx]
    
    return factors

n = int(sys.stdin.readline())
    
factors = prime_factorization(n)

facts = [str(x) if factors.count(x) == 1 else str(x) + '^' + str(factors.count(x)) for x in sorted(set(factors)) ]
print(' x '.join(facts))