import sys

while True:
    n = sys.stdin.readline()
    if not n:
        break
    bs = sys.stdin.readline().split()
    res = 0
    for b in bs:
        res += int(b)

    print(res)