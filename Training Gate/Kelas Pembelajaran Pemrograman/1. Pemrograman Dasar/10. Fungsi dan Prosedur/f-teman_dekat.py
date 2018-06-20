import sys

n, d = sys.stdin.readline().split()
n = int(n)
d = int(d)

ts = []
for i in range(int(n)):
    x, y = sys.stdin.readline().split()
    ts.append([int(x), int(y)])

def t_val(i, j):
    xi = ts[i][0]
    yi = ts[i][1]
    xj = ts[j][0]
    yj = ts[j][1]

    return abs(xj - xi)**d + abs(yj - yi)**d

t_vals = []
for i in range(n):
    for j in range(n):
        if j != i:
            t_vals.append(t_val(i, j))

print(min(t_vals), max(t_vals))