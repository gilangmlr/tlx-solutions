import sys

for line in sys.stdin:
    a = int(line)
    if a > 0:
        print('positif')
    elif a < 0:
        print('negatif')
    else:
        print('nol')