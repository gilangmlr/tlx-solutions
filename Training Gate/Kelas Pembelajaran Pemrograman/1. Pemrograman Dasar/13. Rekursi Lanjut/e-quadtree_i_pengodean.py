import sys

r, c = sys.stdin.readline().split()
r = int(r)
c = int(c)

mat = []
for i in range(r):
    row = sys.stdin.readline().split()
    row = [int(i) for i in row]
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

def is_homogen(mat):
    if len(mat) == 1:
        return True
    for r in mat:
        for e in r:
            if e != mat[0][0]:
                return False
    return True

codes = []
code = []
def quadtree_i(mat):
    lm = len(mat)
    h = lm // 2
    if h == 0:
        return

    m0 = mat[:h]
    for key, i in enumerate(m0):
        m0[key] = i[:h]
    code.append(0)
    if not is_homogen(m0):
        quadtree_i(m0)
    elif m0[0][0] == 1:
        code.insert(0, m0[0][0])
        codes.append(''.join([str(i) for i in code]))
        code.pop(0)
    code.pop()

    m1 = mat[:h]
    for key, i in enumerate(m1):
        m1[key] = i[h:]
    code.append(1)
    if not is_homogen(m1) and h != 1:
        quadtree_i(m1)
    elif m1[0][0] == 1:
        code.insert(0, m1[0][0])
        codes.append(''.join([str(i) for i in code]))
        code.pop(0)
    code.pop()

    m2 = mat[h:]
    for key, i in enumerate(m2):
        m2[key] = i[:h]
    code.append(2)
    if not is_homogen(m2) and h != 1:
        quadtree_i(m2)
    elif m2[0][0] == 1:
        code.insert(0, m2[0][0])
        codes.append(''.join([str(i) for i in code]))
        code.pop(0)
    code.pop()

    m3 = mat[h:]
    for key, i in enumerate(m3):
        m3[key] = i[h:]
    code.append(3)
    if not is_homogen(m3) and h != 1:
        quadtree_i(m3)
    elif m3[0][0] == 1:
        code.insert(0, m3[0][0])
        codes.append(''.join([str(i) for i in code]))
        code.pop(0)
    code.pop()

if not is_homogen(mat):
    quadtree_i(mat)
elif mat[0][0] == 1:
    codes.append(1)

print(len(codes))
for i in codes:
    print(i)