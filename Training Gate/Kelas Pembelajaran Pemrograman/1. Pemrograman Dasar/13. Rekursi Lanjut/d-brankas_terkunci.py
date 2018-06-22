import sys

n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)
used = [False for i in range(n + 1)]
perm = [str(i) for i in range(k)]

def permute(n, k):
    if k == 0:
        print(' '.join(perm))
        return
    
    for i in range(1, n + 1):
        perm_idx = len(perm) - k
        if used[i]:
            continue
        if perm_idx >= 1 and perm[perm_idx - 1] > str(i):
            continue
        perm[perm_idx] = str(i)
        used[i] = True
        permute(n, k - 1)
        used[i] = False

permute(n, k)