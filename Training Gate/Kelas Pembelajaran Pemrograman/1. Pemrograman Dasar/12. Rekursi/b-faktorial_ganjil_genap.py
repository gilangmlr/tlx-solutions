import sys

n = int(sys.stdin.readline())

def fac_odd_even(n):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return n // 2 * fac_odd_even(n-1)
    else:
        return n * fac_odd_even(n-1)

print(fac_odd_even(n))