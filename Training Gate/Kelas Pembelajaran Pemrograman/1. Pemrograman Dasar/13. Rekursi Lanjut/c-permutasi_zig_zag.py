import sys

n = int(sys.stdin.readline())
used = [False for i in range(n + 1)]
perm = [str(i) for i in range(n)]

def permute(n, level):
    if level == 0:
        print(''.join(perm))
    
    for i in range(1, n + 1):
        perm_idx = n - level
        if used[i]:
            continue
        if n >= 3 and perm_idx >= 2:
            if perm[perm_idx - 1] > perm[perm_idx - 2]:
                if str(i) > perm[perm_idx - 1]:
                    continue
            else:
                if str(i) < perm[perm_idx - 1]:
                    continue

        perm[perm_idx] = str(i)
        used[i] = True
        permute(n, level - 1)
        used[i] = False

permute(n, n)