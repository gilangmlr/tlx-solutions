import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break

    n, m, p = line.split()
    
    mat1 = []
    for i in range(int(n)):
        els = sys.stdin.readline().split()
        els = [int(el) for el in els]
        mat1.append(els)
    
    mat2 = []
    for i in range(int(m)):
        els = sys.stdin.readline().split()
        els = [int(el) for el in els]
        mat2.append(els)
    
    mat = []
    for i in range(int(n)):
        row = []
        for j in range(int(p)):
            val = 0
            for k in range(int(m)):
                val += mat1[i][k] * mat2[k][j]
            row.append(str(val))
        mat.append(row)
    
    for i in range(int(n)):
        print(' '.join(mat[i]))
