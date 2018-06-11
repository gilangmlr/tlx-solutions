import sys

while True:
    n = sys.stdin.readline()
    if not n:
        break
    ns = sys.stdin.readline().split()
    ns = [int(n) for n in ns]

    print('%d %d' %(max(ns), min(ns)))