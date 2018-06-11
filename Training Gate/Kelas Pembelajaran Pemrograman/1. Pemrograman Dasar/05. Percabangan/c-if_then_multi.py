import sys

for line in sys.stdin:
    a = int(line)
    if a > 0:
        if a % 2 == 0:
            print(a)