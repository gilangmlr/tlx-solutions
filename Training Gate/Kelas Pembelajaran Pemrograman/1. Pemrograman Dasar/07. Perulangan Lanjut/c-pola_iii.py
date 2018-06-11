import sys

for a in sys.stdin:
    a = int(a)
    idx = 0
    for i in range(a):
        for j in range(i + 1):
            print(idx, end='')
            idx += 1
            idx %= 10
        print('')