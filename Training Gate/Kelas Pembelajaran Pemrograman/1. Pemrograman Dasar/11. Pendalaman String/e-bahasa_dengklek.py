import sys

s = sys.stdin.readline().rstrip()
chs = [ord(i) for i in s]

schs = []
for i in chs:
    diff = 32
    if i >= ord('a'):
        diff *= -1
    schs.append(chr(i + diff))

print(''.join(schs))