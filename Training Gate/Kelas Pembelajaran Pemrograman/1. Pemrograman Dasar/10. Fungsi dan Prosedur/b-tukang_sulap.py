import sys

n = int(sys.stdin.readline())
ns = []
for i in range(2):
    nsi = sys.stdin.readline().split()
    ns.append(nsi)

q = int(sys.stdin.readline())
for i in range(q):
    p, x, q, y = sys.stdin.readline().split()
    x = int(x) - 1
    y = int(y) - 1
    p = (0 if p == 'A' else 1)
    q = (0 if q == 'A' else 1)

    temp = ns[p][x]
    ns[p][x] = ns[q][y]
    ns[q][y] = temp

for nsi in ns:
    print(' '.join(nsi))

