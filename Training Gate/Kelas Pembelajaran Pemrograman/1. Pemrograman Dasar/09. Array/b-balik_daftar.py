import sys

arr = []
for a in sys.stdin:
    a = int(a)
    arr.append(a)

for i in reversed(arr):
    print(i)