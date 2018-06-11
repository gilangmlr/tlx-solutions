import sys

for n in sys.stdin:
    m = int(n)

    divider = 1
    while divider <= m:
        if (m % divider == 0):
            print(m // divider)

        divider += 1
