import sys

for line in sys.stdin:
    a, b = line.split()
    res = int(a) * int(b) / 2
    print('%.2f' % res)