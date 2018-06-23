import sys

n = int(sys.stdin.readline())

codes = []
for i in range(n):
    code = str(sys.stdin.readline()).rstrip()
    code = str(code[1:])
    codes.append(code)

r, c = sys.stdin.readline().split()
r = int(r)
c = int(c)

mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(0)
    mat.append(row)

def make_power_of_two(n):
    temp = 1
    while temp < n:
        temp *= 2
    return temp

d = max(make_power_of_two(r), make_power_of_two(c))
dr = d - r
dc = d - c
if dr > 0:
    for i in range(dr):
        arow = [0 for i in range(c)]
        mat.append(arow)

if dc > 0:
    for row in mat:
        for i in range(dc):
            row.append(0)

def make_homogen_1(r, c, h, mat):
    for i in range(r, r + h):
        for j in range(c, c + h):
            mat[i][j] = 1

code = []
def quadtree_ii(r, c, n, mat):
    h = n // 2
    if h == 0:
        return

    code.append(0)
    r0 = r
    c0 = c
    if len(codes) > 0 and ''.join([str(i) for i in code]) != codes[0]:
        quadtree_ii(r0, c0, h, mat)
    else:
        if len(codes) > 0:
            make_homogen_1(r0, c0, h, mat)
            codes.pop(0)
        else:
            return
    code.pop()

    r1 = r
    c1 = c + h
    code.append(1)
    if len(codes) > 0 and ''.join([str(i) for i in code]) != codes[0]:
        quadtree_ii(r1, c1, h, mat)
    else:
        if len(codes) > 0:
            make_homogen_1(r1, c1, h, mat)
            codes.pop(0)
        else:
            return
    code.pop()

    r2 = r + h
    c2 = c
    code.append(2)
    if len(codes) > 0 and ''.join([str(i) for i in code]) != codes[0]:
        quadtree_ii(r2, c2, h, mat)
    else:
        if len(codes) > 0:
            make_homogen_1(r2, c2, h, mat)
            codes.pop(0)
        else:
            return
    code.pop()

    r3 = r + h
    c3 = c + h
    code.append(3)
    if len(codes) > 0 and ''.join([str(i) for i in code]) != codes[0]:
        quadtree_ii(r3, c3, h, mat)
    else:
        if len(codes) > 0:
            make_homogen_1(r3, c3, h, mat)
            codes.pop(0)
        else:
            return
    code.pop()

if len(codes) > 0:
    if codes[0] == '':
        make_homogen_1(0, 0, len(mat), mat)
    else:
        quadtree_ii(0, 0, len(mat), mat)

for i in mat[:r]:
    row = [str(i) for i in i[:c]]
    print(' '.join(row))