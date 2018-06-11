import sys

for line in sys.stdin:
    a, b = line.split()
    a = int(a)
    b = int(b)

    ls = range(1, a + 1)

    pola = ['*' if n % b == 0 else str(n) for n in ls]
    print(' '.join(pola))