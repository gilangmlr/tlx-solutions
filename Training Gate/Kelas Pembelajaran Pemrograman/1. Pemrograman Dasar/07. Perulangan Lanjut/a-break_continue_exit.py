import sys

for n in sys.stdin:
    m = int(n)

    for i in range(1, m + 1):
        if i % 10 != 0:
            if i != 42:
                print(i)
            else:
                print('ERROR')
                break