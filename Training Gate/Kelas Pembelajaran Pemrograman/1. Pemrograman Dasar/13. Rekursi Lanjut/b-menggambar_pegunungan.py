import sys

n = int(sys.stdin.readline())

def draw(n):
    if n == 1:
        print('*')
        return
    
    draw(n - 1)
    for i in range(n):
        print('*', end='')
    print('')
    draw(n - 1)

draw(n)