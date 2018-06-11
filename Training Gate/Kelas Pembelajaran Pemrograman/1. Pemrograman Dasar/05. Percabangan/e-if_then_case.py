import sys

for line in sys.stdin:
    a = int(line)
    i = 0
    while a > 0:
        a //= 10
        i += 1

    res = {
        1: 'satuan',
        2: 'puluhan',
        3: 'ratusan',
        4: 'ribuan',
        5: 'puluhribuan'
    }[i]

    print(res)