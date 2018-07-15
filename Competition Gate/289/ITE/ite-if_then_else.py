import sys

rl = sys.stdin.readline

n = int(rl())

if n > 0:
    print('positif')
elif n < 0:
    print('negatif')
else:
    print('nol')