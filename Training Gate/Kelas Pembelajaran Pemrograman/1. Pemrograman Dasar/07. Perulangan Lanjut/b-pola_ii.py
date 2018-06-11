import sys

for a in sys.stdin:
    a = int(a)

    for i in range(1, a + 1):
        pola = [' ' if j <= a - i  else '*' for j in range(1, a + 1)]
        print(''.join(pola))