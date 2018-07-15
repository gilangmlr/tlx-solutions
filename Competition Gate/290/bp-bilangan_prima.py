import sys

n = int(sys.stdin.readline())

def is_prime(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if is_prime(n):
    print('Prima')
else:
    print('Bukan Prima')