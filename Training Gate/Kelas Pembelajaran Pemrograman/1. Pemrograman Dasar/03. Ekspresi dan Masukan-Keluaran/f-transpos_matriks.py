import sys

mat = []
for line in sys.stdin:
    mat.append([int(el) for el in line.split()])

tMat = []
for i in range(len(mat[0])):
    tMat.append([row[i] for row in mat])

for row in tMat:
    row = [str(el) for el in row]
    row = ' '.join(row)
    print(row)