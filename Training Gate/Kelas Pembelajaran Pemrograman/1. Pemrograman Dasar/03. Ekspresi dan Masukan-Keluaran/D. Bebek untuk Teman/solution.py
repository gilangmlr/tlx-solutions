import sys

for line in sys.stdin:
    a, b = line.split()
    res = divmod(int(a), int(b))
    print('masing-masing ' + str(res[0]) + '\nbersisa ' + str(res[1]))