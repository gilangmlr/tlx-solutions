import sys

a, b, k, x = [int(i) for i in sys.stdin.readline().split()]

def f(x, k):
    if k == 1:
        return abs(a*x + b)

    return abs(a*f(x, k - 1) + b)

print(f(x, k))