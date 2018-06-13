import sys
from math import sqrt, ceil

while True:
    n = sys.stdin.readline()
    if not n:
        break

    n = int(n)
    for t in range(n):
        a = sys.stdin.readline()
        a = int(a)
        if a == 1:
            print('YA')
            continue
        if a == 2:
            print('YA')
            continue
        
        is_prime = True
        counter = 0
        for i in range(2, ceil(sqrt(a)) + 1):
            if a % i == 0:
                counter += 1
                if counter > 1:
                    print('BUKAN')
                    is_prime = False
                    break
        
        if not is_prime:
            continue

        print('YA')