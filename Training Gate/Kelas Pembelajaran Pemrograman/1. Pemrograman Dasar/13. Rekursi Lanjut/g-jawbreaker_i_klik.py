import sys

m, n = [int(i) for i in sys.stdin.readline().split()]

mat = []
for i in range(m):
    row = [int(i) for i in sys.stdin.readline().split()]
    mat.append(row)

b, k = [int(i) for i in sys.stdin.readline().split()]

el = mat[b][k]
for i in range(m):
    for j in range(n):
        if mat[i][j] == el:
            mat[i][j] = '+'
        else:
            mat[i][j] = '-'

def get_neighbors(b, k, el, mat):
    lb = len(mat)
    lk = len(mat[0])
    neighbors = []
    if b > 0:
        if mat[b - 1][k] == '+':
            neighbors.append([b - 1, k])
    if b < lb - 1:
        if mat[b + 1][k] == '+':
            neighbors.append([b + 1, k])
    if k > 0:
        if mat[b][k - 1] == '+':
            neighbors.append([b, k - 1])
    if k < lk - 1:
        if mat[b][k + 1] == '+':
            neighbors.append([b, k + 1])
    return neighbors

def click(b, k, el, mat):
    mat[b][k] = '*'
    # print('mat')
    # for row in mat:
    #     print(''.join([str(i) for i in row]))

    for n in get_neighbors(b, k, el, mat):
        click(n[0], n[1], el, mat)

def game_not_over(mat):
    for row in mat:
        if '+' in row:
            return True
    return False

def get_bk(mat):
    for i, row in enumerate(mat):
        for j, el in enumerate(row):
            if el == '+':
                return [i, j]

score = 0
click(b, k, mat[b][k], mat)
counter = 0
for row in mat:
    for c in row:
        if c == '*':
            counter += 1
score += counter * (counter - 1)
for i in range(m):
    for j in range(n):
        if mat[i][j] == '*':
            mat[i][j] = '-'
print(score)
# while game_not_over(mat):
#     bk = get_bk(mat)
#     b = bk[0]
#     k = bk[1]
#     click(b, k, mat[b][k], mat)

#     counter = 0
#     for row in mat:
#         for c in row:
#             if c == '*':
#                 counter += 1
#     score += counter * (counter - 1)
#     for i in range(m):
#         for j in range(n):
#             if mat[i][j] == '*':
#                 mat[i][j] = '-'
#     print(score)
