import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break

    m, n = line.split()
    
    rows = []
    for i in range(int(m)):
        els = sys.stdin.readline().split()
        els = [int(el) for el in els]
        rows.append(els)
    
    for i in range(int(n)):
        row = []
        for j in list(reversed(range(int(m)))):
            row.append(str(rows[j][i]))
        
        print(' '.join(row))
