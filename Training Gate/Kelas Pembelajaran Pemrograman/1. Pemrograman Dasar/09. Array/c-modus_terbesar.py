import sys

while True:
    n = sys.stdin.readline()
    if not n:
        break

    line = sys.stdin.readline()
    line = [int(el) for el in line.split()]

    counter = {}
    for i in line:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    
    max_val = 0
    max_key = 0
    for key in counter:
        val = counter[key]
        if val == max_val:
            if key > max_key:
                max_val = val
                max_key = key
        elif val > max_val:
            max_val = val
            max_key = key
    
    print(max_key)