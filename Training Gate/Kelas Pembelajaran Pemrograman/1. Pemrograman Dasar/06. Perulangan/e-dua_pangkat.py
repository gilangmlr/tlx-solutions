import sys

for n in sys.stdin:
    m = int(n)
    while m % 2 == 0:
        m /= 2
    
    if m == 1:
        print('ya')
    else:
        print('bukan')