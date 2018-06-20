import sys

a, b, k, x = [int(i) for i in sys.stdin.readline().split()]

res = x

def f(x):
    return abs(a*x + b)

for i in range(k):
    x = f(res)
    res = x

print(res)