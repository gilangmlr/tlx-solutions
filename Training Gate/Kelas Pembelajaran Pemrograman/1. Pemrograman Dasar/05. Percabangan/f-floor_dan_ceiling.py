import sys
from math import floor, ceil

for line in sys.stdin:
    a = float(line)
    f = floor(a)
    c = ceil(a)

    print('%d %d' % (f, c))