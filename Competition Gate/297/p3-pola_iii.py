import sys

n = sys.stdin.readline()
n = int(n)

count = 0
for i in range(n):
    for j in range(i + 1):
        print(str(count % 10), end='')
        count += 1
    print('')
